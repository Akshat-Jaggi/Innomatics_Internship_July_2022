import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Nearest Neighbours"
)

df = pd.read_csv("..\Find the Nearest Pub\modified_open_pubs.csv")

st.header("Nearest Neighbours According to the Entered Latitude and Longitude")

latitude = st.number_input('Insert the latitude')
longitude1 = st.number_input("Insert the Longitude")

df_new = df[["latitude","longitude"]]
input_points = np.array([latitude,longitude1])

distances = np.sqrt(np.sum((input_points - df_new)**2, axis = 1))

num = 5

min_indices = np.argpartition(distances,num-1)[:num]

st.text("The location corresponsing to below minimum distances : ")
st.dataframe(df.iloc[min_indices])
st.text("The minimum distances are:")
st.dataframe(distances.head(5))
st.text("Locations on map:")
st.map(df.iloc[min_indices])
