import streamlit as st
from pages.shared.pageheader import *
from controller.Data_Viewer import *

data_frame_view_raw = pd.DataFrame()
data_frame_view_edited = pd.DataFrame()

st.set_page_config(
    page_title="PROZIS",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("Data Viewer")

# Carregadmentos dos dados / Cabecalho da tabela
data_frame_view_raw = load_to_dataframe("database")
data_frame_view_edited = st.data_editor(data_frame_view_raw, height=600, use_container_width=True)

