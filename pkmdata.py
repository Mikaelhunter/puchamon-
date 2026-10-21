import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

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

def filtrar_por_stats(df, minimo, maximo):
    return df[(df["Base_Stat_Total"] >= minimo) & (df["Base_Stat_Total"] <= maximo)]

cal_min, cal_max = st.sidebar.slider("Stats totales:", 175, 1125, (175, 1125))
if st.sidebar.button("Buscar por stats totales"):
    resultado = filtrar_por_stats(pkm_data, cal_min, cal_max)
    st.subheader("Resultado de la búsqueda")
    st.write(f"Total de pokemon: {resultado.shape[0]}")
    st.dataframe(resultado)

def filtrar_por_juego(df, Games_of_Origin):
    return df[df["Games_of_Origin"] == Games_of_Origin]
Games_of_Origin = st.sidebar.selectbox(
    "Seleccionar juego de origen",
    sorted(pkm_data["Games_of_Origin"].dropna().unique())
)
if st.sidebar.button("Seleccionar juego de origen"):
  resultado = filtrar_por_juego(pkm_data, Games_of_Origin)
  st.subheader(f"Pokemon del juego {Games_of_Origin}")
  st.write(f"Total de pokemon:{resultado.shape[0]}" )
  st.dataframe(resultado)

fig, ax = plt.subplots()
ax.hist(pkm_data.Catch_Rate)
st.header("Cantidad de pokemon por ratio de captura")
st.pyplot(fig)

fig2, ax2 = plt.subplots()
y_pos = pkm_data['Primary_Type']
x_pos = pkm_data['Attack_Stat']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Tipo")
ax2.set_xlabel("stat de ataque")
ax2.set_title('Que tipo tiene en promedio mas ataque')
st.header("Grafica de Barras de pokemon")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
ax3.scatter(pkm_data.Base_Stat_Total, pkm_data.Primary_Type)
ax3.set_xlabel("tipo de crecimiento")
ax3.set_ylabel("stats totales")
st.header("Grafica de Dispersión")
st.pyplot(fig3)



st.title("Miguel Angel Vega Romero")
st.header("Matrícula: S26004660")
st.header("Mapa de mi localidad")

map_data = pd.DataFrame(
  np.random.randn(1, 2) / [1500, 1500] + [18.8950139, -97.0383833],
  columns=['lat', 'lon'])

st.title("Localidad de Buena Vista, Ixtac.")

st.map(map_data)