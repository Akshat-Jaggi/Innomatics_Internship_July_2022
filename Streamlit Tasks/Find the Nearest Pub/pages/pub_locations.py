import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Pub Locations"
)

df = pd.read_csv("..\Find the Nearest Pub\modified_open_pubs.csv")

st.header("Top Pubs in your Area")
st.subheader("Select the Local Authority to look at the Pubs associated with it.")

local_auth = st.selectbox('The local authority of the area which you want to search', set(df['local_authority']))
button_1 = st.button("Submit Local Authority")

if button_1:
    df_new = df[df["local_authority"] == local_auth]
    st.text("Top Pubs in this region are:")
    st.dataframe(df_new)
    st.map(df_new)