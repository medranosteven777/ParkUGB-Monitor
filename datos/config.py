"""Configuración general: zonas, escenarios y colores."""

# zona: (nombre, total de espacios, reservados para docentes)
ZONAS = {
    "A": ("Auditorio", 40, 10),
    "B": ("Edificio Hugo Lindo", 40, 15),
    "C": ("Edificio Gerardo Barrios", 150, 10),
    "D": ("Edificio de enfermeria", 90, 10),
    "E": ("Zona de espera (cancha)", 40, 0),
}
ZONA_ESPERA = "E"

# probabilidad de que el simulador ocupe un espacio en cada escenario
ESCENARIOS = {"Flujo normal": 0.5, "Hora pico": 0.8, "Salida": 0.2}

VERDE, ROJO, AMARILLO, AZUL = "#10c98a", "#f2406a", "#f5a60a", "#3b82f6"