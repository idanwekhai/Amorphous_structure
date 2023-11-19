import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def bent_120_degrees():

    st.header("bent_120_degrees")
    HtmlFile = open(all_html_dirs['bent 120 degrees'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='120_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='120_comp', value=None, placeholder="Composition")
    bent_120_degrees_val = st.number_input("Bent 120 degrees value", key='120_val', value=None, placeholder="bent_120_degrees value")
    vals = [density, composition, bent_120_degrees_val]
    pred = ""
    if None not in vals:
        pred = models['bent 120 degrees'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
