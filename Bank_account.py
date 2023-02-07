from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
 
db = SQLAlchemy()

class Name_User(db.Model):
    __tablename__ = "Thông Tin Người Dùng"
    Name = db.Column(db.String,nullable=False)     
    password = db.Column(db.String,primary_key=True)
    
     
