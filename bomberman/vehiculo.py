from bomber import Bomberman
class Vehiculo:

    """Define clase vehiculo"""

    def __init__(self, modelo, color, marca, velocidad, c_pasajeros, peso):
        """Init de clase"""
        self.modelo = str(modelo)
        self.color = str(color)
        self.marca = str(marca)
        self.velocidad = velocidad
        self.c_pasajeros = str(c_pasajeros)
        self.peso = int(peso)

    def prender_vehiculo(self):
        print("Prender Vehiculo")

    def apagar_vehiculo(self):
        print("Apagar Vehiculo")

    def __str__(self):
        return f"Modelo: {self.modelo}, Color: {self.color}, Marca: {self.marca}, Velocidad: {self.velocidad}, Pasajeros: {self.c_pasajeros}, Peso: {self.peso} kg"


class Aereo(Vehiculo, Bomberman):
    """Define clase Aereo"""
    def __init__(self, modelo, color, marca, velocidad, c_pasajeros, peso, n_vuelo, h_vuelo, h_salida, name, pos_x, pos_y):
        Vehiculo.__init__(self, modelo, color, marca, velocidad, c_pasajeros, peso)
        Bomberman.__init__(self, name, pos_x, pos_y)

        """Funcion detalles para Aereo"""
        super().__init__(modelo, color, marca, velocidad, c_pasajeros, peso)
        self.n_vuelo = int(n_vuelo)
        self.h_vuelo = h_vuelo
        self.h_salida = h_salida
        self.set_image("airplane.png")

    def elevar(self):
        print("Elevar vehiculo")

    def aterrizar(self):
        print("Aterrizar vehiculo")

    def __str__(self):
        return super().__str__() + f", Número de Vuelo: {self.n_vuelo}, Hora de Vuelo: {self.h_vuelo}, Hora de Salida: {self.h_salida}"


class Terrestre(Vehiculo):
    """Define clase Terrestre"""

    def __init__(self, modelo, color, marca, velocidad, c_pasajeros, peso, n_puertas, c_carga):
        """Funcion detalles para Terrestre"""
        super().__init__(modelo, color, marca, velocidad, c_pasajeros, peso)
        self.n_puertas = int(n_puertas)
        self.c_carga = c_carga

    def marchar(self):
        print("Marchar vehiculo")

    def frenar(self):
        print("Frenar vehiculo")

    def __str__(self):
        return super().__str__() + f", Número de Puertas: {self.n_puertas}, Capacidad de Carga: {self.c_carga}"


class Maritimo(Vehiculo):
    """Define clase Maritimo"""

    def __init__(self, modelo, color, marca, velocidad, c_pasajeros, peso, c_carga):
        """Funcion detalles para Maritimo"""
        super().__init__(modelo, color, marca, velocidad, c_pasajeros, peso)
        self.c_carga = c_carga

    def navegar(self):
        print("Navegar")

    def __str__(self):
        return super().__str__() + f", Capacidad de Carga: {self.c_carga}"

# Creando una instancia de Maritimo
maritimo1 = Maritimo("Barco1", "Blanco", "Waterfall", "24 km/h", "450", 1000, "1 ton")
print(maritimo1)
