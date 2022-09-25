"""

streamlit run st_run.py --server.enableCORS=false
"""

import streamlit as st
import pandas as pd
from dblib.load_pops import load_pop, pandas_country_pop

st.title('World Population Interactive Dashboard')

st.header('Dataset Preview:')
dataframe = load_pop()
st.table(dataframe.head())

st.header('Plot a Country\'s Population Over Time')
st.write("Select a country")
country = st.selectbox("Country", dataframe['Country'].unique())
st.write("You selected:", country)
data = pandas_country_pop(countries=country)
dates = ['1970', '1980', '1990', '2000',
        '2010', '2015', '2020', '2022']

df = pd.DataFrame({
  'date': dates,
  'values': data.values()
})
df = df.rename(columns={'date':'index'}).set_index('index')
st.line_chart(df)
