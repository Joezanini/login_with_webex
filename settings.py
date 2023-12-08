
class SETTINGS:
    # Enter your clientID/secretID that you received from developer.webex.com when you created your integration
    clientID = "<enter clientID>"
    secretID = "<enter secretId>"
    # Enter your redirectURL for where users should be redirected to after successful Webex Authentication
    redirectURI = "http://localhost:8501/landing"
    # No CHANGES NEEDED BELOW
    oauth_url = f'https://webexapis.com/v1/authorize?client_id={clientID}&response_type=code&redirect_uri={redirectURI}&scope=openid%20email'
