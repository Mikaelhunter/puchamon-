import streamlit as st
import pandas as pd

@st.cache_data
def load_data(nrows=1383):
    return pd.read_csv("https://raw.githubusercontent.com/Mikaelhunter/puchamon-/refs/heads/main/Pokemon%20Database.csv",nrows=nrows,encoding="latin-1")

pkm_data = load_data()

st.header("Data Description")
st.dataframe(pkm_data)

if st.sidebar.checkbox("Mostrar todos los pokemon"):
    st.subheader("Todos los pokemon")
    st.write(f"Total pokemon: {len(pkm_data)}")
    st.dataframe(pkm_data)

def filtrar_por_nombre(df, texto):
    return df[df["Pokemon_Name"].str.contains(texto, case=False, na=False, regex=False)]
titulo = st.sidebar.text_input("Nombre del pokemon:")
if st.sidebar.button("Buscar pokemon"):
    resultado = filtrar_por_nombre(pkm_data, titulo)
    st.subheader("Resultado de la busqueda")
    st.write(f"Encontrados:,{resultado.shape[0]}")
    st.dataframe(resultado)

def filtrar_por_tipo(df, Primary_Type):
    return df[df["Primary_Type"] == Primary_Type]
Primary_Type = st.sidebar.selectbox(
    "Seleccionar tipo primario",
    sorted(pkm_data["Primary_Type"].dropna().unique())
)
if st.sidebar.button("Seleccionar tipo primario"):
  resultado = filtrar_por_tipo(pkm_data, Primary_Type)
  st.subheader(f"Pokemon del tipo {Primary_Type}")
  st.write(f"Total de pokemon:{resultado.shape[0]}" )
  st.dataframe(resultado)

