
class SETTINGS:
    # Enter your clientID/secretID that you received from developer.webex.com when you created your integration
    clientID = "Cc835750c4c27674c9670f34b452ec3d72a38bd3262f41a0c9fd3bfad72ab28a1"
    secretID = "74a4dc1a6cdd2e057b7fc8bb17ba137503976bdfe9c12b8e2014d6b5bb119cbb"
    # Enter your redirectURL for where users should be redirected to after successful Webex Authentication
    redirectURI = "http://localhost:8501/landing"
    # No CHANGES NEEDED BELOW
    oauth_url = f'https://webexapis.com/v1/authorize?client_id={clientID}&response_type=code&redirect_uri={redirectURI}&scope=openid%20email'
