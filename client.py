import requests

url = 'http://127.0.0.1:8000/Appraisal', 'http://127.0.0.1:8000/Department', 'http://127.0.0.1:8000/Employee'
headers = {'Authorization': 'Token 49089120c6ef212d941ce8f457f4879a28f1b09a'}
r = requests.get(url, headers=headers)