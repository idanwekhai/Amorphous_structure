import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def t_shaped():

    st.header("T-shaped")
    HtmlFile = open(all_html_dirs['T-shaped'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", value=None, placeholder="Composition")
    t_shaped_val = st.number_input("T-shaped value", value=None, placeholder="t-shaped value")
    vals = [density, composition, t_shaped_val]
    pred = ""
    if None not in vals:
        pred = models['T-shaped'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
