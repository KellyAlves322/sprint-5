import streamlit as st 
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('C:\\Users\\Administrador\\sprint-5\\vehicles.csv')

st.header('Dados')
st.write(car_data)

st.header('Gráficos')

hist_button = st.button('Criar histograma') # criar um botão
st.subheader('Gráficos')        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
build_scatter = st.checkbox('Criar um gráfico de dispersão (odometer vs price)')

if build_scatter:
    st.write('Criando um gráfico de dispersão entre "odometer" e "price"...')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)