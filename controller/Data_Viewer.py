import streamlit as st
import pandas as pd
import os



def load_to_dataframe (path, name):
    """
        Esta funcção carrega os ficheiros excel para um dataframe
    """
    df = pd.read_excel(path + name)
    return df
