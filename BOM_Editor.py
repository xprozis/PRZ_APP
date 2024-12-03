import streamlit as st
from pages.shared.pageheader import *
from controller.BOM_Editor_c import *
from controller.Report_Editor_c import *
import os

export_name_file = "BOM_for_quotation"
df = pd.DataFrame()
df_edited = pd.DataFrame()


st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("BOM Editor","In this page the user can load, add and edit the BOM final quantities")

# Carregar dados
file = st.file_uploader("Drop here your BOM.xlsl file related to your project", type="xlsx")
if file:
    df = pd.read_excel(file)
    save_df_global(df)


# Load data
df_view = load_dataframe()

if df_view.empty:
    st.caption("No data to show.")

col1, col2 = st.columns([1,5])

with col1:
    if not df_view.empty:
        qty = st.number_input("ADD Columns with PCB quantities:", value= 0, min_value=0, step=500)
        if qty > 0: button_state = False 
        else: button_state = True
        if st.button("➕", use_container_width=True, disabled = button_state):
            df_view = column_add(qty)
        if st.button("➖", use_container_width=True, disabled = button_state):
            df_view = column_remove()
        if st.button("Save Providers", use_container_width=True):
            df_view = save_table_edits()
            st.rerun()
    
with col2:
    if not df_view.empty:
        df_edited = st.data_editor(
            df_view,
            use_container_width=True,
            column_config={
                "Provider_Name": st.column_config.SelectboxColumn(
                    "ProviderName",
                    help="The category of the app",
                    width="medium",
                    options=[
                        "ARROW",
                        "RUTRONIK",
                        "AVNET",
                    ],
                    required=True,
                )
            }, hide_index=True)
        save_table_dataframe(df_edited)


col1, col2 = st.columns([1,5])
with col2:
    if not df_view.empty:
        st.download_button(label="Export Excel", data = to_excel(df_view), file_name= export_name_file + ".xlsx", use_container_width=True, type="primary")

