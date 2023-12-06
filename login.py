import streamlit as st
import webbrowser
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

oauth_url = 'INTEGRATION URL FROM BLACK BOX ON WEBEX DEV PORTAL + scope=openid%20email'


st.title("Login With Webex")

result = st.button("Login With Webex")

if (result) :
        webbrowser.open_new_tab(oauth_url)


