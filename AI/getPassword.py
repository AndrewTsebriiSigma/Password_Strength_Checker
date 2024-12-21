from train_model import model, normalizer
import requests

response = requests.get('http://127.0.0.1:5000/api/password')
data = 'lox123'
user_password = {
    'upperCase': 0,
    'Long_Length': 0,
    'letter_count': 0,
    'digit_count': 0,
    'non_repeating': 0,
    'symbol_count': 0
}

# if response.status_code == 200:
#     data = response.json()

def convert_password(password):

    repeated_set = set()

    user_password['upperCase'] = int(any(char.isupper() for char in password))
    user_password['Long_Length'] = int(len(password) > 12)
    user_password['letter_count'] = int(any(char.isalpha() for char in password))
    user_password['digit_count'] = int(any(char.isdigit() for char in password))
    user_password['symbol_count'] = int(any(not char.isalnum() for char in password))

    for char in password:
        if char in repeated_set:
            user_password['non_repeating'] = 1
            break
        repeated_set.add(char)

    return user_password

result = convert_password(data)
print(result)
