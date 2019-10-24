import requests
import google.auth.transport.requests
from google.oauth2 import service_account
import firebase_admin
from firebase_admin import db

class Database:
    def __init__(self):
        scopes = ['https://www.googleapis.com/auth/firebase.database', 'https://www.googleapis.com/auth/userinfo.email']

        token_request = service_account.Credentials.from_service_account_file('test-login-page-for-web-app894-firebase-adminsdk-t3m3e-6c4ddb2477.json', scopes=scopes)
        request = google.auth.transport.requests.Request()
        token_request.refresh(request)
        self.token = token_request.token

    def read(self, name):
        endpoint = 'https://test-login-page-for-web-app894.firebaseio.com/{}.json?access_token='.format(name) + self.token

        request = requests.get(endpoint)
        self.read_database = request.json()

    def write(self, uid, key_value_dict:dict):
        # endpoint = 'https://test-login-page-for-web-app894.firebaseio.com/.json?access_token=' + self.token
        credentials = firebase_admin.credentials.Certificate('test-login-page-for-web-app894-firebase-adminsdk-t3m3e-6c4ddb2477.json')
        firebase_db = firebase_admin.initialize_app(credentials, {'databaseURL':'https://test-login-page-for-web-app894.firebaseio.com'})
        ref = db.reference('/')
        create_value = ref.child(str(uid))
        create_value.set(key_value_dict)
