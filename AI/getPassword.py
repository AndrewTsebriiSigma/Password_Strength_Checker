from train_model import model, normalizer
import requests

response = requests.get('http://127.0.0.1:5000/api/password')
data = ''
user_password = {
    'upperCase': 0,
    'Long_Length': 0,
    'letter_count': 0,
    'digit_count': 0,
    'non_repeating': 0,
    'symbol_count': 0
}

if response.status_code == 200:
    data = response.json()

def convert_password(password):
    repeated_set = ()

    if any(char.isUpper() for char in password):
        list(user_password.items)[0] = 1
    if (len(user_password) > 12):
        list(user_password.items)[1] = 1
    if any(char.isalpha() for char in password):
        list(user_password.items)[2] = 1
    if any(char.isdigit() for char in password):
        list(user_password.items)[3] = 1
    for i in repeated_set:
        if i in repeated_set:
            list(user_password.items)[4] = 1
            break
        repeated_set.add(i)
    if any(not char.isalnum() for char in password):
        list(user_password.items)[5] = 1
convert_password(data)