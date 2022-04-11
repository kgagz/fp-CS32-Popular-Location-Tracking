'''
    WORKING!
    reverse_geocoding.py takes latitude and longitude coordinates and outputs street address. Not the most accurate acoording to api provider details.

'''

import requests
#https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>
params = {'apiKey': '314ac72df3a44ef69df0b93db4613090', 'lat': '40.71455', 'lon': '-74.00714','format':'geocodejson'}
url = 'https://nominatim.openstreetmap.org/reverse?lat=32.5997&lon=-92.0682&'
response = requests.get(url, params=params).json()
#print(response.status_code)
address = response.get('features')
#print(address)
address2 = address[0]
#print(address2)
#print(type(address2))
address3 = address2.get('properties')
#print(address3)
#print(type(address3))
address4 = address3.get('geocoding')
#print(address4)
#print(type(address4))
real_address = address4.get('label')
print(real_address)
