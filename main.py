import streamlit as st

from streamlit_option_menu import option_menu


with st.sidebar:
    data = option_menu(
        menu_title= "myproject",
        options=["Home","About","Contact"]
    )


if data == "Home":
    st.title("Home")
    col1,col2,col3 = st.columns(3)
    with col1:
      #   st.write("Warning: PowerShell detected that you might be using a screen reader and has disabled PSReadLine for compatibility purposes. If you want to re-enable it, run 'Import-Module PSReadLine'.")
      st.text_input("Name")
      st.text_input("Name1")
      st.text_input("Name2")
      st.text_input("Name3")
    with col2:
      st.text_input("Name4")
      st.text_input("Name5")
      st.text_input("Name6")
      st.text_input("Name7")
    with col3:
      st.text_input("Name8")
      st.text_input("Name9")
      st.text_input("Name10")
    st.button("Submit")

elif data == "About":
    st.title("About")
    col1,col2=st.columns(2)
    with col1:
       st.write("A short story is a piece of prose fiction. It can typically be read in a single sitting and focuses on a self-contained incident or series of linked incidents, with the intent of evoking a single effect or mood. The short story is one of the oldest types of literature and has existed in the form of legends, mythic tales, folk tales, fairy tales, tall tales, fables, and anecdotes in various ancient communities around the world. The modern short story developed in the early 19th century.[1]")
      # st.text_input("student")
      # st.text_input("student1")
    with col2:
       st.image("https://img.freepik.com/premium-photo/image_1159192-2.jpg")
elif data == "Contact":
    st.title("Contact")