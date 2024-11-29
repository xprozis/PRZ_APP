import streamlit as st
from pages.shared.pageheader import *
from controller.Data_Viewer import *
import numpy as np


path = "./model/Projects"


st.set_page_config(
    page_title="PROZIS",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("ProzisX - Logistics")


col1, col2,col3, col4 = st.columns(4)
with col1:
    dir_list = os.listdir(path)
    project_name = st.selectbox("Project name select:" , os.listdir(path))
with col2:
    subproject_name = st.selectbox("PCB name select:" , os.listdir(path + "/" + project_name))
with col4:
    st.text("")
    st.text("")
    # Carregadmentos dos dados / Cabecalho da tabela
    if st.button("Load data",use_container_width=True, type="primary"):
        data_frame_view_raw = load_to_dataframe(path + "/" + project_name + "/" + subproject_name + "/BOM", "/BOM")

# Apresentar Tabela
st.divider()
st.subheader("BOM file 📋")
data_frame_view_edited = st.dataframe(data_frame_view_raw, use_container_width=True)

st.divider()
st.subheader("Quotation details")
col1, col2, col3, col4 = st.columns(4)
with col1:
    provider = st.selectbox("Provider:" , ("Arrow", "Rutronik"))
