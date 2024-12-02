import streamlit as st
import pandas as pd

variable_gb_aux = True
df_bom_quotation = pd.DataFrame()

def set_global(variable):
    global variable_gb_aux
    variable_gb_aux = variable
    return variable_gb_aux

def load_to_dataframe(path, name):
    """
        Esta funcção carrega os ficheiros excel para um dataframe
    """
    df = pd.read_excel(path + name)
    return df

def report_maker(df1,df2):
    """
        Esta funcao vai juntar o Dataframe BOM com o Dataframe COST atraves de um LEFT-JOIN
    """
    df = pd.merge(df1, df2, how='left',on='1_MPN')
    return df
