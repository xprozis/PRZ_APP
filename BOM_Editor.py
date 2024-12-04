import streamlit as st
from pages.shared.shared import *
from controller.BOM_Editor_c import *
from controller.Report_Editor_c import *
import os

export_name_file = "BOM_for_quotation"
df_edited = pd.DataFrame()

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("BOM Editor","In this page the user can load, add and edit the BOM final quantities")

# Carregar dados
file = st.file_uploader("Drop here your BOM.xlsl file related to your project", type="xlsx", on_change=clean_df)
if file:
    df = pd.read_excel(file)
    save_df_global(df)

# Load data
df_view = load_dataframe()

if  df_view.empty:
    st.divider()
    st.caption("In this section, the user can drop the original BOM file, configure the right provideres and add the PCB quantitiies and items number.")

col1, col2 = st.columns([1,6])
with col1:
    if not df_view.empty:
        qty = st.number_input("ADD Columns with PCB quantities:", value= 0, min_value=0, step=500)
        if qty > 0: button_state = False 
        else: button_state = True
        if st.button("➕", use_container_width=True, disabled = button_state):
            df_view = column_add(qty)
        if st.button("➖", use_container_width=True, disabled = button_state):
            df_view = column_remove()

with col2:
    if not df_view.empty:
        #double_space()
        radio_view = st.radio("View type:",["Full", "Simple"], horizontal=True)
        df_view = filter_dataframe_to_view(df_view,radio_view)
        
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
                )},
                num_rows="dynamic",
                hide_index=True)
        
        save_table_dataframe(df_edited)

    if not df_view.empty:
        col1, col2 = st.columns([1,2])
        with col1:
            if df_view.equals(df_bom_table_edited): 
                button_state = True
            else: 
                button_state = False

            if st.button("Save changes", use_container_width=True, disabled=button_state):
                df_view = save_table_edits()
                #st.rerun()
        with col2:
            st.download_button(label="Download Excel file", data = to_excel(df_view), file_name= export_name_file + ".xlsx", use_container_width=True, type="primary")

