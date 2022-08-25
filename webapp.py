import streamlit as st
# import time
import sys
from streamlit import cli as stcli

col1, col2, col3 = st.columns([4, 4, 4])
with col2:
    st.image("./data/mariamites_logo.jpg", width=200)
st.markdown("<h1 style='text-align: center; color: black;'>الكشاف المريمي - إستمارة تسجيل</h1>", unsafe_allow_html=True)

# option = st.sidebar.selectbox('Make Your Choice', ['Login', 'StreamLit Documentation'])

# if option == 'Login':
audio_file = open("./data/Santiano.mp3", 'rb')
audio_bytes = audio_file.read()
audio = st.audio(audio_bytes, format='audio/ogg')
first_name = st.text_input("First Name", max_chars=20)
last_name = st.text_input("Last Name", max_chars=20)
c1, c2 = st.columns(2)
totem = c1.text_input("Totem", max_chars=25)
selection = c2.radio("Gender", ("Male", "Female"))
col1, col2 = st.columns(2)
age = col1.slider("Years as a Scout", max_value=30, min_value=0, value=1)
date_of_birth = col2.date_input("Date of Birth")
password = st.text_input("Enter Your Password", max_chars=18, type='password')

if password != "" and len(password) < 8:
    st.warning('Password must contain more than 8 characters ')
    st.stop()

if password != "":
    if st.button(label="Submit"):
        st.success("Your form has been submitted Successfully")
        st.balloons()
        st.text("You have entered:")
        st.text("Name: " + str(name) + '\n\n' + "Age: " + str(age) + '\n\n' + "Date of Birth: " + str(date_of_birth))

# if option == 'StreamLit Documentation':
#    st.markdown("""<a href="https://docs.streamlit.io/en/stable/">StreamLit Documentation</a>""",
#                unsafe_allow_html=True, )
