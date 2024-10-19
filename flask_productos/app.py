from flask import Flask, render_template, request, redirect, url_for
from models.producto import Producto

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener la cantidad de productos registrados
    cantidad_productos = Producto.contar_registros()
    return render_template('index.html', data={
        'cantidad_productos': cantidad_productos
    })

@app.route('/registrar_producto', methods=['POST'])
def registrar_producto():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    precio = request.form.get('precio')
    descripcion = request.form.get('descripcion')

    # Crear una instancia del producto
    producto = Producto(nombre, float(precio), descripcion)

    # Validar el producto
    if producto.is_valid():
        # Guardar el producto si es válido
        producto.save()
        return redirect(url_for('index'))
    else:
        return "Datos inválidos, intenta de nuevo", 400

if __name__ == '__main__':
    app.run(debug=True)
