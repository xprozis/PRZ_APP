import pandas as pd
import streamlit as st
import os

st.set_page_config(
    page_title="PROZIS",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Passar para ficheiro partilhado
def page_header(titulo):
    st.title(titulo)
    st.divider()
page_header("Homepage")


cwd = os.getcwd()
print(cwd)

