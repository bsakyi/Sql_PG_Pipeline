import psycopg2
import mysql.connector

# MySQL connection (source db)
def connect_mysql():
    conn = mysql.connector.connect(host="localhost", port=3306, user="root", password="", db="appleinc")
    cur = conn.cursor()
    return cur, conn

# PostgreSQL connection (destination db)
def connect_postgres():
    conn = psycopg2.connect(host="localhost", database="firstpipe", port=5454, user="postgres", password="hello")
    cur = conn.cursor()
    return cur, conn