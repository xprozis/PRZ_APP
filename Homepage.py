import streamlit as st
from pages.shared.pageheader import *
from controller.Data_Viewer import *


st.set_page_config(
    page_title="PROZIS",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("ProzisX - Logistics")

col1, col2, col3, col4 = st.columns(4)
with col1:
    dir_list = os.listdir(path)
    project_name = st.selectbox("Project name select:" , os.listdir(path))
with col2:
    pcb_name = st.selectbox("PCB name select:" , os.listdir(path + "/" + project_name))
with col3:
    pcb_version = st.selectbox("PCB name select:" , os.listdir(path + "/" + project_name + "/" + pcb_name))
    data_frame_view_raw = load_to_dataframe(path + "/" + project_name + "/" + pcb_name + "/" + pcb_version + "/BOM", "/BOM.xlsx")

# Apresentar Tabela
col1, col2 = st.columns([4,1])
with col1:
    st.subheader("BOM + Quotation 📋")
    data_frame_view_edited = st.data_editor(data_frame_view_raw, use_container_width=True, height=400, disabled=True)
with col2:
    st.subheader("Cost Information")

    st.number_input("PCB Quantity:", min_value=1, value=1, step=1)
    st.caption("Total: 3000 €")
    st.caption("Price (und): 10 €")

st.divider()
st.subheader("PartNumber details")