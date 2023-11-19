import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app

def see_saw_like():

    st.header("See-Saw like")
    HtmlFile = open(all_html_dirs['see-saw-like'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", value=None, placeholder="Composition")
    t_shaped_val = st.number_input("See-Saw like value", value=None, placeholder="see_saw_like value")
    vals = [density, composition, t_shaped_val]
    pred = ""
    if None not in vals:
        pred = models['see-saw-like'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
