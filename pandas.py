import streamlit as st
import pandas as pd
import numpy as np

st.title('Número de corridas Uber em NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Baixando os dados...')
data = load_data(10000)
data_load_state.text("Pronto! (usamos o st.cache_data)")

if st.checkbox('Mostrando o raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Número de viagens por hora')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Alguns números aleatórios
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa com todas as corridas ás %s:00' % hour_to_filter)
st.map(filtered_data)