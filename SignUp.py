from flask import Flask, request, render_template
from Bank_account import *
 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/Name_SignUp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/SignUp")

def name_user():

    return render_template("index.html")


@app.route("/profile")

def profile():

    name = request.args.get("Name")
    password = request.args.get("password")
  
    name_user = Name_User(Name=name, password=password)
    db.session.add(name_user)  
    db.session.commit()

    return f"<h1>Đăng ký thành công rồi nhé {name}</h1>"
    