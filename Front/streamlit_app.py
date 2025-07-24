######################### libreries #########################
import streamlit as st
from streamlit.components.v1 import html
from streamlit_folium import folium_static

import pandas as pd
import numpy as np

import folium
import json
import topojson


######################### Configuration #########################
st.set_page_config(
    layout="wide",
    page_title="Farm",
    page_icon=":earth_americas:",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    /* El stApp es el 'contenedor' donde se ejecuta el streamlit */
    .stApp { 
        background-color: #555879;
    }
    </style>
    """,
    unsafe_allow_html=True
)

######################### Title #########################
st.markdown("<h1 style='font-size: 40px; text-align: center; color: #DED3C4;'>Farm</h1>", unsafe_allow_html=True)
st.markdown("---")

######################### Folium #########################
########## GEOJSON ##########
# Load GeoJSON data
with open("../Back/geojson/departamentos-argentina.geojson", encoding="utf-8") as f: 
    geo_json_data = json.load(f)

# Extract departments
departamentos = sorted([feature['properties']['departamento'] for feature in geo_json_data['features']])

# Sidebar for departament selection
selected_deptos = st.multiselect("Seleccionar departamentos", departamentos)
def estilo(feature):
    depto = feature['properties']['departamento']
    if depto in selected_deptos:
        return {
            "fillColor": "transparent",
            "color": "green",  # Contorno verde si está seleccionado
            "weight": 3
        }
    else:
        return {
            "fillColor": "transparent",
            "color": "#cccccc",  # Gris para no seleccionados
            "weight": 1
        }

#Creating a Folium map
mapa = folium.Map(location=[-36.5, -60.0], zoom_start=6)

# Adding GeoJSON layer to the map
folium.GeoJson(
    geo_json_data,
    style_function=estilo,
    popup=folium.features.GeoJsonPopup(fields=['departamento'], aliases=['Departamento:'])
    #tooltip=folium.features.GeoJsonTooltip(fields=['departamento'], aliases=['Departamento:'])
).add_to(mapa)

# Displaying the map in Streamlit
folium_static(mapa, width=700, height=400)

# Displaying the selected departments
if selected_deptos:
    st.markdown(f"<h2 style='font-size: 25px; color: #DED3C4;'>Departamentos seleccionados:</h2><br><p style='font-size: 15px;'>{', '.join([depto.capitalize() for depto in selected_deptos])}</p>", unsafe_allow_html=True)
else:
    st.markdown("<h2 style='font-size: 25px; color: #DED3C4;'>No se han seleccionado departamentos</h2>", unsafe_allow_html=True)

