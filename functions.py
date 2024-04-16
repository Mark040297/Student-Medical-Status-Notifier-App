import streamlit as st
from send_email import send_email
from datetime import date
import time

current_date = date.today()


def read_me():
    # HTML code for the container with word and image
    html_code = f"""
            <div class="readme_container">                
                <p class="readme_word">
                    Notice: This App can be used by a medical personnel to notify the concerned Faculty about
                    the medical status of his/her student. For demo purpose, kindly read the help icon right 
                    next to each input widgets.
                </p>            
            </div>
            """

    # CSS styles for positioning
    css_style = """
            .readme_container {
                display: flex;
                align-items: center;                   
                background-color: rgba(173, 216, 230, 0.3);
                border: 2px solid #01099e;
                border-radius: 10px;   
                width: 500px;    
                margin: 0 auto; 
                flex-wrap: wrap;  
            }
            .readme_word {
                margin: 0 auto; /* Adjust spacing between word and image */                           
                color: red; 
                font-size: 15px; 
                font-family: 'Pacifico', cursive; 
                font-weight: normal; 
                text-align: justify;                
                border: 2px solid lightyellow;
                border-radius: 10px;
            }        
            """

    # Display HTML and CSS
    st.markdown(html_code, unsafe_allow_html=True)
    st.write('<style>{}</style>'.format(css_style), unsafe_allow_html=True)


def get_logo(image_url):
    # HTML code for the container with word and image
    html_code = f"""
            <div class="patient_info_logo_container">
                <img src={image_url} class="patient_info_logo__image">                          
            </div>
            """

    # CSS styles for positioning
    css_style = """
            .patient_info_logo_container {
                display: flex;
                align-items: center;            
            }

            .patient_info_logo__image {
                width: 300px; /* Adjust image width as needed */
                height: auto; /* Maintain aspect ratio */                
                border: 2px solid lightyellow;
                border-radius: 10px;
                margin: 0 auto;
            }                   
            """

    # Display HTML and CSS
    st.markdown(html_code, unsafe_allow_html=True)
    st.write('<style>{}</style>'.format(css_style), unsafe_allow_html=True)


def get_login_info():
    login_container = st.empty()
    with login_container.container():
        get_logo(image_url="https://c.pxhere.com/images/89/88/f1a747343b1df1aede459939ebaf-1449661.jpg!d")
        read_me()
        st.markdown("""
                                    <style>
                                        div.st-emotion-cache-r421ms.e10yg2by1{
                                            background-color: rgba(60, 179, 113, 0.3);
                                            border: 2px solid #01099e;
                                            border-radius: 10px;                                    
                                        }
                                    </style>
                                    """, unsafe_allow_html=True)
        space_left2, content2, space_right2 = st.columns([1, 1.5, 1])
        with content2:
            with st.form(key='login_form'):
                username = st.text_input("Username", key='username', help="For trial purpose, use 'tracker101'")
                email_info = st.text_input("Email", key='email', help="For trial purpose, use your email add and in this email, you will get notified.")
                password = st.text_input("Password", key='password', type='password', help="For trial purpose, use 'medical101'")
                login_status = st.form_submit_button("login")
                if login_status:
                    if username == "tracker101" and password == "medical101" and email_info != "":
                        st.session_state.logged_in = True
                        st.session_state.email_info = email_info
                        st.rerun()
                    else:
                        st.error('Invalid username and password!', icon="🚨")


def get_patient_info():
    instructors = ['Your Name', 'Professor Ben', 'Professor Dan',
                   'Professor Chui', 'Professor Jurich', 'Professor Natan']
    MSA_sub = ['ESci 110m', 'ESci 123m', 'ESci 124m', 'MEng 133n', 'MEng 124n']
    AJB_sub = ['MEng 123n', 'ESci 116n', 'ESci 134a', 'MEng 198']
    VLI_sub = ['MEng 137', 'MEng 141', 'MEng 142']
    IQC_sub = ['MEng 156', 'MEng 155']
    ECO_sub = ['MEng 136', 'MEng 152']
    RGP_sub = ['MEng 158', 'MEng 154']
    login_container = st.empty()
    with login_container.container():
        get_logo(image_url="https://c.pxhere.com/images/6c/82/2197ff2bf50e38f3bf69deb28097-1589483.jpg!d")
        space_left2, content2, space_right2 = st.columns([1, 1.5, 1])
        with content2:
            with st.container(border=True):
                st.markdown("""
                            <style>
                                div.st-emotion-cache-r421ms.e1f1d6gn0{
                                    background-color: rgba(60, 179, 113, 0.3);
                                    border: 2px solid #01099e;
                                    border-radius: 10px;                                    
                                }
                            </style>
                            """, unsafe_allow_html=True)
                st.text_input("Patient Name", key='patient_name', help="Type in any patient name.")
                st.selectbox("Subject Instructor", options=instructors,
                             key='subject_instructor', placeholder="Please select!", help="Select 'Your Name' since the email you input earlier is associated with this name.")
                if st.session_state['subject_instructor'] == 'Your Name':
                    st.selectbox("Subject", MSA_sub, key='subject', help="Choose any subject.")
                elif st.session_state['subject_instructor'] == 'Professor Ben':
                    st.selectbox("Subject", AJB_sub, key='subject', help="Choose any subject.")
                elif st.session_state['subject_instructor'] == 'Professor Dan':
                    st.selectbox("Subject", VLI_sub, key='subject', help="Choose any subject.")
                elif st.session_state['subject_instructor'] == 'Professor Chui':
                    st.selectbox("Subject", IQC_sub, key='subject', help="Choose any subject.")
                elif st.session_state['subject_instructor'] == 'Professor Jurich':
                    st.selectbox("Subject", ECO_sub, key='subject', help="Choose any subject.")
                elif st.session_state['subject_instructor'] == 'Professor Natan':
                    st.selectbox("Subject", RGP_sub, key='subject')
                st.date_input("Onset Date", key='onset_date', format='MM/DD/YYYY', help="Select any date.")
                st.text_area("Medical Diagnosis and Advice", key='diagnosis', help="Put any diagnosis.")
                if st.session_state['patient_name'] != "" and st.session_state['subject_instructor'] != "" and \
                        st.session_state['subject'] != "" and st.session_state['diagnosis'] != "" and \
                        st.session_state['onset_date'] != "":
                    st.button("Submit", key='submit')
                else:
                    st.button("Submit", key='submit', disabled=True)
                if st.session_state['submit']:
                    message = f"""\
Subject: Medical Report from Hospital {current_date}                                        
Patient name >> {st.session_state['patient_name']}
Subject >> {st.session_state['subject']}
Onset Date >> {st.session_state['onset_date']}
Medical diagnosis and advice >> {st.session_state['diagnosis']}
                            """
                    send_email(message, st.session_state['subject_instructor'], st.session_state['email_info'])
                    with st.spinner("Please wait..."):
                        time.sleep(3)
                    st.success("Submission successful!")
    space_left3, content3, middle, content4, space_right3 = st.columns([2.75, 2, 0.25, 2, 1.75])
    with content3:
        st.button("New entry", key='new')
    with content4:
        st.button("Logout", key='logged_out')
    if st.session_state['new']:
        st.session_state.new_response_message = True
        st.rerun()
    if st.session_state['logged_out']:
        st.session_state.logged_in = False
        st.rerun()


def new_resp_message():
    login_container = st.empty()
    with (login_container.container()):
        get_logo("https://i.pinimg.com/736x/bc/ea/0e/bcea0e0a306b29cd0c8fc30fbbd0b870.jpg")
        space_left2, content2, space_right2 = st.columns([1, 1.5, 1])
        with content2:
            with st.container(border=True):
                st.markdown("""
                                            <style>
                                                div.st-emotion-cache-r421ms.e1f1d6gn0{
                                                    background-color: rgba(60, 179, 113, 0.3);
                                                    border: 2px solid #01099e;
                                                    border-radius: 10px;                                    
                                                }
                                            </style>
                                            """, unsafe_allow_html=True)
                st.caption("Would you like to create a new response?")
                space_left4, middle1, space_right4 = st.columns([3, 1, 3])
                with middle1:
                    st.button("Yes", key='yes')
                if st.session_state['yes']:
                    st.session_state.new_response_message = False
                    st.session_state.logged_in = True
                    st.rerun()


def image_main_header(header, image_url):
    # HTML code for the container with word and image
    html_code = f"""
        <div class="main_container">
            <img src="{image_url}" class="main_image">
            <h1 class="main_word">{header}</h1>            
        </div>
        """

    # CSS styles for positioning
    css_style = """
        .main_container {
            display: flex;
            align-items: center;
            flex-wrap: wrap;            
        }

        .main_image {
            width: 100px; /* Adjust image width as needed */
            height: auto; /* Maintain aspect ratio */
            border: 2px solid #01099e;
            border-radius: 60px;
            margin-left: 150px;
        }

        .main_word {
            margin-left: 10px; /* Adjust spacing between word and image */
            width: 100%; /* Fixed width for the word */
            displays: inline-block; /* Make span behave like a block element */
            color: lightyellow; 
            font-size: 40px; 
            font-family: 'Nunito', cursive; 
            font-weight: normal; 
            text-align: center;
            background-color: #01099e;
            border: 2px solid lightyellow;
            border-radius: 10px;
        }        
        """

    # Display HTML and CSS
    st.markdown(html_code, unsafe_allow_html=True)
    st.write('<style>{}</style>'.format(css_style), unsafe_allow_html=True)


