from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)

# replace mysqldb with pymysql
pymysql.install_as_MySQLdb()

#  db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kstock:lsk.1231@localhost:3306/kstock?charset=UTF8MB4'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# for debug
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)
