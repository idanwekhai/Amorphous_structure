import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def square_pyramidal():

    st.header("Square pyramidal")
    HtmlFile = open(all_html_dirs['square pyramidal'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", value=None, placeholder="Composition")
    square_pyramidal_val = st.number_input("Square pyramidal value", value=None, placeholder="square pyramidal value")
    vals = [density, composition, square_pyramidal_val]
    pred = ""
    if None not in vals:
        pred = models['square pyramidal'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")