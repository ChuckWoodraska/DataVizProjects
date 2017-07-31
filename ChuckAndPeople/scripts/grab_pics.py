from instagram.client import InstagramAPI
import requests
import json

access_token = ""
response = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token={}'.format(access_token))
print(response.text)
