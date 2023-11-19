import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def rectangular_see_saw_like():

    st.header("Rectangular See-Saw like")
    HtmlFile = open(all_html_dirs['rectangular-see-saw-like'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", value=None, placeholder="Composition")
    t_shaped_val = st.number_input("Rectangular See-Saw like value", value=None, placeholder="rectangular_see_saw_like value")
    vals = [density, composition, t_shaped_val]
    pred = ""
    if None not in vals:
        pred = models['rectangular-see-saw-like'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
