from app import db

class Persona(db.Model):
    __tablename__='persona'
    id   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50),nullable=False)
    telefono = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f'<Persona {self.id}>'
