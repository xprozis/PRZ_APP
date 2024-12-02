import streamlit as st
from pages.shared.pageheader import *
from controller.BOM_Editor_c import *

df_bom_file = pd.DataFrame()
df_quotation_file = pd.DataFrame()
df_quotation_costum_file = pd.DataFrame( columns=['MPN', 'Total_Qty_1', 'Unit_Price_1', 'Total_Qty_2', 'Unit_Price_2', 'Total_Qty_3', 'Unit_Price_3'])


quotation_create_view_flag = False 
quotation_create_view_flag = set_global(quotation_create_view_flag)

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("Report Creator","In this page the user can load, add and edit the BOM final quantities")

# Upload data section
col1, col2 = st.columns(2)
with col1:
    bom_file = st.file_uploader("Drop here your BOM.xlsl file realted to your project", type="xlsx")
    if bom_file:
        df_bom_file = pd.read_excel(bom_file)
with col2:        
    quotation_file = st.file_uploader("Drop here your COSTS.xlsl file realted to your project", type="xlsx", accept_multiple_files=False)
    if quotation_file:
        df_quotation_file = pd.read_excel(quotation_file)

# Data Join Table
st.divider()
st.subheader("Report (BOM + Quotation)")

if df_bom_file.empty or df_quotation_file.empty:
    st.caption("No data to show. Select the two files")
else:
    report = report_maker(df_bom_file,df_quotation_file)
    st.dataframe(report,use_container_width=True)
    
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        file_name = st.text_input("Project Name", placeholder="File name", label_visibility="collapsed")
        if len(file_name)>0:
            button_state = False
        else:
            button_state = True
    with col2:
        df_xlsx = to_excel(report)
        st.download_button(label="Export Excel",data=df_xlsx, file_name= file_name + ".xlsx", disabled=button_state, type="primary")