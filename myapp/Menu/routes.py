from flask import Blueprint, redirect
import flask
from flask import Flask, render_template
from flask import request
from flask import url_for
import forms
from config import DevelopmenConfig
from models import db
from models import Alumnos

menu = Blueprint('menu' , __name__)

@alumnos.route('/getAlum',methods=['GET','POST'])
def getalum():
    btn = request.form.get("registrarAlum")
    btn2 = request.form.get("modificar")
    create_form = forms.UserForm(request.form)
    if request.method=='POST':
        if btn == 'Registrar Alumno':
            alum = Alumnos(nombre= create_form.nombre.data,
                        apellidos = create_form.apellidos.data,
                        email = create_form.email.data)
            db.session.add(alum)
            db.session.commit()
        if btn2 == 'modificar':
            return redirect(url_for('alumnos.ABCompleto'))
    return render_template('index.html',form=create_form)






   
