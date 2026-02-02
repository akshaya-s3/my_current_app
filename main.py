import streamlit as st

from streamlit_option_menu import option_menu


with st.sidebar:
    data = option_menu(
        menu_title= "myproject",
        options=["Home","About","Contact"]
    )


if data == "Home":
    st.title("Home page")
    st.title("Welcome to the home page")
    name=st.text_input("name")
    id=st.number_input("ID",min_value=1)
    gender=st.radio("Gender",options=["Male","Female"])
    city=st.selectbox("City",options=["Madurai","Chennai","Bangalore"])
    dob=st.date_input("Pic A Date")
    age=st.slider("Age",20,35)
    skills=st.multiselect("Skills",options=["Html","CSS","js","Python","java"])
    if st.button("Click"):
        st.write(name)
        st.success("Data Print Successfully")

elif data == "About":
    st.title("About")
    col1,col2=st.columns(2)
    with col1:
       st.write("A short story is a piece of prose fiction. It can typically be read in a single sitting and focuses on a self-contained incident or series of linked incidents, with the intent of evoking a single effect or mood. The short story is one of the oldest types of literature and has existed in the form of legends, mythic tales, folk tales, fairy tales, tall tales, fables, and anecdotes in various ancient communities around the world. The modern short story developed in the early 19th century.[1]")
    with col2:
       st.image("https://img.freepik.com/premium-photo/image_1159192-2.jpg")
elif data == "Contact":
    st.title("Contact")
