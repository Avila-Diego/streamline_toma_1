# %% Importación de librerías
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% Título de la aplicación
st.title("Introducción a Streamlit No. 1")

# Sección 1: Texto y entrada de datos
st.header("1. Entrada de datos nuevos.")
st.write("Podemos pedir información al usuario usando widgets.")

# Entrada de texto
nombre = st.text_input("¿Cuál es tu nombre?", "Diego")
st.write(f"Hola, {nombre}!")

# Slider de número
edad = st.slider("¿Cuál es tu edad?", 0, 100, 25)
st.write(f"Tienes {edad} años.")
anio_actual = pd.Timestamp.now().year
anio_nacimiento = anio_actual - edad
st.write(f"Naciste en el año {anio_nacimiento}.")

# Sección 2: Gráficas y visualización
st.header("2. Visualización de datos")
st.write("Veamos un gráfico de datos generados aleatoriamente.")

# Generar datos aleatorios
datos = np.random.randn(100)

# Crear y mostrar gráfico de matplotlib
fig, ax = plt.subplots()
ax.hist(datos, bins=15, color='skyblue', edgecolor='black')
st.pyplot(fig)

# Sección 3: Carga de datos y visualización en tabla
st.header("3. Carga y visualización de datos")
st.write("Podemos cargar un dataset y mostrarlo en una tabla.")

# %% Cargar datos de ejemplo
data_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
data = pd.read_csv(data_url)
data = data[["Month"]]

# %%
st.write("Datos de muestra de viajes aéreos:")
st.dataframe(data)

# Sección 4: Gráfico de línea interactivo
st.header("4. Gráfico interactivo")
st.write("Puedes seleccionar un rango de datos y ver el resultado.")

# Simular datos de ventas mensuales de enero-2020 a agosto-2024
np.random.seed(0)
fechas = pd.date_range(start="2020-01-01", end="2024-08-01", freq="M")
fechas_formateadas = fechas.strftime("%b-%Y")
data = pd.DataFrame({
    "Mes": fechas_formateadas,
    "Valor de ventas": np.random.randint(100, 1000, size=len(fechas))
})

# Crear selección de rango
mes_inicio, mes_fin = st.select_slider(
    "Selecciona el rango de fechas",
    options=fechas_formateadas,
    value=(fechas_formateadas.min(), fechas_formateadas.max())
)

# Convertir los valores seleccionados a índices
mes_inicio_idx = np.where(fechas_formateadas == mes_inicio)[0][0]
mes_fin_idx = np.where(fechas_formateadas == mes_fin)[0][0]

# Filtrar datos por rango de meses
data_filtrada = data.iloc[mes_inicio_idx:mes_fin_idx+1]
st.line_chart(data_filtrada.set_index("Mes"))

# Sección 5: Checkbox y botón
st.header("5. Opciones adicionales")
if st.checkbox("Mostrar datos tabulados de ventas"):
    st.write("Datos tabulados de ventas:")
    data_pivot = data_filtrada.copy()
    data_pivot['Año'] = pd.to_datetime(data_pivot['Mes'], format='%b-%Y').dt.year
    data_pivot['Mes'] = pd.to_datetime(data_pivot['Mes'], format='%b-%Y').dt.month
    data_pivot = data_pivot.pivot(index='Mes', columns='Año', values='Valor de ventas')
    st.dataframe(data_pivot)

# Botón para refrescar la aplicación
if st.button("Refrescar"):
    st.rerun()


