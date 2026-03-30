from . import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    facturas = db.relationship('Factura', backref='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'