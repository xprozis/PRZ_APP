import streamlit as st

def page_header(title, description):
    """
    Gera um cabeçalho identico para todos
    
    """
    st.title(title,help=description)
    st.divider()


def double_space():
    st.markdown("")
    st.markdown("")