import streamlit as st
import pandas as pd
import os

def load_to_dataframe (name):
    """
        Esta funcção carrega os ficheiros excel para um dataframe
    """
    path = "./model/DB/"
    df = pd.read_excel(path + name + ".xlsx")
    return df

 