from flask import Flask,render_template,flash,redirect,url_for,session,logging,request,g
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators, SubmitField
from passlib.hash import sha256_crypt 
from functools import wraps
import hashlib


app = Flask(__name__)
app.secret_key= "isdfgrhsri"

# 


app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "forumapp"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntüleme izniniz yok", "danger")
            return redirect(url_for("index"))
    return decorated_function


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug= True)