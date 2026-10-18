import streamlit as st
import pandas as pd

@st.cache_data
def load_data(nrows=300):
    return pd.read_csv("https://raw.githubusercontent.com/Mikaelhunter/puchamon-/refs/heads/main/pokemon.csv",nrows=nrows,encoding="latin-1")

pkm_data = load_data()

st.header("Data Description")
st.dataframe(pkm_data)

if st.sidebar.checkbox("Mostrar todos los pokemon"):
    st.subheader("Todos los pokemon")
    st.write(f"Total pokemon: {len(pkm_data)}")
    st.dataframe(pkm_data)
