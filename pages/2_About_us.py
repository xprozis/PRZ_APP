import streamlit as st
from pages.shared.pageheader import *
from controller.Data_Viewer import *
import os 


st.set_page_config(
    page_title="PROZIS",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("About us")

