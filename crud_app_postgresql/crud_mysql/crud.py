import mysql.connector
mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="pycrudsql")
mysqlcursor = mysqldb.cursor()
mysqlcursor.execute("create table users (id int auto_increment primary key, name varchar(50), email varchar(50))")  # creating table

mysqldb.close()