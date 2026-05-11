# Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción
Sistema desarrollado en Python que permite gestionar clientes,
servicios y reservas mediante programación orientada a objetos.

El sistema implementa:
- Validaciones
- Manejo de excepciones
- Logging
- Simulación automática
- Arquitectura modular

## Integrantes
- Juan Sebastian Gonzalez Quiñones
- Sebastian Pacheco Chica
- Breiner Andres Herrera Vera

## Tecnologías usadas
- Python
- Tkinter
- GitHub

## Ejecución

```bash
python main.py
```

## Funcionalidades
- Registro de clientes
- Gestión de servicios
- Reservas automáticas
- Simulación de casos válidos e inválidos
- Registro de eventos mediante logging

# Guía de Funcionamiento

## 1. Ejecutar el sistema

Abrir la terminal en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

---

## 2. Inicio del sistema

Al ejecutar el archivo principal `main.py`, el sistema inicia automáticamente las simulaciones y procesos del programa.

---

## 3. Funcionalidades principales

El sistema permite:

- Registrar clientes
- Gestionar servicios
- Procesar reservas
- Validar datos ingresados
- Manejar errores mediante excepciones
- Registrar eventos y errores usando logging

---

## 4. Simulación automática

El sistema ejecuta automáticamente diferentes casos de prueba:

- Clientes válidos
- Clientes inválidos
- Servicios válidos
- Servicios inválidos
- Reservas exitosas
- Reservas fallidas
- Validaciones de datos
- Manejo de excepciones

---

## 5. Arquitectura modular

El proyecto está organizado en módulos:

- `cliente.py`
- `servicios.py`
- `reserva.py`
- `excepciones.py`
- `main.py`

Cada módulo cumple una función específica dentro del sistema.

---

## 6. Registro de eventos

El sistema genera registros automáticos mediante logging para almacenar:

- Eventos del sistema
- Reservas realizadas
- Errores detectados
- Validaciones fallidas

---

## 7. Interfaz gráfica

El sistema utiliza Tkinter para mostrar los resultados de simulaciones y procesos realizados.
