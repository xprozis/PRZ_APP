import streamlit as st
import pandas as pd
from io import BytesIO
import streamlit as st

df_file_raw = pd.DataFrame()
df_file_raw_view_edit = pd.DataFrame()
quantity_counter = 0


def save_df_global(df):
    global df_file_raw
    global df_file_raw_view_edit
    global quantity_counter

    if df_file_raw.empty:
        df_file_raw = df
        df_file_raw_view_edit = df
        quantity_counter = 0
        df_file_raw_view_edit['Provider_Name'] = "Quotation Provider"
   

def clean_df():
    df_file_raw_view_edit.drop(df_file_raw_view_edit.index , inplace=True)


def df_view_load():
    global df_file_raw_view_edit
    return df_file_raw_view_edit


def save_df_view(df):
    global df_file_raw_view_edit
    df_file_raw_view_edit = df
    return df_file_raw_view_edit


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


def column_add(df,value):
    global quantity_counter

    df['Qty_PCBUnits_' + str(quantity_counter + 1)] = value
    df['Qty_' + str(quantity_counter + 1)] = value * df['Qty']
    quantity_counter+=1
    return df


def column_remove(df):
    global quantity_counter

    if(quantity_counter > 0):
        df = df[df.columns[:-2*quantity_counter]]
    quantity_counter = 0
    df['Provider_Name'] = "Quotation Provider"
    return df


def compare_df_df_raw(df):
    global df_file_raw
    if df.equals(df_file_raw):
        return True
    else:
        return False


def reset_counter():
    global quantity_counter
    quantity_counter = 0


def filter_dataframe_to_view(df,view_type):
    if view_type == "Simple":
        df = df.filter(items=['Qty', '1_MPN'])
    return df