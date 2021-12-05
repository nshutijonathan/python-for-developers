import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()
create_table = 'CREATE DATABASE IF NOT EXISTS  task_database'
cursor.execute(create_table)
cursor.execute('USE  task_database')
cursor.execute(
    'CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY, name VARCHAR(50),ingredients VARCHAR(255),cooking_time INTEGER ,difficulty VARCHAR(10)')
cursor.main_menu(conn, cursor)
cursor
