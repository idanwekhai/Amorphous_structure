import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def pentagonal_planar():

    st.header("Pentagonal planar")
    HtmlFile = open(all_html_dirs['pentagonal planar'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", value=None, placeholder="Composition")
    pentagonal_planar_val = st.number_input("Pentagonal planar value", value=None, placeholder="Pentagonal planar value")
    vals = [density, composition, pentagonal_planar_val]
    pred = ""
    if None not in vals:
        pred = models['pentagonal planar'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")