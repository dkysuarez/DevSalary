import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde Google Sheets
url = 'https://docs.google.com/spreadsheets/d/10-VD4DD5vBUJGevk_aF7sZcpHVxZk6EUk19jzuX1-1I/export?format=csv'
df = pd.read_csv(url)

# Título de la aplicación
st.title('📊 Análisis de Salarios de Desarrolladores en Cuba')

# Sidebar para botones
st.sidebar.header("📈 Opciones de Análisis")

# Función para graficar con estilo
def graficar(datos, titulo, xlabel, ylabel):
    fig, ax = plt.subplots()
    datos.plot(kind='bar', ax=ax)
    ax.set_title(titulo, fontsize=18, weight='bold')
    ax.set_xlabel(xlabel, fontsize=14, weight='bold')
    ax.set_ylabel(ylabel, fontsize=14, weight='bold')
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    st.pyplot(fig)

if st.sidebar.button("Mostrar Datos"):
    st.write("### 📋 Datos de Desarrolladores")
    st.write(df)

if st.sidebar.button("Mostrar Promedio por Posición"):
    promedio_posicion = df.groupby('Posición')['Salario Mensual (En USD)'].mean()
    st.write("### 💼 Promedio de Salarios por Posición")
    graficar(promedio_posicion, 'Promedio de Salarios por Posición', 'Posición', 'Salario Mensual (USD)')

if st.sidebar.button("Mostrar Promedio por Seniority"):
    promedio_puesto = df.groupby('Seniority')['Salario Mensual (En USD)'].mean()
    st.write("### 📈 Promedio de Salarios por Seniority")
    graficar(promedio_puesto, 'Promedio de Salarios por Seniority', 'Seniority', 'Salario Mensual (USD)')

if st.sidebar.button("Mostrar Salarios Máximo y Mínimo"):
    max_salario = df.loc[df['Salario Mensual (En USD)'].idxmax()]
    min_salario = df.loc[df['Salario Mensual (En USD)'].idxmin()]
    st.write("### 💰 Lo Más Pagado")
    st.write(max_salario)
    st.write("### 💸 Lo Menos Pagado")
    st.write(min_salario)

if st.sidebar.button("Mostrar Promedios de Experiencia"):
    promedio_experiencia_industria = df['Años de experiencia en la industria'].mean()
    promedio_experiencia_puesto = df['Años de experiencia en el puesto actual'].mean()
    st.write(f"### 📊 Promedio de Años de Experiencia en la Industria: {promedio_experiencia_industria:.2f}")
    st.write(f"### 📊 Promedio de Años de Experiencia en el Seniority Actual: {promedio_experiencia_puesto:.2f}")

if st.sidebar.button("Mostrar Promedio de Salario por Residencia"):
    promedio_salario_residente = df[df['Residente en Cuba'] == 'Si']['Salario Mensual (En USD)'].mean()
    promedio_salario_no_residente = df[df['Residente en Cuba'] == 'No']['Salario Mensual (En USD)'].mean()
    st.write(f"### 🏡 Promedio de Salario (Residente): {promedio_salario_residente:.2f} USD")
    st.write(f"### 🏝️ Promedio de Salario (No Residente): {promedio_salario_no_residente:.2f} USD")

if st.sidebar.button("Mostrar Gráficos para Residentes"):
    if 'Si' in df['Residente en Cuba'].values:
        promedio_salario_posicion_residente = df[df['Residente en Cuba'] == 'Si'].groupby('Posición')['Salario Mensual (En USD)'].mean()
        promedio_salario_puesto_residente = df[df['Residente en Cuba'] == 'Si'].groupby('Seniority')['Salario Mensual (En USD)'].mean()
        
        st.header("🏡 Promedio de Salarios por Posición (Residentes)")
        graficar(promedio_salario_posicion_residente, 'Promedio de Salarios por Posición (Residentes)', 'Posición', 'Salario Mensual (USD)')
        
        st.header("🏡 Promedio de Salarios por Seniority (Residentes)")
        graficar(promedio_salario_puesto_residente, 'Promedio de Salarios por Seniority (Residentes)', 'Seniority', 'Salario Mensual (USD)')
    else:
        st.write("No hay datos disponibles para residentes.")
