#Import Lib
import pandas as pd
import psycopg2
from configparser import ConfigParser

#Read Config from config.ini file
config = ConfigParser()
config.read('config.ini')

#Retrive database config
database_config = config['database']
database_name = database_config['database_name']
user = database_config['user']
password = database_config['password']
host = database_config['host']
port = int(database_config['port'])

#Conection to Postgresql
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database_name,
    user=user,
    password=password
)

#Read excel file
df = pd.read_excel("de_challenge_data.xlsx", header=1,sheet_name='FoodSales')

#Pattern for regex
pattern = r"^ID\d+$"

#Filter row by value of ID col
df = df[df["ID"].astype(str).str.match(pattern)]

#Reset index
df = df.reset_index()
df.drop('index', axis=1, inplace=True)

#Create table
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS food_sales (
    ID character varying(10),  
    Date date, 
    Region character varying(25),
    City character varying(50),
    Category character varying(50), 
    Product character varying(50),
    Qty integer,
    UnitPrice numeric(5,2), 
    TotalPrice numeric(10,2)
);
""")

#Insert Data
for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO food_sales (ID, Date, Region, City, Category, Product, Qty, UnitPrice, TotalPrice)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """,
        (row["ID"], row["Date"], row["Region"], row["City"], row["Category"], row["Product"], row["Qty"], row["UnitPrice"], row["TotalPrice"]),
    )

#Create cat_reg table with call sql script
with open("SQL_Script.sql", "r") as sql_file:
    sql_commands = sql_file.read()

cursor.execute(sql_commands)

#Commit
conn.commit()

#Close
conn.close()