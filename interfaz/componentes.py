"""Componentes visuales: cada función devuelve un bloque de HTML."""
from datos.config import AMARILLO, AZUL, ROJO, VERDE, ZONAS
from logica.ocupacion import color_por_pct, resumen_general, resumen_zona


def html_topbar(hora):
    return ('<div class="topbar"><div class="brand"><div class="logo">P<i></i></div><div>'
            '<h1>ParkUGB Monitor 2.0</h1><span>Universidad Gerardo Barrios · Monitoreo de parqueos</span></div></div>'
            f'<div class="live"><b>●</b>EN VIVO · {hora}</div></div>')


def html_slot(e):
    if e["tipo"] == "espera":
        clase, icono = ("s-ocupado", "🚗") if e["ocupado"] else ("s-espera", "P")
    elif e["tipo"] == "docente":
        clase, icono = ("s-reservado-ocupado", "🚗") if e["ocupado"] else ("s-reservado", "DOC")
    else:
        clase, icono = ("s-ocupado", "🚗") if e["ocupado"] else ("s-libre", "P")
    return f'<div class="slot {clase}" title="{e["id"]}"><span>{icono}</span>{e["id"][1:]}</div>'


def html_zona(espacios, zona):
    r = resumen_zona(espacios, zona)
    color = color_por_pct(r["pct"])
    texto = "LLENA" if r["llena"] else f'{r["libres"]} libres'
    slots = "".join(html_slot(e) for e in espacios if e["zona"] == zona)
    return (f'<div class="zona"><div class="zhead"><strong>Zona {"de espera" if r["espera"] else zona} · {ZONAS[zona][0]}</strong>'
            f'<div class="pct" style="color:{color}">{r["pct"]}%</div></div>'
            f'<div class="zsub"><span class="badge" style="background:{color}">{texto}</span>'
            f'{r["ocupados"]} de {r["total"]} espacios ocupados</div>'
            f'<div class="bar"><div style="width:{r["pct"]}%;background:{color}"></div></div>'
            f'<div class="slots">{slots}</div></div>')


def html_kpis(espacios):
    g = resumen_general(espacios)
    color = color_por_pct(g["pct"])
    barra = f'<div class="bar"><div style="width:{g["pct"]}%;background:{color}"></div></div>'
    tarjetas = [
        (VERDE, "Disponibles", g["libres"], "espacios públicos libres", ""),
        (ROJO, "Ocupados", g["ocupados"], f'de {g["total"]} espacios públicos', ""),
        (AZUL, "Reservados", g["reservados_libres"], "espacios de docentes libres", ""),
        (color, "Ocupación", f'{g["pct"]}%', "", barra),
    ]
    return '<div class="kpis">' + "".join(
        f'<div class="kpi" style="--c:{c}"><small>{t}</small><b>{v}</b><em>{d}</em>{b}</div>' for c, t, v, d, b in tarjetas
    ) + "</div>"


def html_banner(espacios):
    g = resumen_general(espacios)
    if g["lleno"]:
        espera = g["espera_libres"]
        destino = (f"dirigir los vehículos a la zona de espera ({espera} lugares libres)" if espera
                   else "pedir a los conductores esperar en la calle de acceso")
        return f'<div class="banner full">🚨 PARQUEO LLENO · Avisar a los vigilantes de la entrada y {destino}.</div>'
    mejores = ", ".join(f"Zona {z} ({n})" for z, n in sorted(g["libres_por_zona"].items(), key=lambda x: -x[1]) if n)
    return f'<div class="banner ok">✅ Hay espacios disponibles · Dirigir a: {mejores}</div>'


def html_leyenda():
    return ('<div class="leyenda">'
            f'<span><i style="border-color:{VERDE};background:rgba(25,230,160,.15)"></i>Libre</span>'
            f'<span><i style="border-color:{ROJO};background:rgba(255,77,109,.25)"></i>Ocupado</span>'
            f'<span><i style="border-color:{AZUL};background:rgba(77,141,255,.2)"></i>Reservado docente</span>'
            f'<span><i style="border-color:{AMARILLO};background:rgba(255,194,77,.15)"></i>Zona de espera</span></div>')
