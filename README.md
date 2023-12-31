# Coraline Data Engineer Challenge

This is a repository for assignment interviews in data engineer role.

## Table of content

- [installation guide](#installation-guide)
- [setup database](#setup-database)
- [how to use](##How%20to%20use)

## Installation guide

``` bash
git clone https://github.com/FOLKGG/Coraline_challenge.git

cd Coraline_challenge

pip install requirements.txt
```
## Setup database 

> **This part not include postgresql software installation. You can find installation guide in youtube or postgresql official website**

**You can skip this part if you already have.**

**1. Access PostgreSQL:**
-   Open a terminal or command prompt.
-   Connect to the PostgreSQL server using the  `psql`  command:
    -   `psql -U postgres` (Connect via the default "postgres" user)

**2. Step:**
``` bash
#Create the database
CREATE DATABASE challenge;

#Create User
CREATE  USER root WITH PASSWORD 'DataEngineer_2023';

#Grant privileges to the user
GRANT  ALL PRIVILEGES ON DATABASE challenge TO root;
```
**3. Verify:**

-   Exit  `psql`  using  `\q`.
-   Connect to the new database as the  `root`  user:
    ``` bash
    psql -U root challenge
    ```
-   If successful, you'll be connected to the  `challenge`  database.

## How to use 
**1. Make sure path still .\Coraline_challenge**
``` bash
#Make sure you are still in Coraline_challenge by
pwd
#if not please change to Coraline_challenge
cd Coraline_challenge
```

**2.  Run Python_Script.py**
``` bash
#Run Python Script
python Python_Script.py
```
This part will call script name 'Python_Script.py' that will ingest data from Excel sheet to Postgresql database as table name  'food_sales'

**3.  Run SQL_Script.py**
``` bash
#Run SQL Script
psql -h localhost -d challenge -U root -f SQL_Script.sql

#After that command system will ask password and then past this password
DataEngineer_2023

```
After SQL command you will see new table name 'cat_reg' that contain sumarize price data from 'food_sales' table
