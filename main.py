# ============================================
# IMPORTACIÓN DE LIBRERÍAS Y MÓDULOS
# ============================================

# Librería para crear la interfaz gráfica
import tkinter as tk

# Librería para generar datos aleatorios
import random

# Librería para registrar eventos y errores
import logging

# Importar clase Cliente desde cliente.py
from cliente import Cliente

# Importar tipos de servicios desde servicios.py
from servicios import Sala, Equipo, Asesoria

# Importar clase Reserva desde reserva.py
from reserva import Reserva

# Importar excepción personalizada
from excepciones import ErrorValidacion


# ============================================
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# ============================================

# Crear archivo donde se guardarán errores y eventos
logging.basicConfig(

    # Nombre del archivo log
    filename="registro_sistema.log",

    # Nivel de información guardada
    level=logging.INFO,

    # Formato de los mensajes
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ============================================
# GENERADOR DE NOMBRES ALEATORIOS
# ============================================

def generar_nombre():

    # Lista de nombres
    nombres = [
        "Juan", "Ana", "Luis", "Camila",
        "Pedro", "Sofia", "Andres"
    ]

    # Lista de apellidos
    apellidos = [
        "Gomez", "Lopez", "Perez",
        "Torres", "Martinez"
    ]

    # Retornar nombre completo aleatorio
    return f"{random.choice(nombres)} {random.choice(apellidos)}"


# ============================================
# GENERADOR DE CORREOS
# ============================================

def generar_correo(nombre):

    # Dominios disponibles
    dominios = [
        "gmail.com",
        "hotmail.com",
        "outlook.com"
    ]

    # Convertir nombre a minúsculas
    base = nombre.lower().replace(" ", "")

    # Generar número aleatorio
    numero = random.randint(1, 999)

    # Crear correo dinámico
    return f"{base}{numero}@{random.choice(dominios)}"


# ============================================
# GENERADOR DE CONTRASEÑAS
# ============================================

def generar_password():

    # Contraseñas válidas e inválidas
    opciones = [
        "123",
        "abc",
        "segura123",
        "claveFuerte"
    ]

    # Elegir contraseña aleatoria
    return random.choice(opciones)


# ============================================
# GENERADOR DE NAVEGADORES
# ============================================

def generar_navegador():

    # Navegadores posibles
    return random.choice([
        "Chrome",
        "Firefox",
        "Edge",
        "Safari"
    ])


# ======================================================
# MOSTRAR RESULTADOS SIN QUE EL USUARIO PUEDA EDITARLOS
# ======================================================

def insertar_texto(widget, texto, tag=None):

    # Activar temporalmente el cuadro
    widget.config(state="normal")

    # Insertar texto
    widget.insert(tk.END, texto + "\n", tag)

    # Bloquear nuevamente el cuadro
    widget.config(state="disabled")


# ============================================
# FUNCIÓN PRINCIPAL DEL SISTEMA
# ============================================

def ejecutar():

    # Lista de servicios válidos e inválidos
    servicios = [
        ("Sala", 50),
        ("Equipo", 20),
        ("Asesoria", 100),
        ("ErrorPrecio", -5),
        ("ErrorNombre", 30),
        ("ErrorLogico", 40)
    ]

    # Simulación de múltiples usuarios
    for _ in range(8):

        # Generar datos dinámicos
        nombre = generar_nombre()
        correo = generar_correo(nombre)
        password = generar_password()
        navegador = generar_navegador()

        # ====================================
        # VALIDACIÓN DE REGISTRO
        # ====================================

        try:

            # Validar longitud de contraseña
            if len(password) < 5:
                raise ErrorValidacion(
                    f"Contraseña débil: {password}"
                )

            insertar_texto(
                texto_reg_ok,
                f"✔ Usuario creado: {nombre} | {correo}"
            )

        except Exception as e:

            insertar_texto(
                texto_reg_error,
                f"❌ Registro inválido | {nombre} | Motivo: {e}",
                "error"
            )

        # ====================================
        # CREACIÓN DE CLIENTE
        # ====================================

        try:

            cliente = Cliente(
                nombre,
                correo,
                navegador
            )

            insertar_texto(
                texto_exitos,
                f"🌐 Cliente: {nombre} | {correo} | {navegador}",
                "cliente"
            )

        except Exception as e:

            insertar_texto(
                texto_errores,
                f"❌ Cliente inválido | {nombre} | {e}",
                "error"
            )

            continue

        # ====================================
        # CREACIÓN DE SERVICIOS
        # ====================================

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
                raise ErrorValidacion(
                    "Servicio no válido"
                )

            elif tipo == "ErrorLogico":
                raise ErrorValidacion(
                    "Parámetros inconsistentes"
                )

            insertar_texto(
                texto_exitos,
                f"🛠 Servicio: {tipo}",
                "servicio"
            )

        except Exception as e:

            insertar_texto(
                texto_errores,
                f"❌ Servicio inválido | {tipo} | {e}",
                "error"
            )

            continue

        # ====================================
        # PROCESAMIENTO DE RESERVAS
        # ====================================

        horas = random.randint(-2, 5)

        try:

            reserva = Reserva(
                cliente,
                servicio,
                horas
            )

            costo = servicio.calcular_costo(
                horas,
                descuento=random.randint(0, 10)
            )

        except ErrorValidacion as e:

            insertar_texto(
                texto_errores,
                f"❌ Error reserva | Cliente: {nombre} | "
                f"Servicio: {tipo} | Motivo: {e}",
                "error"
            )

        else:

            insertar_texto(
                texto_exitos,
                f"✔ {nombre} | {tipo} | ${costo}",
                "reserva"
            )

            logging.info(
                f"Reserva exitosa: {nombre} - {tipo}"
            )

        finally:

            logging.info(
                "Proceso de reserva finalizado"
            )


# ============================================
# INTERFAZ DEL SISTEMA
# ============================================

# Crear ventana principal
ventana = tk.Tk()

# Título de la ventana
ventana.title("Sistema Software FJ")

# Tamaño de la ventana
ventana.geometry("1000x600")

# Crear frame principal
frame = tk.Frame(ventana)
frame.pack()

# ============================================
# TÍTULOS
# ============================================

tk.Label(
    frame,
    text="✔ PROCESOS EXITOSOS",
    fg="green",
    font=("Arial", 10, "bold")
).grid(row=0, column=0)

tk.Label(
    frame,
    text="❌ ERRORES DEL SISTEMA",
    fg="red",
    font=("Arial", 10, "bold")
).grid(row=0, column=1)

tk.Label(
    frame,
    text="👤 REGISTROS EXITOSOS",
    fg="blue",
    font=("Arial", 10, "bold")
).grid(row=2, column=0)

tk.Label(
    frame,
    text="⚠️ REGISTROS INVÁLIDOS",
    fg="red",
    font=("Arial", 10, "bold")
).grid(row=2, column=1)

# ============================================
# CUADROS DE TEXTO
# ============================================

texto_exitos = tk.Text(
    frame,
    width=45,
    height=15,
    state="disabled"
)

texto_exitos.grid(row=1, column=0)

texto_errores = tk.Text(
    frame,
    width=45,
    height=15,
    state="disabled"
)

texto_errores.grid(row=1, column=1)

texto_reg_ok = tk.Text(
    frame,
    width=45,
    height=10,
    state="disabled"
)

texto_reg_ok.grid(row=3, column=0)

texto_reg_error = tk.Text(
    frame,
    width=45,
    height=10,
    state="disabled"
)

texto_reg_error.grid(row=3, column=1)

# ============================================
# CONFIGURACIÓN DE COLORES
# ============================================

texto_exitos.tag_config(
    "cliente",
    foreground="blue"
)

texto_exitos.tag_config(
    "servicio",
    foreground="purple"
)

texto_exitos.tag_config(
    "reserva",
    foreground="green"
)

texto_errores.tag_config(
    "error",
    foreground="red"
)

texto_reg_error.tag_config(
    "error",
    foreground="red"
)

# ============================================
# EJECUCIÓN AUTOMÁTICA DEL SISTEMA
# ============================================

def ejecutar_automatico():

    # Ejecutar simulación
    ejecutar()

    # Repetir simulación cada 2 segundos
    ventana.after(2000, ejecutar_automatico)


# Iniciar simulación automática
ejecutar_automatico()


# ============================================
# MANTENER VENTANA ABIERTA
# ============================================

ventana.mainloop()