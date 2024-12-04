import streamlit as st
import pandas as pd
from io import BytesIO
import streamlit as st

df_bom_table_edited = pd.DataFrame()
df_bom_file_edited = pd.DataFrame()
quantity_counter = 1


def teste():
    df_bom_file_edited.drop(df_bom_file_edited.index , inplace=True)

def save_df_global(df):
    global df_bom_file_edited
    global quantity_counter

    if df_bom_file_edited.empty:
        df_bom_file_edited = df
        reset_counter()


def to_excel(df):
    reset_counter()
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


def column_add(value):
    global quantity_counter
    global df_bom_file_edited
    
    if quantity_counter == 0:
        df_bom_file_edited['Provider_Name'] = "ARROW"

    df_bom_file_edited['Qty_PCBUnits_' + str(quantity_counter + 1)] = value
    df_bom_file_edited['Qty_' + str(quantity_counter + 1)] = value * df_bom_file_edited['Qty']
    quantity_counter+=1

    return df_bom_file_edited


def column_remove():
    global quantity_counter
    global df_bom_file_edited

    if quantity_counter > 0:
        df_bom_file_edited = df_bom_file_edited.iloc[:,:-2]
        quantity_counter+=-1

    return df_bom_file_edited

def save_table_dataframe(df):
    global df_bom_table_edited
    df_bom_table_edited = df

def load_dataframe():
    global df_bom_file_edited
    return df_bom_file_edited

def save_table_edits():
    global df_bom_table_edited
    global df_bom_file_edited
    df_bom_file_edited = df_bom_table_edited
    return df_bom_file_edited

def reset_counter():
    global quantity_counter
    quantity_counter = 0

