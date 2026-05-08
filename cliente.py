import random
from excepciones import ErrorValidacion

# ============================================
# GENERADOR DE DATOS
# ============================================

def generar_nombre():
    nombres = [
        "Juan", "Ana", "Luis", "Camila", "Pedro",
        "Sofia", "Andres", "Valentina"
    ]

    apellidos = [
        "Gomez", "Rodriguez", "Martinez",
        "Lopez", "Garcia", "Perez"
    ]

    return f"{random.choice(nombres)} {random.choice(apellidos)}"


def generar_correo(nombre):
    dominios = ["gmail.com", "hotmail.com", "outlook.com"]

    base = nombre.lower().replace(" ", "")
    numero = random.randint(1, 999)

    return f"{base}{numero}@{random.choice(dominios)}"


def generar_navegador():
    return random.choice([
        "Chrome",
        "Firefox",
        "Edge",
        "Safari"
    ])


# ============================================
# CLASE CLIENTE
# ============================================

class Cliente:

    def __init__(self, nombre, correo, navegador):

        if "@" not in correo or "." not in correo:
            raise ErrorValidacion("Correo inválido")

        self.nombre = nombre
        self.correo = correo
        self.navegador = navegador

    def mostrar_datos(self):

        return (
            f"Cliente: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Navegador: {self.navegador}"
        )


# ============================================
# SIMULACIÓN AUTOMÁTICA CLIENTES
# ============================================

def simular_clientes(cantidad=5):

    clientes = []

    for _ in range(cantidad):

        try:

            nombre = generar_nombre()
            correo = generar_correo(nombre)
            navegador = generar_navegador()

            cliente = Cliente(
                nombre,
                correo,
                navegador
            )

            clientes.append(cliente)

            print("✔", cliente.mostrar_datos())

        except ErrorValidacion as e:

            print("❌ Error cliente:", e)

    return clientes
