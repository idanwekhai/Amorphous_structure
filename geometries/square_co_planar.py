import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def square_co_planar():

    st.header("Square Co-planar")
    HtmlFile = open(all_html_dirs['square co-planar'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", value=None, placeholder="Composition")
    square_co_planar_val = st.number_input("Square co-planar value", value=None, placeholder="square co_planar value")
    vals = [density, composition, square_co_planar_val]
    pred = ""
    if None not in vals:
        pred = models['square co-planar'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")