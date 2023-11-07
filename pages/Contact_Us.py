import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message here")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}"""
    # Special button which is designed to submit the form
    # it belongs to -- is Boolean Type
    button = st.form_submit_button("Submmit")
    print(button)
    if button:
      send_email(message)
      st.info("Your email was sent succesfully")
