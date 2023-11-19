import streamlit as st
import streamlit.components.v1 as components

from .utils import all_html_dirs, models


# embed streamlit docs in a streamlit app


def sgl_bd():

    st.header("Single Bond")
    HtmlFile = open(all_html_dirs['sgl_bd'], 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    st.header("Make Prediction")
    density =  st.number_input("Density Value", key=1, value=None, placeholder="density (g cm^-3)")
    composition =  st.number_input("Composition Value", key=2, value=None, placeholder="Composition")
    single_bond_val = st.number_input("SGL_BD value", key=3, value=None, placeholder="SGL_BD value")
    vals = [density, composition, single_bond_val]
    pred = ""
    if None not in vals:
        pred = models['sgl_bd'][1].predict([vals])[0]
    st.write(f"Energy: {pred}")
    # st.button("Predict", type="primary", on_click=st.write(f"Energy: {pred}"))
