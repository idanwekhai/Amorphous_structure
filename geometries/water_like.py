import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def water_like():

    st.header("water_like")
    HtmlFile = open(all_html_dirs['water-like'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='water_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='water_comp', value=None, placeholder="Composition")
    water_like_val = st.number_input("water_like value", key='water_val', value=None, placeholder="water_like value")
    vals = [density, composition, water_like_val]
    pred = ""
    if None not in vals:
        pred = models['water-like'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
