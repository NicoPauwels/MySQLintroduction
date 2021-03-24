import os
import pymysql

#Get username

username = os.getenv('C9_USER')

#Connect to the database

connection = pymysql.connect(host='localhost',
                                user=username,
                                password='',
                                db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * From Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection
    connection.close()