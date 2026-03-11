import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',  # Cambia esto por tu contraseña
        database='inventario'  # Cambia esto por el nombre de tu base de datos
    )