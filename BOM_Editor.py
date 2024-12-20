import streamlit as st
from pages.shared.shared import *
from controller.BOM_Editor_c import *
from office365.sharepoint.files.file import File
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext


# SharePoint and Folder urls
sharepoint_url = "https://ositsgps.sharepoint.com/:f:/s/ElectronicX/En8NKEJoIHNCv3AR1IjW2qoBzJC0ejSO3F6Qe_w3JAy8dw?e=89Qw4N"
folder_in_sharepoint = "https://ositsgps.sharepoint.com/:f:/s/ElectronicX/Er6IbqKJHYRAhP5EIXixNdUBO8NCOKUtoZmULUeu-WesSQ?e=HgwH8P"

st.set_page_config(
    page_title="PROZIS HW Logistics",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)


page_header("BOM Editor","In this page the user can load, add and edit the BOM final quantities")



# First section: e-mail and password as input
placeholder = st.empty()
with placeholder.container():
  col1, col2, col3 = st.columns(3)
  with col2:
    st.subheader("Login to sharepoint")
    email_user = st.text_input("Your e-mail")
    password_user = st.text_input("Your password", type="password")

    # Save the button status
    Button = st.button("Connect", type="primary", use_container_width=True)
    if st.session_state.get('button') != True:
      st.session_state['button'] = Button

# Authentication and connection to SharePoint
def authentication(email_user, password_user, sharepoint_url) :
  auth = AuthenticationContext(sharepoint_url) 
  auth.acquire_token_for_user(email_user, password_user)
  ctx = ClientContext(sharepoint_url, auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  return ctx

# Second section: display results
# Check if the button "Connect" has been clicked
if st.session_state['button'] :  
  try :                            
    placeholder.empty()
    if "ctx" not in st.session_state :
        st.session_state["ctx"] = authentication(email_user, 
                                                 password_user,
                                                 sharepoint_url)
    
    st.write("Authentication: successfull!")
    st.write("Connected to SharePoint: **{}**".format( st.session_state["ctx"].web.properties['Title']))
  
    # Connection to the SharePoint folder
    target_folder = st.session_state["ctx"].web.get_folder_by_server_relative_url(folder_in_sharepoint)
    
    # Read and load items
    items = target_folder.files
    st.session_state["ctx"].load(items)
    st.session_state["ctx"].execute_query()
    
    # Save some information for each file using item.properties
    names, last_mod, relative_url = [], [], []
    for item in items:
        names.append( item.properties["Name"] )
        last_mod.append( item.properties["TimeLastModified"] )
        relative_url.append( item.properties["ServerRelativeUrl"] )
     
    # Create and display the final data frame
    Index = ["File name", "Last modified", "Relative url"]
    dataframe = pd.DataFrame([names, last_mod, relative_url], index = Index).T
    st.write("")
    st.write("")
    st.write("These are the files in the folder:")
    st.table(dataframe)
  
  # Handle the error in the authentication section
  except :
    col1, col2, col3 = st.columns(3)
    with col2:
      st.write("**Authentication error: reload the page**")

      
# Sempre que carregar no componente, faz reset ao dataframe e carrega um novo dataframe para a página e para uma variavel global guardada no controlador
file = st.file_uploader("Drop here your BOM.xlsl file related to your project", type="xlsx", on_change=clean_df)
if file:
    df = pd.read_excel(file)
    save_df_global(df,file.name)

# Carrega do ficheiro original para a página, desta forma o carregamento do ficheiro so se faz quando o utilizador assim o pretender
df_view = df_view_load()

# Principal conteudo da pagina (Tabelas botoes)
if  df_view.empty:
    st.divider()
    st.caption("In this section, the user can drop the original BOM file, configure the right provideres and add the PCB quantitiies and items number. Please drop your BOM file")
else:
    col1, col2 = st.columns([1,6])
    with col2:
        double_space()
        df_view_table = st.data_editor(
            df_view,
            use_container_width=True,
            column_config={
                "Provider_Name": st.column_config.SelectboxColumn(
                    "ProviderName",
                    help="Select the provider name",
                    width="medium",
                    options=[
                        "Quotation Provider",
                        "ARROW",
                        "RUTRONIK",
                        "AVNET",
                    ],
                    required=True,
                )}, hide_index=True)
        
        # Always saving the edits from the table
        save_df_table_edit(df_view_table)
    
    with col1:
        qty = st.number_input("ADD Columns with PCB quantities:", value= 0, min_value=0, step=500)
        if qty > 0: button_state = False 
        else: button_state = True
        if st.button("➕", use_container_width=True, disabled = button_state):
            df_view = quantities_add(df_view_table, qty)
            save_df_view(df_view)
            st.rerun()
        if st.button("Refresh data", use_container_width=True):
            df_view = quantities_remove(df_view_table)
            save_df_view(df_view)
            st.rerun()
        if st.download_button(label="Export BOM File", data = to_excel(df_view_table), file_name = "Qty_" + get_file_name(), use_container_width=True, type="primary"):
            st.success('File created')