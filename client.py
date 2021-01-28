import requests

url = 'http://127.0.0.1:8000/Appraisal', 'http://127.0.0.1:8000/Department', 'http://127.0.0.1:8000/Employee'
headers = {'Authorization': 'Token affc9211d5aa93a9e9d069260f54860cbd7637ab'}
r = requests.get(url, headers=headers)