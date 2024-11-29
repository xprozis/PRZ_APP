import streamlit as st
import pandas as pd
import os

data_frame_view_raw = pd.DataFrame()
data_frame_view_edited = pd.DataFrame()

def load_to_dataframe (path, name):
    global data_frame_view_raw
    """
        Esta funcção carrega os ficheiros excel para um dataframe
    """
    data_frame_view_raw = pd.read_excel(path + name + ".xlsx")
    return data_frame_view_raw

