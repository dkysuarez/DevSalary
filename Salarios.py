import streamlit as st
import pandas as pd

# Cargar datos
df = pd.read_excel('Encuestas de sueldos 2025 (respuestas).xlsx')

# Título de la aplicación
st.title('Análisis de Salarios de Desarrolladores en Cuba')

# Sidebar para botones
st.sidebar.header("Opciones de Análisis")

if st.sidebar.button("Mostrar Datos"):
    st.write("### Datos de Desarrolladores")
    st.write(df)

if st.sidebar.button("Mostrar Promedio por Posición"):
    promedio_posicion = df.groupby('Posición')['Salario Mensual (En USD)'].mean()
    st.write("### Promedio de Salarios por Posición")
    st.bar_chart(promedio_posicion)

if st.sidebar.button("Mostrar Promedio por Puesto"):
    promedio_puesto = df.groupby('Puesto')['Salario Mensual (En USD)'].mean()
    st.write("### Promedio de Salarios por Puesto")
    st.bar_chart(promedio_puesto)

if st.sidebar.button("Mostrar Salarios Máximo y Mínimo"):
    max_salario = df.loc[df['Salario Mensual (En USD)'].idxmax()]
    min_salario = df.loc[df['Salario Mensual (En USD)'].idxmin()]
    st.write("### Lo Más Pagado")
    st.write(max_salario)
    st.write("### Lo Menos Pagado")
    st.write(min_salario)

if st.sidebar.button("Mostrar Promedios de Experiencia"):
    promedio_experiencia_industria = df['Años de experiencia en la industria'].mean()
    promedio_experiencia_puesto = df['Años de experiencia en el puesto actual'].mean()
    st.write(f"### Promedio de Años de Experiencia en la Industria: {promedio_experiencia_industria:.2f}")
    st.write(f"### Promedio de Años de Experiencia en el Puesto Actual: {promedio_experiencia_puesto:.2f}")

if st.sidebar.button("Mostrar Promedio de Salario por Residencia"):
    promedio_salario_residente = df[df['Residente en Cuba'] == 'Si']['Salario Mensual (En USD)'].mean()
    promedio_salario_no_residente = df[df['Residente en Cuba'] == 'No']['Salario Mensual (En USD)'].mean()
    st.write(f"### Promedio de Salario (Residente): {promedio_salario_residente:.2f} USD")
    st.write(f"### Promedio de Salario (No Residente): {promedio_salario_no_residente:.2f} USD")

if st.sidebar.button("Mostrar Gráficos para Residentes"):
    if 'Si' in df['Residente en Cuba'].values:
        promedio_salario_posicion_residente = df[df['Residente en Cuba'] == 'Si'].groupby('Posición')['Salario Mensual (En USD)'].mean()
        promedio_salario_puesto_residente = df[df['Residente en Cuba'] == 'Si'].groupby('Puesto')['Salario Mensual (En USD)'].mean()
        
        st.header("Promedio de Salarios por Posición (Residentes)")
        st.bar_chart(promedio_salario_posicion_residente)
        
        st.header("Promedio de Salarios por Puesto (Residentes)")
        st.bar_chart(promedio_salario_puesto_residente)
    else:
        st.write("No hay datos disponibles para residentes.")

