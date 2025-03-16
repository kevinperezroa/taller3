from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import Persona

@app.route('/', methods=['GET'])
def index():
    personas = Persona.query.all()
    
    if request.headers.get('Content-Type') == 'application/json':
        personas_json = [{"id": p.id, "nombre": p.nombre, "direccion": p.direccion, "telefono": p.telefono, "email": p.email} for p in personas]
        return jsonify(personas_json), 200

    return render_template('index.html', personas=personas)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = request.get_json()
        else:
            data = request.form
        
        nombre = data.get('nombre')
        direccion = data.get('direccion')
        telefono = data.get('telefono')
        email = data.get('email')

        if not nombre or not direccion or not telefono or not email:
            return jsonify({"error": "Faltan datos"}), 400

        new_persona = Persona(nombre=nombre, direccion=direccion, telefono=telefono, email=email)
        db.session.add(new_persona)
        db.session.commit()

        if request.headers.get('Content-Type') == 'application/json':
            return jsonify({"message": "Persona creada", "persona": {
                "id": new_persona.id,
                "nombre": new_persona.nombre,
                "direccion": new_persona.direccion,
                "telefono": new_persona.telefono,
                "email": new_persona.email
            }}), 201

        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST', 'PUT'])
def update(id):
    persona = Persona.query.get_or_404(id)

    if request.method in ['POST', 'PUT']:
        if request.headers.get('Content-Type') == 'application/json':
            data = request.get_json()
        else:
            data = request.form
        
        persona.nombre = data.get('nombre', persona.nombre)
        persona.direccion = data.get('direccion', persona.direccion)
        persona.telefono = data.get('telefono', persona.telefono)
        persona.email = data.get('email', persona.email)

        db.session.commit()

        if request.headers.get('Content-Type') == 'application/json':
            return jsonify({"message": "Persona actualizada", "persona": {
                "id": persona.id,
                "nombre": persona.nombre,
                "direccion": persona.direccion,
                "telefono": persona.telefono,
                "email": persona.email
            }}), 200

        return redirect(url_for('index'))

    return render_template('update.html', persona=persona)


@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()

    if request.headers.get('Content-Type') == 'application/json':
        return jsonify({"message": "Persona eliminada"}), 200

    return redirect(url_for('index'))
