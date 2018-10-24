"""

Current Implementation : Web FLow

At the authentication page, login with your bitly account and allow the web app. Copy the Redirect URL and paste it when the prompt asks. Then, enter your URL to be shortened. 


There is an alternative way, I believe : 
Access tokens can be directly exchanged for username and password in Bitly API, I have not used this method in this script.


"""

from requests_oauthlib import OAuth2Session
import json



client_id 	= r"your_client_id"
client_secret 	= r"your_client_secret"
redirect_uri 	= "your_redirect_url"
oauth 		= OAuth2Session(client_id, redirect_uri=redirect_uri)

base_auth_url   = "https://bitly.com/oauth/authorize"
token_url       = "https://api-ssl.bitly.com/oauth/access_token"

authorization_url = oauth.authorization_url(base_auth_url)


print("Please authorise and continue - \n")

print(authorization_url[0])



redirect_response = input("\n Paste the redirect URL")  #string

ind = redirect_response.find("&code=") + 6

code = redirect_response[ind:]

api_url_base    = "https://api-ssl.bitly.com/oauth/access_token?client_id=aadbabdf05cf85001538249359cedf3e3ad87235&client_secret=5211d81ade2f88af0ff1d7f21b5b5deb0a1c2e7d&code="+code
token                   = oauth.fetch_token(api_url_base, authorization_response=redirect_response)  #json 

print(token)
long_url = input("Enter your URL: \n")
pydata = {
    "group_guid": "Bial8svtjwM",  #get group guid by sending get request to the guid link mentioned in documentation
    "domain": "bit.ly",   
    "long_url": long_url,
    
    "title": "string",
    
}

data = json.dumps(pydata)  # data is json now

headers = {'Authorization': 'Bearer {token}'}  
r = oauth.post("https://api-ssl.bitly.com/v4/bitlinks", headers = headers, data=data)
     
final = json.loads(r.text)


print("Shortened URL : \n")
print(final['link'])



