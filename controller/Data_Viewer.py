import streamlit as st
import pandas as pd


df_bom_quotation = pd.DataFrame()
quotation_create_flag = False

def load_to_dataframe (path, name):
    """
        Esta funcção carrega os ficheiros excel para um dataframe
    """
    df = pd.read_excel(path + name)
    return df
