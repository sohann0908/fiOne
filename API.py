from flask import Flask, render_template, request, flash, redirect, url_for,jsonify
from flask_mysqldb import MySQL
import mysql.connector
# from passlib.hash import sha256_crypt





app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Aniketraut@04'
app.config['MYSQL_DB'] = 'Fiserv'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)
        

@app.route('/')
def index():
     cur = mysql.connect.cursor()
     cur.execute("Select * from BankCards where mobile_number=1234567890")
     answer = cur.fetchall()
     return jsonify(answer)


@app.route('/Add_card',methods=['POST'])
def Add_card():
     return "Added Card request get"

     





if __name__ == "__main__":
    app.run(debug=True)
