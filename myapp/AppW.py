import flask
from flask import Flask, redirect, render_template
from flask import request

from config import DevelopmenConfig
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('/myapp/templates/'))
template = env.get_template('main.html')


app= flask.Flask(__name__)
app.config.from_object(DevelopmenConfig)

app.config['DEBUG']= True

@app.route("/",methods=['GET', 'POST'])
def menu():


    return render_template('main.html')



if __name__ =="__main__":
    app.run(debug=True, port=3000)