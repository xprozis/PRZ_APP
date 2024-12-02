import streamlit as st
from pages.shared.pageheader import *
from controller.Data_Viewer import *



df_bom_quotation = pd.DataFrame()
df_quotation_file = pd.DataFrame()
df_report = pd.DataFrame( columns=['MPN', 'Total_Qty_1', 'Unit_Price_1', 'Total_Qty_2', 'Unit_Price_2', 'Total_Qty_3', 'Unit_Price_3'])

quotation_create_view_flag = False 
quotation_create_view_flag = set_global(quotation_create_view_flag)

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("Report Creator")

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


    if st.button("Create Quotation manually", use_container_width=True):
        quotation_create_view_flag = True



# Page to create the quotation 
if quotation_create_view_flag:
    col1, col2 = st.columns([4,1])
    with col1:
        # Title
        st.subheader("Quotation Creator")
        # Page Body
        new_df_report = st.data_editor(df_report, use_container_width=True)
        
    # Footer
    col1,col2 = st.columns([4,1])
    with col1:
        if st.button("Save", type="primary", use_container_width=True):
            view = True
    with col2:
        if st.button("Close", use_container_width=True):
            view = False

st.divider()
st.subheader("Report (BOM + Quotation)")
if df_bom_quotation.empty and df_quotation_file.empty:
    st.caption("No data to show.")
else:
    st.dataframe(df_bom_quotation)
    st.dataframe(df_quotation_file)