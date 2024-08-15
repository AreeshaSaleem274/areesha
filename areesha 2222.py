import pandas as pd
import pyodbc

# Define the connection string
conn_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:server-ha-ya.database.windows.net,1433;"
    "Database=database-ha-ya;"
    "Uid=UserID-ha-ya;"
    "Pwd=P@ssword-ha-ya;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

# Establish the connection
connection = pyodbc.connect(conn_string)

# Create a new table
create_table_query = """
CREATE TABLE digi (
    id INT,
    name VARCHAR(50)
);
"""
with connection.cursor() as cursor:
    cursor.execute(create_table_query)
    connection.commit()
print("Table created successfully.")

# Insert data into the table
insert_data_query = """
INSERT INTO digi (id, name) VALUES
    (1, 'Kainat'),
    (2, 'Asad'),
    (3, 'Areesha');
"""
with connection.cursor() as cursor:
    cursor.execute(insert_data_query)
    connection.commit()
print("Data inserted successfully.")

# Query the table to verify data insertion
select_query = "SELECT * FROM digi"
data_frame = pd.read_sql(select_query, connection)
print(data_frame)

# Close the connection
connection.close()
print("Connection closed.")

# Print a hello message
print("Hello world")
