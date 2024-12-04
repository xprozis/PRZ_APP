import streamlit as st
from pages.shared.shared import *
from controller.BOM_Editor_c import * 

df_quotation = pd.DataFrame()

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("Quotation Editor","In this page the user can load, add and edit the BOM final quantities")

# Sempre que carregar no componente, faz reset ao dataframe e carrega um novo dataframe para a página e para uma variavel global guardada no controlador
file = st.file_uploader("Drop here your BOM.xlsl file related to your project", type="xlsx", on_change=clean_df)
if file:
    df = pd.read_excel(file)
    save_df_global(df,file.name)

# Carrega do ficheiro original para a página, desta forma o carregamento do ficheiro so se faz quando o utilizador assim o pretender
df_view = df_view_load()

# Pagina para quando nao há informacao
if  df_view.empty:
    st.divider()
    st.caption("In this section, the user can drop the original BOM file, configure the right provideres and add the PCB quantitiies and items number. Please drop your BOM file")
else:
    df_view_table = st.data_editor(
        df_view,
        use_container_width=True,
        column_config={
            "Provider_Name": st.column_config.SelectboxColumn(
                "ProviderName",
                help="Select the provider name",
                width="medium",
                options=[
                    "Quotation Provider",
                    "ARROW",
                    "RUTRONIK",
                    "AVNET",
                ],
                required=True,
            )}, hide_index=True)