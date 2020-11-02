import pyodbc

def read(conn):
    print("read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Sales.Currency")
    for row in cursor:
        print(f'{row[0]} - {row[1]}')
    print()

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=OPTIPLEX\\SQLEXPRESS;"
    "Database=AdventureWorks2017;"
    "Trusted_Connection=yes;"
)

read(conn)
conn.close()
