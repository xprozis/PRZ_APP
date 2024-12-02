import streamlit as st
from pages.shared.pageheader import *
from controller.BOM_Editor_c import * 

df_quotation = pd.DataFrame()

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("Quotation Editor","In this page the user can load, add and edit the BOM final quantities")

quotation_file = st.file_uploader("Drop here your Report.xlsl file related to your project", type="xlsx")
if quotation_file:
    df_quotation = pd.read_excel(quotation_file)

if not df_quotation.empty:
    # Create table
    df_bom_edited = st.data_editor(df_quotation, use_container_width=True)
