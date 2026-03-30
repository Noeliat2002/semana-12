from . import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    facturas = db.relationship('Factura', backref='producto', lazy=True)

    def __repr__(self):
        return f'<Producto {self.nombre}>'