"""
import mysql.connector as mc

mydb = mc.connect(host='localhost', user="root", password='Datha@123')

mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)

"""



from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="127.0.0.1:3306",
        user='root',
        password='Datha@123',
        database='pets'
    ) as connection:
        print(connection)
except Error as e:
    print(e)


"""
import mysql.connector
from mysql.connector import Error

try:
    connection_config_dict = {
        'host': '127.0.0.1:3306',
        'user': 'root',
        'password': 'Datha@123',
        'database': 'pets',
        }
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
"""

import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="datha",
  passwd="Datha@123"
)
print(db_connection)