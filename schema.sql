-- Script SQL para crear la base de datos y tablas del sistema de inventario

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS inventario;
USE inventario;

-- Tabla de usuarios
CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    mail VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- Tabla de productos
CREATE TABLE producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    cantidad INT NOT NULL
);

-- Tabla de facturas (relaciona usuarios y productos)
CREATE TABLE factura (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES producto(id) ON DELETE CASCADE
);

-- Datos de ejemplo (opcional)
-- INSERT INTO usuario (nombre, mail, password) VALUES ('Juan Perez', 'juan@example.com', 'password123');
-- INSERT INTO producto (nombre, precio, cantidad) VALUES ('Producto A', 10.50, 100);
-- INSERT INTO factura (id_usuario, id_producto, cantidad, total) VALUES (1, 1, 2, 21.00);