import streamlit as st
import functions as fn

st.set_page_config(layout="wide", page_title="Medical Tracker")
page_bg_image = """
    <style>
    [data-testid="stAppViewContainer"]{
        background-image: url("https://images.unsplash.com/photo-1587370560942-ad2a04eabb6d?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
    }
    [data-testid="stHeader"]{
        background-color: rgba(0, 0, 0, 0);
    }        
    </style>
"""
st.markdown(page_bg_image, unsafe_allow_html=True)


fn.image_main_header("Student Medical Status Notifier", "https://c.pxhere.com/images/1b/10/39f51f849d260466caeb6d043b9f-1678646.jpg!d")

print(st.session_state)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.new_response_message = False

if not st.session_state.logged_in:
    fn.get_login_info()
elif st.session_state.new_response_message:
    fn.new_resp_message()
else:
    fn.get_patient_info()
