

import mysql.connector

cnx = mysql.connector.connect(user='root', password='0pl,9okM!?', host='localhost')

cursor = cnx.cursor()

cursor.execute("CREATE DATABASE python_youtube")



