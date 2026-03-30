from flask import Flask, render_template, request, redirect, url_for, send_file
from models import db
from models.producto import Producto
from models.usuario import Usuario
from models.factura import Factura
from forms.producto_form import ProductoForm
from forms.usuario_form import UsuarioForm
from forms.factura_form import FacturaForm
from services.producto_service import *
from inventario.productos import guardar_txt, leer_txt, guardar_json, leer_json, guardar_csv, leer_csv
import os
import pymysql
import json
import json
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors

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
    productos_db = get_all_productos()
    return render_template('productos/productos.html', productos=productos_db)

@app.route('/edit_producto/<int:id>', methods=['GET', 'POST'])
def edit_producto(id):
    producto = get_producto_by_id(id)
    form = ProductoForm(obj=producto)
    if form.validate_on_submit():
        update_producto(id, form.nombre.data, form.precio.data, form.cantidad.data)
        return redirect(url_for('productos'))
    return render_template('productos/producto_form.html', form=form, producto=producto)

@app.route('/usuarios')
def usuarios():
    usuarios_db = Usuario.query.all()
    return render_template('usuarios/usuarios.html', usuarios=usuarios_db)

@app.route('/edit_usuario/<int:id>', methods=['GET', 'POST'])
def edit_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    form = UsuarioForm(obj=usuario)
    if form.validate_on_submit():
        usuario.nombre = form.nombre.data
        usuario.mail = form.mail.data
        usuario.password = form.password.data
        db.session.commit()
        return redirect(url_for('usuarios'))
    return render_template('usuarios/usuario_form.html', form=form, usuario=usuario)

@app.route('/delete_producto/<int:id>')
def delete_producto(id):
    delete_producto(id)
    return redirect(url_for('productos'))

@app.route('/delete_usuario/<int:id>')
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuarios'))

@app.route('/facturas')
def facturas():
    facturas_db = Factura.query.all()
    return render_template('facturas/facturas.html', facturas=facturas_db)

@app.route('/factura_form', methods=['GET', 'POST'])
def factura_form():
    form = FacturaForm()
    form.id_usuario.choices = [(u.id_usuario, u.nombre) for u in Usuario.query.all()]
    form.id_producto.choices = [(p.id, p.nombre) for p in Producto.query.all()]
    if form.validate_on_submit():
        producto = Producto.query.get(form.id_producto.data)
        total = producto.precio * form.cantidad.data
        factura = Factura(id_usuario=form.id_usuario.data, id_producto=form.id_producto.data, cantidad=form.cantidad.data, total=total)
        db.session.add(factura)
        db.session.commit()
        return redirect(url_for('facturas'))
    return render_template('facturas/factura_form.html', form=form)

@app.route('/delete_factura/<int:id>')
def delete_factura(id):
    factura = Factura.query.get_or_404(id)
    db.session.delete(factura)
    db.session.commit()
    return redirect(url_for('facturas'))

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

@app.route('/reporte_pdf')
def reporte_pdf():
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph("Reporte de Productos", styles['Title'])
    elements.append(title)

    # Table data
    productos = Producto.query.all()
    data = [['ID', 'Nombre', 'Precio', 'Cantidad']]
    for p in productos:
        data.append([str(p.id), p.nombre, str(p.precio), str(p.cantidad)])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    doc.build(elements)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='reporte_productos.pdf', mimetype='application/pdf')

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)