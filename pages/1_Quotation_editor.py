import streamlit as st
from pages.shared.pageheader import *
from controller.Data_Viewer import *
import os 


st.set_page_config(
    page_title="PROZIS",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("Quotation editor")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    dir_list = os.listdir(path)
    project_name = st.selectbox("Project name select:" , os.listdir(path))
with col2:
    pcb_name = st.selectbox("PCB name select:" , os.listdir(path + "/" + project_name))
with col3:
    pcb_version = st.selectbox("PCB version select:" , os.listdir(path + "/" + project_name + "/" + pcb_name))
with col4:
    provider_name = st.selectbox("Quotation provider:", os.listdir(path + "/" + project_name+ "/" + pcb_name + "/" + pcb_version + "/Cost/"))
with col5:
    quotation_version = st.selectbox("Quotation version:", os.listdir(path + "/" + project_name+ "/" + pcb_name + "/" + pcb_version + "/Cost/" + provider_name) )
    
    df_view = load_to_dataframe(path + "/" + project_name + "/" + pcb_name + "/" + pcb_version + "/Cost/" + provider_name + "/", quotation_version)

st.subheader(provider_name + " Quotation")
data_frame_view_edited = st.data_editor(df_view, use_container_width=True, height=400, disabled=False)