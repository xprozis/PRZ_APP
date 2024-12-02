import streamlit as st
import pandas as pd

variable_gb_aux = True
df_bom_quotation = pd.DataFrame()

def set_global(variable):
    global variable_gb_aux
    variable_gb_aux = variable
    return variable_gb_aux

def load_to_dataframe (path, name):
    """
        Esta funcção carrega os ficheiros excel para um dataframe
    """
    df = pd.read_excel(path + name)
    return df
