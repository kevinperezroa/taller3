from app import db
from app.models import Persona

def get_all_persona():
    return Persona.query.all()

def get_persona_by_id(persona_id):
    return Persona.query.get_or_404(persona_id)

def create_persona(persona_data):
    persona = Persona(
        nombre = persona_data['nombre'],
        direccion = persona_data['direccion'],
        telefono = persona_data['telefono'],
        email = persona_data['email']
    )
    db.session.add(persona)
    db.session.commit()

def update_persona(persona_id,persona_data):
    persona = Persona.query.get_or_404(persona_id)
    persona.nombre = persona_data['nombre']
    persona.direccion = persona_data['direccion']
    persona.telefono = persona_data['telefono']
    persona.email = persona_data['telefono']
    db.session.commit()

def delete_persona(persona_id):
    persona = Persona.query.get_or_404(persona_id)
    db.session.delete(persona)
    db.session.commit()