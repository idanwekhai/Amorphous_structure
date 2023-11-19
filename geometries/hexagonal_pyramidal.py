import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def hexagonal_pyramidal():

    st.header("Hexagonal pyramidal")
    HtmlFile = open(all_html_dirs['hexagonal pyramidal'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='hpy_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='hpy_comp', value=None, placeholder="Composition")
    hexagonal_pyramidal_val = st.number_input("Hexagonal pyramidal value", key='hpy_val', value=None, placeholder="hexagonal_pyramidal value")
    vals = [density, composition, hexagonal_pyramidal_val]
    pred = ""
    if None not in vals:
        pred = models['hexagonal pyramidal'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
