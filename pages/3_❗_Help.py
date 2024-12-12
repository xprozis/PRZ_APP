import streamlit as st
from pages.shared.shared import *
import pandas as pd

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_header("Help page 👋", "Isto é uma pagina de ajuda")

user_feedback = "Escreva algo..."

image_path = "https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80"
image_path_2 = "./pages/shared/Logo_Prozis.png"

with st.form(key='my_form'):
	theme = st.text_area(label='We value your feedback. Please tell us more about your experience.')
	submit_button = st.form_submit_button(label='Submit')

st.divider()

# Save button
new_user_feedback = st.text_area(label = "We value your feedback. Please tell us more about your experience.", value=user_feedback)
if st.button("Gravar feedback"):
    user_feedback = new_user_feedback
    st.success("Gravado com sucesso")
#st.download_button("Gravar feedback em txt", file_name="Readme.txt", data=user_feedback, use_container_width=False, type="primary")

# Table
minha_tabela = {'Qty': [1, 2], 'MPN': ["213123s", "AAAZB"]}
df = pd.DataFrame(minha_tabela)
st.table(df)

st.caption("Depois de adicionar")
df_2 = pd.DataFrame({'Nova_coluna': [1, 2,2,5,7,4,2,4]})
df_concat = pd.concat([df,df_2], ignore_index=True)

df_edited_values = st.data_editor(df)
st.divider()

st.table(df_edited_values)

st.subheader("1) How can I edit my BOM file?")
with st.expander("Clique para ver as respostas"):
    st.caption('a) Click on "Browse files" button')
    st.caption('a) Add PCB quantities')
    st.caption('a) Click on "Export BOM" button')

st.subheader("2) How can I edit my Quotation?")
with st.expander("Clique para ver as respostas"):
    st.caption('a) Drop your BOM.xlsl file related to your project')
    st.caption('a) Edit table')

st.subheader("3) How can I edit my Quotation?")
with st.expander("Clique para ver as respostas"):
        st.caption('a) Drop your BOM.xlsl file related to your project')

double_space()
st.image(image_path_2,"")