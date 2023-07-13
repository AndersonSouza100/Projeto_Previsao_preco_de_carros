#!/usr/bin/env python
# coding: utf-8

# ### Organizando os nomes das colunas

# In[1]:


import pandas as pd
import streamlit as st
import joblib


# In[2]:


colunas = ['Ano',
'Motor HP',
'Nº de Cilindros',
'Nº de Portas',
'KM/L Estrada',
'KM/L Cidade',
'Preço Sugerido Fabricante',
'Fabricante_Acura',
'Fabricante_Audi',
'Fabricante_BMW',
'Fabricante_Buick',
'Fabricante_Cadillac',
'Fabricante_Chevrolet',
'Fabricante_Chrysler',
'Fabricante_Dodge',
'Fabricante_Ford',
'Fabricante_GMC',
'Fabricante_Honda',
'Fabricante_Hyundai',
'Fabricante_Infiniti',
'Fabricante_Kia',
'Fabricante_Lexus',
'Fabricante_Lincoln',
'Fabricante_Mazda',
'Fabricante_Mercedes-Benz',
'Fabricante_Mitsubishi',
'Fabricante_Nissan',
'Fabricante_Oldsmobile',
'Fabricante_Outros',
'Fabricante_Pontiac',
'Fabricante_Saab',
'Fabricante_Subaru',
'Fabricante_Suzuki',
'Fabricante_Toyota',
'Fabricante_Volkswagen',
'Fabricante_Volvo',
'Tipo de Combustivel_Flex',
'Tipo de Combustivel_Gas Natural',
'Tipo de Combustivel_Gasolina',
'Tipo de Combustivel_diesel',
'Tipo Transmissão_Automático',
'Tipo Transmissão_Automático e Manual',
'Tipo Transmissão_MANUAL',
'Tração_tracao dianteira',
'Tração_tracao em 4 rodas',
'Tração_tracao traseira',
'Tamanho Veículo_Grande',
'Tamanho Veículo_Medio',
'Tamanho Veículo_Pequeno',
'Estilo Veículo_Conversível',
'Estilo Veículo_Cupê',
'Estilo Veículo_Hatchback de 2 portas',
'Estilo Veículo_Hatchback de 4 portas',
'Estilo Veículo_Minivan de Passageiros',
'Estilo Veículo_Outros',
'Estilo Veículo_Perua',
'Estilo Veículo_Picape Cabine Dupla',
'Estilo Veículo_Picape Cabine Estendida',
'Estilo Veículo_Picape Cabine Simples',
'Estilo Veículo_SUV de 4 portas',
'Estilo Veículo_Sedã',]


x_listas = {}
x_numericos = {}

for item in colunas:
    if 'Fabricante' in item:
        x_listas.setdefault('Fabricante', []).append(item.replace('Fabricante_', ''))
    elif 'Tipo de Combustivel' in item:
        x_listas.setdefault('Tipo de Combustivel', []).append(item.replace('Tipo de Combustivel_', ''))
    elif 'Tipo Transmissão' in item:
        x_listas.setdefault('Tipo Transmissão', []).append(item.replace('Tipo Transmissão_', ''))  
    elif 'Tração' in item:
        x_listas.setdefault('Tração', []).append(item.replace('Tração_', ''))   
    elif 'Tamanho Veículo' in item:
        x_listas.setdefault('Tamanho Veículo', []).append(item.replace('Tamanho Veículo_', ''))
    elif 'Estilo Veículo' in item:
        x_listas.setdefault('Estilo Veículo', []).append(item.replace('Estilo Veículo_', ''))
    else:
        x_numericos[item] = 0
del x_listas['Fabricante'][0]
print(x_listas)
print('--'* 20)
print(x_numericos)


# In[3]:


dicionario = {} # criou um dicionario vazio para editar as variaveis dummies de x_listas
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0 # usou o for para concatenar o nome de cada item de x_listas com o valor de cada item

for item in x_numericos:
    valor = st.number_input(f'{item}', step=1, value=0)
    x_numericos[item] = valor
    
for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[item])
    dicionario[f'{item}_{valor}'] = 1
    
botao = st.button('Prever valor do carro')

if botao:
    dicionario.update(x_numericos)
    valores_x = pd.DataFrame(dicionario, index=[0]) 
    dados = pd.read_csv('dados.csv') 
    colunas = list(dados.columns)[1:-1]
    valores_x = valores_x[colunas]
    modelo = joblib.load('modelo.joblib')
    preco = modelo.predict(valores_x) 
    st.write(preco[0])



    
    
    


# In[ ]:




