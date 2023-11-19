import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def body_centered_cubic():

    st.header("Body centered cubic")
    HtmlFile = open(all_html_dirs['body-centered cubic'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='bod_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='bod_comp', value=None, placeholder="Composition")
    body_centered_cubic_val = st.number_input("Body centered cubic value", key='bod_val', value=None, placeholder="body_centered_cubic value")
    vals = [density, composition, body_centered_cubic_val]
    pred = ""
    if None not in vals:
        pred = models['body-centered cubic'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
