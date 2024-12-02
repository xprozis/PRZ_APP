import streamlit as st
from pages.shared.pageheader import *
from controller.Data_Viewer import *

quotation_create = False
df_bom_quotation = pd.DataFrame()
df_quotation_file = pd.DataFrame()

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("Quotation editor")

st.subheader("Upload files")
col1, col2 = st.columns(2)
with col1:
    bom_file = st.file_uploader("Drop here your BOM.xlsl file realted to your project", type="xlsx")
    if bom_file:
        df_bom_file = pd.read_excel(bom_file)
        df_bom_quotation = df_bom_file # DEV
with col2:        
    quotation_file = st.file_uploader("Drop here your COSTS.xlsl file realted to your project", type="xlsx")
    if quotation_file:
        df_quotation_file = pd.read_excel(quotation_file)
    if st.button("Create new quotation", use_container_width=True):
        quotation_create = True

# Page to create the quotation 
if quotation_create:
    # Title
    st.subheader("Quotation Creator")

    # Page Body

    # Footer
    col1,col2 = st.columns([4,1])
    with col1:
        if st.button("SAVE", type="primary", use_container_width=True):
            view = False
    with col2:
        if st.button("CLOSE", use_container_width=True):
            view = False

st.divider()
st.subheader("BOM + Quotation")
if df_bom_quotation.empty and df_quotation_file.empty:
    st.caption("No data to show.")
else:
    st.dataframe(df_bom_quotation)
    st.dataframe(df_quotation_file)