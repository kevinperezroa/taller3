from flask import render_template, request, redirect, url_for
from app import app,db
from app.models import Persona

@app.route('/')
def index():
    personas = Persona.query.all()
    return render_template('index.html',personas = personas)

@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        new_persona = Persona(nombre=nombre, direccion=direccion, telefono=telefono, email=email)
        db.session.add(new_persona)
        db.session.commit()
        return redirect(url_for('index.html'))
    return render_template('create.html')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    persona = persona.query.get_or_404(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        db.session.commit()
        return redirect(url_for('index.html'))
    return render_template('create.html')

@app.route('/delete/<int:id>')
def update(id):
    persona = persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('index.html'))
