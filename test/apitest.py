import requests
link = 'https://www.datakick.org/api/items/'
code = '00000000000000'
response = requests.get(link+code)
data = response.json()
print(data)
