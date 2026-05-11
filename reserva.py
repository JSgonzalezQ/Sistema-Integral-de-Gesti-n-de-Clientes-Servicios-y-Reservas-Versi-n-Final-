from excepciones import ErrorValidacion

# ================================
# CLASE RESERVA
# ================================
# Clase encargada de gestionar reservas

class Reserva:
    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
# Verifica que las horas sean válidas
    def procesar(self):
        if self.horas <= 0:
            raise ErrorValidacion("Horas inválidas")
# Procesa la reserva y calcula el costo
        return self.servicio.calcular_costo(self.horas)
    
