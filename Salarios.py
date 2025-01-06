import streamlit as st
import pandas as pd

# Cargar datos desde Google Sheets
url = 'https://docs.google.com/spreadsheets/d/10-VD4DD5vBUJGevk_aF7sZcpHVxZk6EUk19jzuX1-1I/export?format=csv'
df = pd.read_csv(url)

# Título de la aplicación
st.title('📊 Análisis de Salarios de Desarrolladores en Cuba')

# Sidebar para botones
st.sidebar.header("📈 Opciones de Análisis")

def estilo_tabla(dataframe):
    return dataframe.style.set_properties(**{'font-weight': 'bold', 'text-align': 'center', 'background-color': '#f0f0f0'})

if st.sidebar.button("Mostrar Datos"):
    st.write("### 📋 Datos de Desarrolladores")
    st.write(estilo_tabla(df))

if st.sidebar.button("Mostrar Promedio por Posición"):
    promedio_posicion = df.groupby('Posición')['Salario Mensual (En USD)'].mean().reset_index()
    st.write("### 💼 Promedio de Salarios por Posición")
    st.write(estilo_tabla(promedio_posicion))
    st.bar_chart(promedio_posicion.set_index('Posición'))

if st.sidebar.button("Mostrar Promedio por Seniority"):
    promedio_puesto = df.groupby('Seniority')['Salario Mensual (En USD)'].mean().reset_index()
    st.write("### 📈 Promedio de Salarios por Seniority")
    st.write(estilo_tabla(promedio_puesto))
    st.bar_chart(promedio_puesto.set_index('Seniority'))

if st.sidebar.button("Mostrar Salarios Máximo y Mínimo"):
    max_salario = df.loc[df['Salario Mensual (En USD)'].idxmax()]
    min_salario = df.loc[df['Salario Mensual (En USD)'].idxmin()]
    st.write("### 💰 Lo Más Pagado")
    st.write(estilo_tabla(pd.DataFrame(max_salario).T))
    st.write("### 💸 Lo Menos Pagado")
    st.write(estilo_tabla(pd.DataFrame(min_salario).T))

if st.sidebar.button("Mostrar Promedios de Experiencia"):
    promedio_experiencia_industria = df['Años de experiencia en la industria'].mean()
    promedio_experiencia_puesto = df['Años de experiencia en el puesto actual'].mean()
    st.write(f"### 📊 Promedio de Años de Experiencia en la Industria: **{promedio_experiencia_industria:.2f}**")
    st.write(f"### 📊 Promedio de Años de Experiencia en el Seniority Actual: **{promedio_experiencia_puesto:.2f}**")

if st.sidebar.button("Mostrar Promedio de Salario por Residencia"):
    promedio_salario_residente = df[df['Residente en Cuba'] == 'Si']['Salario Mensual (En USD)'].mean()
    promedio_salario_no_residente = df[df['Residente en Cuba'] == 'No']['Salario Mensual (En USD)'].mean()
    st.write(f"### 🏡 Promedio de Salario (Residente): **{promedio_salario_residente:.2f} USD**")
    st.write(f"### 🏝️ Promedio de Salario (No Residente): **{promedio_salario_no_residente:.2f} USD**")

if st.sidebar.button("Mostrar Gráficos para Residentes"):
    if 'Si' in df['Residente en Cuba'].values:
        promedio_salario_posicion_residente = df[df['Residente en Cuba'] == 'Si'].groupby('Posición')['Salario Mensual (En USD)'].mean().reset_index()
        promedio_salario_puesto_residente = df[df['Residente en Cuba'] == 'Si'].groupby('Seniority')['Salario Mensual (En USD)'].mean().reset_index()
        
        st.header("🏡 Promedio de Salarios por Posición (Residentes)")
        st.write(estilo_tabla(promedio_salario_posicion_residente))
        st.bar_chart(promedio_salario_posicion_residente.set_index('Posición'))
        
        st.header("🏡 Promedio de Salarios por Seniority (Residentes)")
        st.write(estilo_tabla(promedio_salario_puesto_residente))
        st.bar_chart(promedio_salario_puesto_residente.set_index('Seniority'))
    else:
        st.write("No hay datos disponibles para residentes.")
