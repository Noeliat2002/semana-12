from flask import Flask, render_template, request, redirect, url_for
from inventario.bd import db, Producto, Usuario
from form import ProductoForm, UsuarioForm
from inventario.productos import guardar_txt, leer_txt, guardar_json, leer_json, guardar_csv, leer_csv
import os
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/inventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    productos_db = Producto.query.all()
    return render_template('productos.html', productos=productos_db)

@app.route('/producto_form', methods=['GET', 'POST'])
def producto_form():
    form = ProductoForm()
    if form.validate_on_submit():
        # Guardar en archivos
        datos = {
            'id': len(leer_json()) + 1,
            'nombre': form.nombre.data,
            'precio': form.precio.data,
            'cantidad': form.cantidad.data
        }
        guardar_txt(datos)
        guardar_json(datos)
        guardar_csv(datos)
        
        # Guardar en DB
        producto = Producto(nombre=form.nombre.data, precio=form.precio.data, cantidad=form.cantidad.data)
        db.session.add(producto)
        db.session.commit()
        
        return redirect(url_for('productos'))
    return render_template('producto_form.html', form=form)

@app.route('/usuarios')
def usuarios():
    usuarios_db = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios_db)

@app.route('/usuario_form', methods=['GET', 'POST'])
def usuario_form():
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario = Usuario(nombre=form.nombre.data, mail=form.mail.data, password=form.password.data)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('usuarios'))
    return render_template('usuario_form.html', form=form)

@app.route('/delete_producto/<int:id>')
def delete_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos'))

@app.route('/delete_usuario/<int:id>')
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuarios'))

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/datos')
def datos():
    datos_txt = leer_txt()
    datos_json = leer_json()
    datos_csv = leer_csv()
    productos_db = Producto.query.all()
    usuarios_db = Usuario.query.all()
    return render_template('datos.html', datos_txt=datos_txt, datos_json=json.dumps(datos_json, indent=4), datos_csv=datos_csv, productos_db=productos_db, usuarios_db=usuarios_db)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)