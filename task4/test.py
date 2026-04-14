import requests

res = requests.get('http://localhost:5252/api/hello')
print(res.text)
