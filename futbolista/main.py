class SeleccionFutbol:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def concentrarse(self):
        return f"{self.nombre} está concentrándose."
    
    def viajar(self):
        return f"{self.nombre} está viajando."


class Futbolista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion
    
    def jugarPartido(self):
        return f"{self.nombre} está jugando un partido en la posición de {self.demarcacion}."
    
    def entrenar(self):
        return f"{self.nombre} está entrenando."


class Entrenador(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)
        self.idFederacion = idFederacion
    
    def dirigirPartido(self):
        return f"{self.nombre} está dirigiendo un partido."
    
    def dirigirEntrenamiento(self):
        return f"{self.nombre} está dirigiendo un entrenamiento."


class Masajista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, titulacion, aniosExperiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.aniosExperiencia = aniosExperiencia
    
    def darMasajes(self):
        return f"{self.nombre} está dando masajes."

futbolista = Futbolista(1, "Lionel", "Messi", 35, 10, "Delantero")
print(futbolista.concentrarse())
print(futbolista.jugarPartido())

entrenador = Entrenador(2, "Pep", "Guardiola", 50, "12345")
print(entrenador.viajar())
print(entrenador.dirigirEntrenamiento())

masajista = Masajista(3, "Juan", "Perez", 40, "Fisioterapia", 15)
print(masajista.darMasajes())
