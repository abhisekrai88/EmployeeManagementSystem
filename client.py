import requests

url = 'http://127.0.0.1:8000/Appraisal', 'http://127.0.0.1:8000/Department', 'http://127.0.0.1:8000/Employee'
headers = {'Authorization': 'Token b17142ba437ce4ba9356e7649ce395ae47bef372'}
r = requests.get(url, headers=headers)