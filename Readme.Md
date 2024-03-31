# Project README

## Overview
This project contains the code for transferring data from MySQL to PostgreSQL.
It does extraction and loading. 

## Files
- `ingest.py`: Contains the code for the data transfer pipeline.
- `dbconnection.py`: Contains functions to connect to MySQL and PostgreSQL databases.

## Instructions
1. Ensure that both MySQL and PostgreSQL databases are set up and accessible.
2. Modify the connection parameters in `dbconnection.py` as per your database configurations.
3. Run `pipeline.py` to transfer data from MySQL to PostgreSQL.

## Requirements
- Python 3.x
- `psycopg2` library for PostgreSQL connectivity
- `mysql-connector-python` library for MySQL connectivity

## Usage
```bash
python pipeline.py
