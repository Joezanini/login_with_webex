import streamlit as st
import webbrowser
import os
from settings import SETTINGS

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

oauth_url = SETTINGS.oauth_url

st.title("Login With Webex")

result = st.button("Login With Webex")

if result:
    webbrowser.open_new_tab(oauth_url)
