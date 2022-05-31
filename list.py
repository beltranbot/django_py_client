import requests
from getpass import getpass

def detail_request(token):
    # requires trailing slash here to work
    endpoint = "http://localhost:8000/api/products/" 
    headers = {
        'Authorization': f"Bearer {token}"
    }
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())


def get_token():
    auth_endpoint = "http://localhost:8000/api/auth/"
    username = input('username?: ')
    password = getpass('password?: ')
    data = {
        'username': username,
        'password': password
    }
    auth_response = requests.post(auth_endpoint, json=data)
    if auth_response.status_code == 200:
        token = auth_response.json()['token']
        return token
    print('Wrong credentials.')
    return None

token = get_token()
if token:
    detail_request(token)
