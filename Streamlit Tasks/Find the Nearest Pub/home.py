import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Home"
)

st.header("Open Pubs Database:")
df = pd.read_csv("modified_open_pubs.csv")

st.dataframe(df.head(21))

st.subheader('The total number of rows in the data are :') 
total = df.count()[0]
st.text(total)

agree = st.checkbox('Statistical Measures')
if agree:
     st.write(df.describe())





