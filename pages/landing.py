import streamlit as st
import requests
import json
import os
import jwt
from settings import SETTINGS

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

clientID = SETTINGS.clientID
secretID = SETTINGS.secretID
redirectURI = SETTINGS.redirectURI


def get_tokens(code):
    print("function : get_tokens()")
    print("code:", code)

    url = "https://webexapis.com/v1/access_token"
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    payload = ("grant_type=authorization_code&client_id={0}&client_secret={1}&"
               "code={2}&redirect_uri={3}&").format(clientID, secretID, code, redirectURI)
    req = requests.post(url=url, data=payload, headers=headers)
    results = json.loads(req.text)

    id_token = results["id_token"]
    st.session_state["access_token"] = results["access_token"]

    st.session_state['id_token'] = id_token

    print("Token stored in session : ", st.session_state['id_token'])
    return


# Function to parse JWT
def parse_jwt(token):
    """
    Parse JWT token

    :param token: JWT token
    :return: Decoded payload
    """
    return jwt.decode(token, options={"verify_signature": False})


def user_info():
    accessToken = st.session_state['access_token']
    url = "https://webexapis.com/v1/userinfo"
    headers = {'accept': 'application/json', 'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + accessToken}
    req = requests.get(url=url, headers=headers)
    print(req)
    results = json.loads(req.text)
    return results


st.write("Landing Page")

if "access_token" not in st.session_state.keys():
    if 'code' in st.experimental_get_query_params():
        code = st.experimental_get_query_params()['code'][0]

        get_tokens(code)

    if 'id_token' in st.session_state.keys():
        claims = parse_jwt(st.session_state['id_token'])
        st.write('claims : ', claims)
        st.write('==================================')
        st.write('user_info : ', user_info())
