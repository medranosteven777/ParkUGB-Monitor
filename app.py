"""ParkUGB Monitor 2.0 · punto de entrada. Ejecutar con: streamlit run app.py"""
from datetime import datetime

import streamlit as st

st.set_page_config(page_title="ParkUGB Monitor 2.0", page_icon="🅿️", layout="wide")

from datos.config import ESCENARIOS, ZONA_ESPERA, ZONAS
from fuente_datos.simulador import crear_espacios, simular_paso
from interfaz.componentes import html_banner, html_kpis, html_leyenda, html_topbar, html_zona
from interfaz.estilos import CSS


def panel(escenario, simular):
    espacios = st.session_state["espacios"]
    if simular:
        simular_paso(espacios, ESCENARIOS[escenario])
    st.markdown(html_topbar(datetime.now().strftime("%H:%M:%S")), unsafe_allow_html=True)
    st.markdown(html_kpis(espacios) + html_banner(espacios), unsafe_allow_html=True)

    zonas_normales = [z for z in ZONAS if z != ZONA_ESPERA]
    for i in range(0, len(zonas_normales), 2):
        columnas = st.columns(2)
        for col, z in zip(columnas, zonas_normales[i:i + 2]):
            col.markdown(html_zona(espacios, z), unsafe_allow_html=True)
    st.markdown(html_zona(espacios, ZONA_ESPERA), unsafe_allow_html=True)
    st.markdown(html_leyenda(), unsafe_allow_html=True)


def main():
    st.markdown(CSS, unsafe_allow_html=True)
    if "espacios" not in st.session_state:
        st.session_state["espacios"] = crear_espacios()
    st.sidebar.header("Controles")
    simular = st.sidebar.toggle("Simulación de sensores", value=True)
    escenario = st.sidebar.selectbox("Escenario", list(ESCENARIOS))
    if st.sidebar.button("Reiniciar espacios"):
        st.session_state["espacios"] = crear_espacios()
    st.sidebar.caption("Los datos son simulados y aún no se guardan.")
    st.fragment(run_every="2s" if simular else None)(panel)(escenario, simular)


main()
