'''
    ip_location.py takes an ip address and gives latitude and longitude coordinates. It can also give you street addresses directly. More accurate!

'''
#api = 314ac72df3a44ef69df0b93db4613090
#url = https://api.ipgeolocation.io/ipgeo
import requests
url = 'https://api.ipgeolocation.io/ipgeo'
params = {'apiKey': '314ac72df3a44ef69df0b93db4613090', 'ip': '89.187.177.75'}
r = requests.get(url, params=params).json()

print(r.get('latitude'))
print(r.get('longitude'))
print(r.get('city'))
print(r.get('country_name'))
