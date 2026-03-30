from models.producto import Producto
from models import db

def get_all_productos():
    return Producto.query.all()

def get_producto_by_id(id):
    return Producto.query.get_or_404(id)

def create_producto(nombre, precio, cantidad):
    producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
    db.session.add(producto)
    db.session.commit()
    return producto

def update_producto(id, nombre, precio, cantidad):
    producto = get_producto_by_id(id)
    producto.nombre = nombre
    producto.precio = precio
    producto.cantidad = cantidad
    db.session.commit()
    return producto

def delete_producto(id):
    producto = get_producto_by_id(id)
    db.session.delete(producto)
    db.session.commit()