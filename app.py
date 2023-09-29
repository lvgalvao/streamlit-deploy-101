import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd

load_dotenv() # <- carrega as variáveis de ambiente do .env

DATE_COLUMN = 'date/time' 
DATA_URL = os.getenv('UBER_DATA_URL') # <- define a variável DATA_URL

@st.cache_data # <- define o cache para os dados
def load_data(nrows): # <- função para carregar os dados
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower() 
    data.rename(lowercase, axis='columns', inplace=True) 
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) 
    return data # <- retorna os dados

st.title('Uber corridas em NYC') # <- define o título do app
data_load_state = st.text('Loading data...')
data = load_data(10000) # <- carrega os dados
if st.checkbox('Mostra tabela'):
    st.subheader('Tabela de Raw data')
    st.dataframe(data) # <- mostra os dados em um dataframe
data_load_state.text('Testando o (using st.cache_data)"')

import numpy as np
st.subheader('Número de corridas por hora')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# setando o filtro de hora
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de todas as viagens até ás %s:00' % hour_to_filter)
st.map(filtered_data)