import streamlit as st
from datetime import datetime
from src import codes

#### SOURCES: https://docs.streamlit.io/library/advanced-features/multipage-apps



# ---------------------------- Initialization session state - works like a python dictionary ----------------------------
if all(key not in st.session_state.keys() for key in ('text_page_main', 'number_page_main', 'text_page_3')):
    st.session_state['text_page_main'] = 'Default string main page'
    st.session_state['number_page_main'] = 10
    st.session_state['text_page_3'] = 'Default string page threee'



# ---------------------------- SET SESSION STATE TO AVOID THE RESET WHEN THE USER SWITCH BETWEEN PAGES ----------------------------
# sources: https://stackoverflow.com/questions/74968179/session-state-is-reset-in-streamlit-multipage-app
st.session_state['text_page_main'] = st.session_state['text_page_main']
st.session_state['number_page_main'] = st.session_state['number_page_main']
st.session_state['text_page_3'] = st.session_state['text_page_3']



# ---------------------------- Page configuration ----------------------------
st.set_page_config(
    page_title="Homepage", # name that apear in the tab in web navigator
    page_icon="🏡", # icon that apear in the tab in web navigator
    layout="centered",
    initial_sidebar_state="auto"
)


# ---------------------------- invoke codes from script ----------------------------
msg_script = codes.invoke_function()
st.write('---')
st.write(msg_script)
st.write('---')


# ---------------------------- calculations ----------------------------
# get actual time
actual_time = datetime.now()
format_time = actual_time.strftime("%H:%M:%S %d/%m/%Y")



# ---------------------------- show information ----------------------------
# Give your app a title
st.title("Hello World update streamlit")

# Header
st.header("Hello World update streamlit")

# Subheader
st.subheader(f"The time is: {format_time}")



# ---------------------------- Write text transversal each page ----------------------------
st.divider()
st.divider()
st.write("### Write a TEXT that will be transversal between each page")

st.text_input("Write a transversal text", placeholder="Write a text", key = "text_page_main") # it is not necessary create a python variable
st.write(f"Text transversal: {st.session_state['text_page_main']}")



# ---------------------------- Write a transversal number ----------------------------
st.divider()
st.divider()
st.write("### Write a NUMBER that will be transversal between each page")

number_page_main_var = st.number_input("Pick a number", min_value=0, max_value=100, value=0, step=1, key = "number_page_main") # creating a python variable to operate the input value
st.write(f"Number transversal: {st.session_state['number_page_main']}")
st.write(number_page_main_var)


# ---------------------------- Show a all session states ----------------------------
st.divider()
st.divider()
st.write("### Show all session states")
st.write(st.session_state)