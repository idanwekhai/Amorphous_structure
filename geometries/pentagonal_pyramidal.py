import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def pentagonal_pyramidal():

    st.header("Pentagonal pyramidal")
    HtmlFile = open(all_html_dirs['pentagonal pyramidal'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", value=None, placeholder="Composition")
    pentagonal_pyramidal_val = st.number_input("Pentagonal pyramidal value", value=None, placeholder="Pentagonal pyramidal value")
    vals = [density, composition, pentagonal_pyramidal_val]
    pred = ""
    if None not in vals:
        pred = models['pentagonal pyramidal'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")