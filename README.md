# Coraline Data Engineer Challenge

This is a repository for assignment interviews in data engineer role.


## Table of content

- [installation guide](#installation-guide)
- [how to use](##How%20to%20use)

## Installation guide

``` bash
git clone https://github.com/FOLKGG/Coraline_challenge.git

cd Coraline_challenge

pip install requirements.txt
```

## How to use 
1. Make sure the path is still .\Coraline_challenge
``` bash
#Make sure you still in Coraline_challenge by
pwd
#if not please change to Coraline_challenge
cd Coraline_challenge
```

2.  Run Python_Script.py
``` bash
#Run Python Script
python Python_Script.py
```
This part will call script name 'Python_Script.py' that will ingest data from Excel sheet to Postgresql database as table name  'food_sales'

3.  Run SQL_Script.py
``` bash
#Run SQL Script
psql -h localhost -d challenge -U root -f SQL_Script.sql

#After that command system will ask password and then paste this password
DataEngineer_2023

```
After SQL command you will see new table name 'cat_reg' that contain sumarize price data from 'food_sales' table
