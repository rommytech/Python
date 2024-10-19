# tecnico.py
from empleado import Empleado

class Tecnico(Empleado):
    def __init__(self, nombres, id_empleado, especialidad):  # Cambia a 'nombres'
        super().__init__(nombres, id_empleado)  # Usa 'nombres' en lugar de 'nombre'
        self.especialidad = especialidad
