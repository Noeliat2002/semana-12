from Conexión.conexion import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Crear tabla usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        mail VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL
    )
    """)
    
    # Crear tabla productos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS producto (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        precio FLOAT NOT NULL,
        cantidad INT NOT NULL
    )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tablas creadas.")