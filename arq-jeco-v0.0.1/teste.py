
import requests

response = requests.get(
    'http://127.0.0.1:5000/register',
    data = {
        'email': 'jejeco75@gmail.com',
        'password': 'mengao6x1vasco'
    }
)

print(
    response.json()
)