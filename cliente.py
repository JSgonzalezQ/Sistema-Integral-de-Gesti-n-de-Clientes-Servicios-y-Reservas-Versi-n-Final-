from excepciones import ErrorValidacion

# ================================
# CLASE CLIENTE
# ================================
class Cliente:

    def __init__(self, nombre, correo, navegador):

        if "@" not in correo or "." not in correo:
            raise ErrorValidacion("Correo inválido")

        self.nombre = nombre
        self.correo = correo
        self.navegador = navegador