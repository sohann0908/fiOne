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
     return render_template("signup.html")


@app.route('/Add_card',methods=['POST'])
def Add_card():
     cur = mysql.connect.cursor()
     print(request.form.get("CardNumber"))
     return  render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)
