from abc import ABC, abstractmethod
from excepciones import ErrorValidacion

# ================================
# CLASE SERVICIO
# ================================
class Servicio(ABC):
    def __init__(self, nombre, precio):
        if precio <= 0:
            raise ErrorValidacion("Precio inválido")
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, horas, descuento=0):
        pass


class Sala(Servicio):
    def calcular_costo(self, horas, descuento=0):
        return (self.precio * horas) - descuento


class Equipo(Servicio):
    def calcular_costo(self, horas, descuento=0):
        return (self.precio * horas + 10) - descuento


class Asesoria(Servicio):
    def calcular_costo(self, horas, descuento=0):
        return (self.precio * horas * 1.2) - descuento