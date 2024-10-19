from datetime import datetime

class Pedido:
    def __init__(self, nombres, producto, fecha_entrega, descripcion):
        self.nombres = nombres
        self.producto = producto
        self.fecha_entrega = fecha_entrega
        self.descripcion = descripcion
    
    def is_valid(self):
        errors = []

        # Validación de nombre
        if len(self.nombres.strip()) <= 1:
            errors.append("Ingrese un nombre correcto.")
        
        # Validación de descripción
        if len(self.descripcion.strip()) <= 3:
            errors.append("Ingrese una descripción correcta.")
        
        # Validación de fecha: no puede ser en el pasado
        try:
            fecha_entrega_date = datetime.strptime(self.fecha_entrega, "%Y-%m-%d")
            fecha_actual = datetime.now()
            if fecha_entrega_date < fecha_actual:
                errors.append("Ingrese una fecha correcta.")
        except ValueError:
            errors.append("Ingrese una fecha válida en formato AAAA-MM-DD.")
        
        return errors

    def notificar(self):
        # Simulación de notificación
        print(f"Notificación enviada para el pedido de {self.nombres}. Producto: {self.producto}")
