import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv(
    r'\Users\ylove\OneDrive\Escritorio\Tripleteen\VS Code\prueba_4\vehicles_us.csv')
st.title("Análisis de Datos de Vehículos")

if st.checkbox("Mostrar Histograma"):
    fig_hist = px.histogram(car_data, x="odometer")
    st.write("### Histograma del Odómetro")
    st.plotly_chart(fig_hist)

if st.checkbox("Mostrar Gráfico de Dispersión"):
    fig_scatter = px.scatter(
        car_data, x="odometer", y="price", title="Relación entre Kilometraje y Precio")
    st.write("### Gráfico de Dispersión: Odómetro vs Precio")
    st.plotly_chart(fig_scatter)
