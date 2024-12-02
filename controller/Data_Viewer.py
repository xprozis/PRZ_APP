import streamlit as st
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import streamlit as st


variable_gb_aux = True
df_bom_quotation = pd.DataFrame()


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.close()
    processed_data = output.getvalue()
    return processed_data

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
