from abc import ABC, abstractmethod
import random
from excepciones import ErrorValidacion

# ============================================
# CLASE ABSTRACTA
# ============================================

class Servicio(ABC):

    def __init__(self, nombre, precio):

        if precio <= 0:
            raise ErrorValidacion(
                "Precio inválido"
            )

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, horas):
        pass


# ============================================
# TIPOS DE SERVICIO
# ============================================

class Sala(Servicio):

    def calcular_costo(self, horas):

        return self.precio * horas


class Equipo(Servicio):

    def calcular_costo(self, horas):

        return (self.precio * horas) + 10


class Asesoria(Servicio):

    def calcular_costo(self, horas):

        return (self.precio * horas) * 1.2


# ============================================
# SIMULACIÓN AUTOMÁTICA SERVICIOS
# ============================================

def simular_servicios():

    servicios_creados = []

    tipos = [
        ("Sala", 50),
        ("Equipo", 20),
        ("Asesoria", 100),
        ("Error", -10)
    ]

    for tipo, precio in tipos:

        try:

            if tipo == "Sala":

                servicio = Sala(tipo, precio)

            elif tipo == "Equipo":

                servicio = Equipo(tipo, precio)

            elif tipo == "Asesoria":

                servicio = Asesoria(tipo, precio)

            else:

                servicio = Sala(tipo, precio)

            servicios_creados.append(servicio)

            print(
                f"✔ Servicio: {servicio.nombre}"
            )

        except ErrorValidacion as e:

            print(
                f"❌ Error servicio: {e}"
            )

    return servicios_creados
