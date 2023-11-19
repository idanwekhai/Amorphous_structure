import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def pentagonal_bipyramidal():

    st.header("Pentagonal_bipyramidal")
    HtmlFile = open(all_html_dirs['pentagonal bipyramidal'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='pby_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='pby_comp', value=None, placeholder="Composition")
    pentagonal_bipyramidal_val = st.number_input("Pentagonal bipyramidal value", key='pby_val', value=None, placeholder="Pentagonal bipyramidal value")
    vals = [density, composition, pentagonal_bipyramidal_val]
    pred = ""
    if None not in vals:
        pred = models['pentagonal bipyramidal'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")