import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def hexagonal_planar():

    st.header("Hexagonal planar")
    HtmlFile = open(all_html_dirs['hexagonal planar'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='hpl_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='hpl_comp', value=None, placeholder="Composition")
    hexagonal_planar_val = st.number_input("Hexagonal planar value", key='hpl_val', value=None, placeholder="hexagonal_planar value")
    vals = [density, composition, hexagonal_planar_val]
    pred = ""
    if None not in vals:
        pred = models['hexagonal planar'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
