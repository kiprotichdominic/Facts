import os
import requests

def login():
    url = 'http://127.0.0.1:8000/api/rest-auth/login/'
    r = requests.get(url)
    users= r.json()
    return posts 