
from requests_oauthlib import OAuth2Session
import json
from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://github.com/login/oauth/authorize")



client_id = "your_cleint_id"
client_secret="your_client_secret"
redirect_uri="your_redirect_uri"

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

base_auth_url = "https://github.com/login/oauth/authorize"

authorization_url = oauth.authorization_url(base_auth_url)


browser.get(authorization_url[0])

response =input("Enter redirect response")

s = "code"
s2 = '&'
code = response[response.find(s)+5 : response.find(s2)]  

api_url_base = "https://github.com/login/oauth/access_token?client_id="+ client_id+"&client_secret="+ client_secret +"&code="+code


token = oauth.fetch_token(api_url_base, authorization_response=response)  
print(token)


