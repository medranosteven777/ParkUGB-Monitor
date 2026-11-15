"""Cálculos de ocupación: porcentajes por zona, totales y estado de lleno."""
from datos.config import AMARILLO, ROJO, VERDE, ZONA_ESPERA


def color_por_pct(pct):
    return ROJO if pct >= 90 else AMARILLO if pct >= 70 else VERDE


def resumen_zona(espacios, zona):
    espera = zona == ZONA_ESPERA
    sp = [e for e in espacios if e["zona"] == zona]
    base = sp if espera else [e for e in sp if e["tipo"] == "normal"]
    libres = sum(not e["ocupado"] for e in base)
    ocupados = len(base) - libres
    pct = round(ocupados / len(base) * 100)
    return {"espera": espera, "total": len(base), "libres": libres, "ocupados": ocupados,
            "pct": pct, "llena": libres == 0 and not espera}


def resumen_general(espacios):
    publicos = [e for e in espacios if e["tipo"] == "normal"]
    ocupados = sum(e["ocupado"] for e in publicos)
    libres_por_zona = {}
    for e in publicos:
        libres_por_zona[e["zona"]] = libres_por_zona.get(e["zona"], 0) + (not e["ocupado"])
    return {
        "total": len(publicos),
        "ocupados": ocupados,
        "libres": len(publicos) - ocupados,
        "pct": round(ocupados / len(publicos) * 100),
        "reservados_libres": sum(1 for e in espacios if e["tipo"] == "docente" and not e["ocupado"]),
        "espera_libres": sum(1 for e in espacios if e["tipo"] == "espera" and not e["ocupado"]),
        "libres_por_zona": libres_por_zona,
        "lleno": ocupados == len(publicos),
    }
