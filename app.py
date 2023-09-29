import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd

load_dotenv()

st.title('Número de corridas UBER em NYC')

DATE_COLUMN = 'date/time'
DATA_URL = os.getenv('UBER_DATA_URL')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Carregando os dados dados...')
data = load_data(10000)
data
data_load_state.text("Dados carregados, novamente...")
data_load_state.text("Done! (using st.cache_data)")