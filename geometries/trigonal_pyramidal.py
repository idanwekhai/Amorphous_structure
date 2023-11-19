import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def trigonal_pyramidal():

    st.header("Trigonal pyramidal")
    HtmlFile = open(all_html_dirs['trigonal pyramidal'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", value=None, placeholder="Composition")
    trigonal_pyramidal_val = st.number_input("Trigonal pyramidal value", value=None, placeholder="trigonal pyramidal value")
    vals = [density, composition, trigonal_pyramidal_val]
    pred = ""
    if None not in vals:
        pred = models['trigonal pyramidal'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")