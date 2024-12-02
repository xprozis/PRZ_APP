import streamlit as st
from pages.shared.pageheader import *
from controller.Data_Viewer import *
import os

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("BOM Editor","In this page the user can load, add and edit the BOM final quantities")

# Apresentar Tabela
bom_file = st.file_uploader("Drop here your BOM.xlsl file related to your project", type="xlsx")
if bom_file:
    df_bom_file = pd.read_excel(bom_file)

# Adicionar BOM editor
