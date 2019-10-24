import requests
from db import Database
import os

def signup(email, password):
    web_api_key = 'api_key'
    signup_endpoint = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=' + web_api_key

    json = {'email':email, 'password':password}
    r = requests.post(signup_endpoint, json=json)
    if r.status_code == 400:
        return [r.status_code, r.json()['error']['message']]
    elif r.status_code == 200:
        id_code = r.json()['localId']
        write_to_db = Database()
        write_to_db.write(id_code, {'key':'test_key'})
        return [r.status_code]

def login(email, password):
    web_api_key = 'api_key'
    login_endpoint = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=' + web_api_key

    json = {'email':email, 'password':password}

    r = requests.post(login_endpoint, json = json)

    if r.status_code == 400:
        return [400, r.json()['error']['message']]
    elif r.status_code == 200:
        return [200, r.json()['idToken']]
    else:
        return ['UNKNOWN']