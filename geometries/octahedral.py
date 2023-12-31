import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def octahedral():

    st.header("Octahedral")
    HtmlFile = open(all_html_dirs['octahedral'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='oct_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='oct_comp', value=None, placeholder="Composition")
    octahedral_val = st.number_input("Octahedral value", key='oct_val', value=None, placeholder="Octahedral value")
    vals = [density, composition, octahedral_val]
    pred = ""
    if None not in vals:
        pred = models['octahedral'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
