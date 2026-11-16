# ParkUGB Monitor 2.0

## Integrantes
| Nombre | Carnet |
|---|---|
| Melvin Lizandro Castro Sorto | SMSS018725 |
| Luis Jeovanny Majano Rivera | SMSS025725 |
| Steven Moises Medrano Arbaiza | SMSS025425 |
| William Edgardo Vasquez Lopez | SMSS020525 |

## Descripción
ParkUGB Monitor 2.0 es una aplicación web de monitoreo en tiempo real de los parqueos de la Universidad Gerardo Barrios.
Resuelve el problema de los conductores que recorren todo el campus buscando un espacio y descubren que el parqueo ya está lleno.

El sistema:
- Muestra el estado de cada espacio (libre, ocupado o reservado para docentes) por zona.
- Calcula el porcentaje de ocupación de cada zona y del parqueo completo, actualizado cada 2 segundos.
- Alerta a los vigilantes cuando el parqueo se llena y recomienda una zona de espera.
- Reserva espacios para docentes (la asignación del espacio más cercano al aula llegará en la Entrega 2).

En esta primera etapa los datos de ocupación son simulados.

## Instalación y ejecución

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Se abre el navegador en `http://localhost:8501`. Para detener la app, presione `Ctrl + C`.
Importante: la app se ejecuta con `streamlit run app.py`, no con el botón de ejecutar de VS Code.

## Tecnologías
Python 3, Streamlit (interfaz web) y Git/GitHub (control de versiones).
