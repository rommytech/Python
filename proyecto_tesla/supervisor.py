# supervisor.py
from empleado import Empleado

class Supervisor(Empleado):
    def __init__(self, nombre, id_empleado):
        super().__init__(nombre, id_empleado)
        self.tecnicos = []

    def agregar_tecnico(self, tecnico):
        self.tecnicos.append(tecnico)
        tecnico.supervisor = self

