import streamlit as st
import pandas as pd

df_file_raw = pd.DataFrame()
df_file_raw_view_edit = pd.DataFrame()
quantity_counter = 0

def save_df_global(df, name):
    global name_file
    global df_file_raw
    global df_file_raw_view_edit
    global quantity_counter

    if df_file_raw_view_edit.empty:
        name_file = name
        df_file_raw_view_edit = df
        df_file_raw = df
        quantity_counter = 0

def df_view_load():
    global df_file_raw_view_edit
    return df_file_raw_view_edit

def clean_df():
    df_file_raw_view_edit.drop(df_file_raw_view_edit.index , inplace=True)