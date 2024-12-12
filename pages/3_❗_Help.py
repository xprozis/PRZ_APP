import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.write("# Welcome to our Help page! 👋")
image_path = "https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80"
image_path_2 = "./pages/shared/Logo_Prozis.png"

with st.form(key='my_form'):
	theme = st.text_area(label='We value your feedback. Please tell us more about your experience.')
	submit_button = st.form_submit_button(label='Submit')

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

st.image(image_path_2,"")