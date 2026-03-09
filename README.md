# Proyecto Flask Inventario

Este proyecto es una aplicación web Flask para gestionar un inventario de productos, implementando persistencia de datos en archivos (TXT, JSON, CSV) y base de datos SQLite con SQLAlchemy.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask
- `form.py`: Formularios WTForms
- `inventario/`: Módulo de inventario
  - `bd.py`: Modelo de base de datos SQLAlchemy
  - `productos.py`: Funciones para persistencia en archivos
  - `data/`: Archivos de datos
- `static/`: Archivos estáticos (CSS)
- `templates/`: Plantillas HTML

## Instalación

1. Crear entorno virtual:
   ```
   python -m venv .venv
   ```

2. Activar entorno virtual:
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`

3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

```
python app.py
```

La aplicación estará disponible en http://127.0.0.1:5000/

## Funcionalidades

- Agregar productos mediante formulario
- Persistencia en archivos TXT, JSON, CSV
- Persistencia en base de datos SQLite
- Visualización de datos almacenados

## Subir a GitHub

1. Crear repositorio en GitHub
2. Agregar remote:
   ```
   git remote add origin <URL_DEL_REPO>
   ```
3. Push:
   ```
   git push -u origin master
   ```