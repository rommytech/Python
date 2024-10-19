from flask import Flask, render_template, request
from utils import guardar_pedidos_csv, contar_pedidos_csv  # Importa la nueva función
from models.pedido import Pedido

app = Flask(__name__)

# Ruta para la página de inicio
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guardar_pedido", methods=["POST"])
def guardar_pedido():
    # Obtener los datos del formulario
    nombres = request.form.get("nombres")
    producto = request.form.get("producto")
    fecha_entrega = request.form.get("fecha_entrega")
    descripcion = request.form.get("descripcion")
    
    # Crear instancia de Pedido
    mi_pedido = Pedido(nombres, producto, fecha_entrega, descripcion)
    
    # Validar el pedido
    errors = mi_pedido.is_valid()
    
    # Si hay errores, devolver la página de agradecimiento con el mensaje de error
    if len(errors) > 0:
        return render_template("gracias.html", data={"error": str(errors)})
    
    # Guardar los datos en el archivo CSV
    guardar_pedidos_csv(nombres, producto, fecha_entrega, descripcion)
    
    # Contar la cantidad de registros/pedidos
    cantidad_pedidos = contar_pedidos_csv()
    
    # Generar un número de pedido (usando la cantidad de registros)
    numero_pedido = cantidad_pedidos
    
    # Redirigir a la página de agradecimiento con el número de pedido y la cantidad de pedidos
    return render_template("gracias.html", data={"n_order": numero_pedido, "total_pedidos": cantidad_pedidos})

if __name__ == "__main__":
    app.run(debug=True)
