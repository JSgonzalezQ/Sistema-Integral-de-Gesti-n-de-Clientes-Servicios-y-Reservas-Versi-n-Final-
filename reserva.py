from excepciones import ErrorValidacion

# ================================
# CLASE RESERVA
# ================================
class Reserva:
    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas

    def procesar(self):
        if self.horas <= 0:
            raise ErrorValidacion("Horas inválidas")

        return self.servicio.calcular_costo(self.horas)
    
