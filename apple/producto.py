class Producto:
    #_nombre: Parametro del constructor
    #self.nombre: Atributo de la clase
    def __init__(self, _nombre, _precio, _fecha_lanzamiento):
        self.nombre = _nombre # Solicita al usuario
        self.precio = _precio # Solicita al usuario
        self.fecha_lanzamiento = _fecha_lanzamiento # Solicita al usuario
        self.marca = "Apple" # Atributo es por defecto
        ###
        #   Puedes anadir otras acciones, cuando 
        #   se crea la instancia de la clase
        ###
    
    def detalles(self):
        #Interpolacion
        return f"Producto: {self.nombre}, Precio: ${self.precio}, F. Lanzamiento: {self.fecha_lanzamiento}"

class IPhone(Producto):
    def __init__(self, _nombre, _precio, _fecha_lanzamiento, _capacidad_bateria):
        # Super, se conecta con el padre la clase
        # Le envia los parametros que necesita el padre
        super().__init__(_nombre, _precio, _fecha_lanzamiento)
        
        self.capacidad_bateria = _capacidad_bateria

    def detalles(self):
        detalle_padre = super().detalles()
        return f"{detalle_padre}, C. Bateria: {self.capacidad_bateria}"

class MacBook(Producto):
    def __init__(self, _nombre, _precio, _fecha_lanzamiento, _ram):
        super().__init__(_nombre, _precio, _fecha_lanzamiento) # Herencia
        
        self.ram = _ram
    
    def detalles(self):
        detalle_padre = super().detalles()
        return f"{detalle_padre}, RAM: {self.ram}"

productox = Producto("iPad", 56000, "2026-03-12")
print(productox.detalles())

mi_iphone = IPhone("iPhone", 67000, "2027-12-12", "24 horas")
# mi_iphone es una instancia de IPhone
print(mi_iphone.detalles())

mi_macbook = MacBook("Macbook 13inc", 454545, "2025-12-12", "16 GB.")
print(mi_macbook.detalles())


class InventarioApple:
    def __init__(self):
        # Al momento de crear la instancia
        # el atributos se define como array vacio
        self.productos = []

    def agregar_producto(self, producto):
        # Recibe una instancia producto como parametro
        self.productos.append(producto)
        # Incluimos el producto en el atributo productos
    
    def mostrar_inventario(self):
        print("Reporte Inventario")
        print("==================")
        for pro in self.productos:
            print(pro.detalles()) #<------

inventario = InventarioApple()
# inventario es una instancia de InventarioApple
inventario.agregar_producto(Producto("AirTag", 3434, "2024-11-12"))
# anadimos una instancia de la clase Producto
inventario.agregar_producto(IPhone("iPhone 14", 34344, "2024-01-12", "24 horas"))
# anadimos una instancia de la clase IPhone
inventario.agregar_producto(MacBook("Macbook pro", 34344, "2022-01-12", "16 GB"))
# anadimos una instancia de la clase Macbook

inventario.mostrar_inventario()
