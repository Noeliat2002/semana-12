import pymysql
from models import db
from models.producto import Producto
from models.usuario import Usuario
from models.factura import Factura
from flask import Flask

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/inventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_database():
    # Conectar a MySQL sin especificar base de datos
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=''
    )
    cursor = connection.cursor()

    # Crear la base de datos si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS inventario")
    print("Base de datos 'inventario' creada o ya existe.")

    cursor.close()
    connection.close()

def create_tables():
    with app.app_context():
        db.create_all()
        print("Tablas creadas exitosamente.")

if __name__ == "__main__":
    create_database()
    create_tables()
    print("Base de datos y tablas listas.")