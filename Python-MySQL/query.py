import mysql.connector

dbName = "python_test_db"
myDBConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database= dbName
)

myCursor = myDBConnection.cursor();

sqlQuery_createDB = "create database " + dbName

sqlQuery_createTable =  """
            create table Student (
                roll char(4) primary key,
                name varchar(15)
            )
            """

sqlQuery_insertIntoTable =  """
            insert into Student(roll, name) values('4', 'riyad')
            """


myCursor.execute(sqlQuery_insertIntoTable);
myDBConnection.commit()