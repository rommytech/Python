# -*- coding: utf-8 -*-

class BancoGalactico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personajes = []

    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)

    def buscar_personaje(self, nombre):
        for personaje in self.personajes:
            if personaje.nombre == nombre:
                return personaje
        return None
