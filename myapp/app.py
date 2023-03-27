import flask
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from config import DevelopmenConfig
from flask_wtf.csrf import CSRFProtect
from models import db


app= flask.Flask(__name__)
csrf= CSRFProtect()
app.config.from_object(DevelopmenConfig)

app.config['DEBUG']= True

@app.route("/",methods=['GET', 'POST'])
def home():


    return render_template('main.html')



if __name__ =="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
         db.create_all()
    app.run(debug=True, port=3000)