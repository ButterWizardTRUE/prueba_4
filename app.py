import os
import streamlit as st
import pandas as pd
import plotly.express as px

# Obtiene la ruta del archivo en el mismo directorio que app.py
file_path = os.path.join(os.path.dirname(__file__), "vehicles_us.csv")

# Cargar los datos
car_data = pd.read_csv(file_path, encoding="utf-8")

st.title("Análisis de Datos de Vehículos")

# Histograma del odómetro
if st.checkbox("Mostrar Histograma"):
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Histograma del Odómetro")
    st.plotly_chart(fig_hist)

# Gráfico de dispersión: odómetro vs precio
if st.checkbox("Mostrar Gráfico de Dispersión"):
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Relación entre Kilometraje y Precio")
    st.plotly_chart(fig_scatter)
