import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def linear():

    st.header("Linear")
    HtmlFile = open(all_html_dirs['linear'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='lin_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='lin_comp', value=None, placeholder="Composition")
    linear_val = st.number_input("Linear value", key='lin_val', value=None, placeholder="Linear value")
    vals = [density, composition, linear_val]
    pred = ""
    if None not in vals:
        pred = models['linear'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
