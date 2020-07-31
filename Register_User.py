import mysql.connector
from flask import *

app = Flask(__name__)

 
@app.route('/')  
def message():
	return "<html><body><h1>Hi, welcome to insert_server_local</h1></body></html>"

@app.route('/create')
def createUser():
	 mydb = mysql.connector.connect(
 	 host="localhost",
  	 user="root",
  	 password="Sourab@98",
 	 database="android"
 	  )
	 mycursor=mydb.cursor()
	 query="insert into login values('server','1234')"
	 mycursor.execute(query)
	 mydb.commit()
	 return "Success"
app.run(debug = True,port = 80,host = "0.0.0.0")  

