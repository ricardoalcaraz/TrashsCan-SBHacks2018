import requests
link = 'https://www.datakick.org/api/items/'
code = '0859584007079'
response = requests.get(link+code)
data = response.json()
print(data)
