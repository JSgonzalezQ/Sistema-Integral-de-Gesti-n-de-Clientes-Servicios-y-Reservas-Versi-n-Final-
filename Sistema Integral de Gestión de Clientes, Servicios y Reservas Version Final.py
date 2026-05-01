from abc import ABC, abstractmethod
import logging
import tkinter as tk
import random

# ============================================
# LOG ; INFORMACION REGISTRADA EN EL SISTEMA 
# ============================================
logging.basicConfig(
    filename="registro_sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ErrorValidacion(Exception):
    pass

# ================================
# GENERADOR DE NOMBRES RAMDOMS
# ================================
def generar_nombre():
    nombres = [
        "Juan", "Ana", "Luis", "Camila", "Pedro", "Sofia",
        "Andres", "Valentina", "Carlos", "Laura",
        "Diego", "Mariana", "Sebastian", "Daniela"
    ]

    apellidos = [
        "Gomez", "Rodriguez", "Martinez", "Lopez",
        "Garcia", "Hernandez", "Perez", "Sanchez",
        "Ramirez", "Torres", "Castro", "Vargas"
    ]

    return f"{random.choice(nombres)} {random.choice(apellidos)}"


def generar_correo(nombre):
    dominios = ["gmail.com", "hotmail.com", "outlook.com"]
    base = nombre.lower().replace(" ", "")
    numero = random.randint(1, 999)
    return f"{base}{numero}@{random.choice(dominios)}"


def generar_password():
    opciones = ["123", "abc", "segura123", "claveFuerte", "pass", "admin"]
    return random.choice(opciones)


def generar_navegador():
    return random.choice(["Chrome", "Firefox", "Edge", "Safari", "Brave"])


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


# ======================================================
# MOSTRAR RESULTADOS SIN QUE EL USUARIO PUEDA EDITARLOS
# ======================================================
def insertar_texto(widget, texto, tag=None):
    widget.config(state="normal")
    widget.insert(tk.END, texto + "\n", tag)
    widget.config(state="disabled")


# ================================
# SIMULACIÓN
# ================================
def ejecutar():

    # TIPOS DE ERROR
    servicios = [
        ("Sala", 50),
        ("Equipo", 20),
        ("Asesoria", 100),
        ("ErrorPrecio", -5),
        ("ErrorNombre", 30),
        ("ErrorLogico", 40)
    ]

    for _ in range(8):

        # DATOS DINÁMICOS
        nombre = generar_nombre()
        correo = generar_correo(nombre)
        password = generar_password()
        navegador = generar_navegador()

        # ====================
        # REGISTRO
        # ====================
        try:
            if len(password) < 5:
                raise ErrorValidacion(f"Contraseña débil: {password}")

            insertar_texto(texto_reg_ok, f"✔ Usuario creado: {nombre} | {correo}")
        except Exception as e:
            insertar_texto(texto_reg_error, f"❌ Registro inválido | {nombre} | Motivo: {e}", "error")

        # ====================
        # CLIENTE
        # ====================
        try:
            cliente = Cliente(nombre, correo, navegador)
            insertar_texto(texto_exitos, f"🌐 Cliente: {nombre} | {correo} | {navegador}", "cliente")
        except Exception as e:
            insertar_texto(texto_errores, f"❌ Cliente inválido | {nombre} | {e}", "error")
            continue

        # ====================
        # SERVICIO
        # ====================
        tipo, precio = random.choice(servicios)

        try:
            if tipo == "Sala":
                servicio = Sala(tipo, precio)

            elif tipo == "Equipo":
                servicio = Equipo(tipo, precio)

            elif tipo == "Asesoria":
                servicio = Asesoria(tipo, precio)

            elif tipo == "ErrorPrecio":
                servicio = Sala(tipo, precio)

            elif tipo == "ErrorNombre":
                raise ErrorValidacion("Servicio no válido")

            elif tipo == "ErrorLogico":
                raise ErrorValidacion("Parámetros inconsistentes")

            else:
                servicio = Sala(tipo, precio)

            insertar_texto(texto_exitos, f"🛠 Servicio: {servicio.nombre}", "servicio")

        except Exception as e:
            insertar_texto(texto_errores, f"❌ Servicio inválido | {tipo} | {e}", "error")
            continue

        # ====================
        # RESERVA
        # ====================
        horas = random.randint(-2, 5)

        try:
            reserva = Reserva(cliente, servicio, horas)

            costo = reserva.servicio.calcular_costo(
                horas,
                descuento=random.randint(0, 10)
            )

        except ErrorValidacion as e:
            insertar_texto(
                texto_errores,
                f"❌ Error reserva | Cliente: {nombre} | Servicio: {servicio.nombre} | Motivo: {e}",
                "error"
            )

        else:
            insertar_texto(
                texto_exitos,
                f"✔ {nombre} | {servicio.nombre} | ${costo}",
                "reserva"
            )
            logging.info(f"Reserva exitosa: {nombre} - {servicio.nombre}")

        finally:
            logging.info("Proceso de reserva finalizado")


# ================================
# INTERFAZ VISUAL
# ================================
ventana = tk.Tk()
ventana.title("Sistema Software FJ")
ventana.geometry("1000x600")

frame = tk.Frame(ventana)
frame.pack()

# TÍTULOS
tk.Label(frame, text="✔ PROCESOS EXITOSOS", fg="green", font=("Arial", 10, "bold")).grid(row=0, column=0)
tk.Label(frame, text="❌ ERRORES DEL SISTEMA", fg="red", font=("Arial", 10, "bold")).grid(row=0, column=1)

tk.Label(frame, text="👤 REGISTROS EXITOSOS", fg="blue", font=("Arial", 10, "bold")).grid(row=2, column=0)
tk.Label(frame, text="⚠️ REGISTROS INVÁLIDOS", fg="red", font=("Arial", 10, "bold")).grid(row=2, column=1)

# CUADROS
texto_exitos = tk.Text(frame, width=45, height=15, state="disabled")
texto_exitos.grid(row=1, column=0)

texto_errores = tk.Text(frame, width=45, height=15, state="disabled")
texto_errores.grid(row=1, column=1)

texto_reg_ok = tk.Text(frame, width=45, height=10, state="disabled")
texto_reg_ok.grid(row=3, column=0)

texto_reg_error = tk.Text(frame, width=45, height=10, state="disabled")
texto_reg_error.grid(row=3, column=1)

# COLORES
texto_exitos.tag_config("cliente", foreground="blue")
texto_exitos.tag_config("servicio", foreground="purple")
texto_exitos.tag_config("reserva", foreground="green")
texto_errores.tag_config("error", foreground="red")
texto_reg_error.tag_config("error", foreground="red")

# BOTÓN
tk.Button(ventana, text="Ejecutar Simulación", command=ejecutar).pack(pady=10)

ventana.mainloop()