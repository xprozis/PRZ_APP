import streamlit as st
import pandas as pd
import os

path = "./model/Projects"

def load_to_dataframe (path, name):
    """
        Esta funcção carrega os ficheiros excel para um dataframe
    """
    df = pd.read_excel(path + name)
    return df
