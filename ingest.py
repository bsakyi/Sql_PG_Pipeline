import dbconnection


# Assign the cursor and connection functions to variables
sqlcur, sqlcon = dbconnection.connect_mysql()
pgcur, pgcon = dbconnection.connect_postgres()

# Execute the table creation query in PostgreSQL
pgcreate_table = """CREATE TABLE IF NOT EXISTS customers (
    id integer,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender CHAR(1),
    date_of_birth date,
    contact_number VARCHAR(20)
)"""
pgcur.execute(pgcreate_table)
pgcon.commit()

# Execute query to retrieve data from MySQL
sqlcur.execute("SELECT * FROM customers")
mysql_data = sqlcur.fetchall()

print(mysql_data)

# Insert data into PostgreSQL
for row in mysql_data:
    pgcur.execute("INSERT INTO customers (id, first_name, last_name, gender, date_of_birth, contact_number) VALUES (%s, %s, %s, %s, %s, %s)", row)

pgcon.commit()

# Close connections
pgcur.close()
pgcon.close()
sqlcur.close()
sqlcon.close()
