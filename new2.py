import pandas
import pyodbc

conn_string="Driver=ODBC Driver 18 for SQL Server;Server=tcp:server-ha-ya.database.windows.net,1433;Database=database-ha-ya;Uid=UserID-ha-ya;Pwd=P@ssword-ha-ya;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
connection=pyodbc.connect(conn_string)
connection.execute("""Create table ttable_1(
                id int ,
                name varchar(50))  """)

connection.execute("Insert into table_1 (id,name)  values (1,'Amanat'), (2,'Asad'), (3,'Abdullah') ")
connection.commit()
print("Hellow worl222222222222ksjdfhskdfbksjdfksjdbfskjdbfskjdbfjsbfdkjs2222d")
