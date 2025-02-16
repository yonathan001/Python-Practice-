import mysql.connector
mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="pycrudsql")
mysqlcursor = mysqldb.cursor()

 # creating table
mysqlcursor.execute("create table users (id int auto_increment primary key, name varchar(50), email varchar(50))") 

# inserting values
mysqlcursor.execute("insert into users(name,email) values(yoni,user1@gmail.com)") 
mysqldb.commit()
print(mysqlcursor.rowcount, "record inserted") 
mysqldb.close()