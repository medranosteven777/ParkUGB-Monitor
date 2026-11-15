"""Simulador de sensores: genera y cambia el estado de los espacios."""
import random

from datos.config import ZONAS, ZONA_ESPERA


def crear_espacios():
    espacios = []
    for zona, (_, total, docentes) in ZONAS.items():
        for i in range(1, total + 1):
            tipo = "espera" if zona == ZONA_ESPERA else "docente" if i <= docentes else "normal"
            prob = {"normal": 0.55, "docente": 0.3, "espera": 0.25}[tipo]
            espacios.append({"id": f"{zona}{i:03d}", "zona": zona, "tipo": tipo, "ocupado": random.random() < prob})
    return espacios


def simular_paso(espacios, prob_llenar, cambios=5):
    publicos = [e for e in espacios if e["tipo"] == "normal"]
    for _ in range(cambios):
        llenar = random.random() < prob_llenar
        candidatos = [e for e in publicos if e["ocupado"] != llenar]
        if candidatos:
            random.choice(candidatos)["ocupado"] = llenar
