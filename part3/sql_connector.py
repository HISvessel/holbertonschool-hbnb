import mysql.connector

#connects to the sql database and stores a query
conn = mysql.connector.connect(
host="localhost", #place where the query is run
user="myapp_user", #the user name that will have access
password="sumPASS", # username access
database="myapp_db" #the raw file where data is stored
)

#confirming that we connected to the myapp_db database
#opens in a similar way to file I/O, where we open deposit or load and then clsoe
if conn.is_connected():
	print("Successfully connected to MariaDB!")
	conn.close()

