

import mysql.connector

cnx = mysql.connector.connect(user='root', password='', host='localhost')

cursor = cnx.cursor()

cursor.execute("CREATE DATABASE python_youtube")



