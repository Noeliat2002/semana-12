from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class FacturaForm(FlaskForm):
    id_usuario = SelectField('Usuario', coerce=int, validators=[DataRequired()])
    id_producto = SelectField('Producto', coerce=int, validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    submit = SubmitField('Crear Factura')