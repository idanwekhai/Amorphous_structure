import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app


def tetrahedral():

    st.header("Tetrahedral")
    HtmlFile = open(all_html_dirs['tetrahedral'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key='tet_den', value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key='tet_comp',value=None, placeholder="Composition")
    tetrahedral_val = st.number_input("Tetrahedral value", key='tet_val', value=None, placeholder="Tetrahedral value")
    vals = [density, composition, tetrahedral_val]
    pred = ""
    if None not in vals:
        pred = models['tetrahedral'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")