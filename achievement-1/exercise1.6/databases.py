import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()
my_query = '''CREATE TABLE inventory(
    item_id             INT,
    item_name           VARCHAR(50),
    price               FLOAT,
    qty                 INT
)'''
cursor.execute(my_query)
cursor.execute('USE inventory')
