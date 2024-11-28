import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PROZIS",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Warehouse Dashboard")



def read_excel_file():

    # Exemplo de uma BOM (EXEMPLO
    BOM_SD = "./Prozis Group S.A/ElectronicX - Hardware/Projects/pcb0002 Prozis Smart Device/pcb0002HR - Heart Rate Board/V2.2/pcb0002HR_v2_2/Production/Assembly/"

    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel(BOM_SD + "pcb0002HR_v2_2_bom.xlsx")
    print("testez")

read_excel_file()