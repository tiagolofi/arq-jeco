
import requests
import time
import json

response = requests.post(
    'http://127.0.0.1:5000/register',
    data = {
        'email': 'jejecox75@gmail.com',
        'password': 'mengao7x0vasco',
        'nome': 'Jejeco'
    }
)

response = requests.post(
    'http://127.0.0.1:5000/login',
    data = {
        'email': 'jejecox75@gmail.com',
        'password': 'mengao7x0vasco' 
    }
)

print(
    json.dumps(
        response.json(),
        indent = 2
    )
)