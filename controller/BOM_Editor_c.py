import streamlit as st
import pandas as pd
from io import BytesIO
import streamlit as st

name_file = "BOM.xlsx"
df_file_raw = pd.DataFrame()
df_file_edit = pd.DataFrame()
df_table = pd.DataFrame()
quantity_counter = 0


def save_df_global(df, name):
    global name_file
    global df_file_raw
    global df_file_edit
    global quantity_counter

    if df_file_edit.empty:
        name_file = name
        df_file_edit = df
        df_file_raw = df
        quantity_counter = 0
        df_file_edit['Provider_Name'] = "Quotation Provider"
   

def clean_df():
    df_file_edit.drop(df_file_edit.index , inplace=True)


def df_view_load():
    global df_file_edit
    return df_file_edit


def save_df_view(df):
    global df_file_edit
    df_file_edit = df
    return df_file_edit


def save_df_table_edit(df):
    global df_table
    df_table = df


def get_file_name():
    global name_file
    return name_file


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


def to_excel_multiple(df):
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


def quantities_add(df,value):
    global quantity_counter
    df['Qty_PCBUnits_' + str(quantity_counter + 1)] = value
    df['Qty_' + str(quantity_counter + 1)] = value * df['Qty']
    quantity_counter+=1
    return df


def quantities_remove(df):
    global quantity_counter

    if(quantity_counter > 0):
        df = df[df.columns[:-2*quantity_counter]]
    quantity_counter = 0
    df['Provider_Name'] = "Quotation Provider"
    return df


def reset_counter():
    global quantity_counter
    quantity_counter = 0


def filter_dataframe_to_view(df,view_type):
    if view_type == "Simple":
        df = df.filter(items=['Qty', '1_MPN'])
    return df


