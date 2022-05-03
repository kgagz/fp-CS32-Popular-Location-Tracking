"""
    final_analysis.py forms the main part of my final project. It consists of the main function - main()
    which takes the ip addresses, converts them into latitude and longitude coordinates, processes these
    coordinates to find the location with the most ip addresses within 100m of each other, converts 
    these latitude and longitude coordinates into addresses, and then outputs these most popular street
    locations along with their corresponding coordinates and the number of "people" at these locations.
"""

from codecs import Codec
from http.client import UnimplementedFileMode
from sqlite3 import ProgrammingError
import analyze_library
import statistics
from urllib.request import urlopen
import requests
import json
import csv

def build_lists(dictionary):
    """converts dictionary of coordinates into two lists: one for latitude coordinates and one
        for longitude coordinates
    """
    lat = []
    long= []
    for i in range(len(dictionary)):
        lat.append(dictionary[i].get('lat'))
        long.append(dictionary[i].get('long'))
    return lat, long

def build_test_data():
    """
    makes a dictionary of example latitude and longitude coordinates for testing
    """
    coordinates = {}
    coordinates[0] = {
                'lat': 42.371262,
                'long': -71.119200,
            }
    coordinates[1] = {
                'lat': 42.371048,
                'long': -71.118498,
            }
    coordinates[2] = {
                'lat': 42.372018,
                'long': -71.119854,
            }
    coordinates[3] = {
                'lat': 42.371303,
                'long': -71.119283,
            }
    coordinates[4] = {
                'lat': 42.367431,
                'long': -71.127225,
            }
    coordinates[5] = {
                'lat': 42.378337,
                'long': -71.126882,
            }
    coordinates[6] = {
                'lat': 42.379212,
                'long': -71.120087,
            }
    coordinates[7] = {
                'lat': 42.376036,
                'long': -71.235417,
            }
    coordinates[8] = {
                'lat': 42.375791,
                'long': -71.235701,
            }
    coordinates[9] = {
                'lat': 42.375949,
                'long': -71.235487,
            }
    return coordinates

def check_dict(value, dictionary):
    '''checks for a value in a given dictionary. If found, returns the key of the dictionary with that 
        value
    '''
    for i in dictionary:
        list = dictionary[i]
        for r in list:
            if value == r:
                return i
    return None

def coordinates_to_address(lat, long):
    '''
    converts latitude and longitude coordinates into street addresses using OpenStreetMap API
    '''
    params = {'apiKey': '314ac72df3a44ef69df0b93db4613090', 'lat': str(lat), 'lon': str(long),'format':'geocodejson'}
    url = 'https://nominatim.openstreetmap.org/reverse?lat=32.5997&lon=-92.0682&'
    response = requests.get(url, params=params).json()

    #strips off excess details to get only the street address
    address = response.get('features')
    address2 = address[0]
    address3 = address2.get('properties')
    address4 = address3.get('geocoding')
    real_address = address4.get('label')
    return real_address

def get_ip():
    '''
    get_ip finds the public ip address of the device where the code is run
    '''
    public_ip = urlopen('https://ident.me').read().decode('utf8')
    return public_ip


def ip_to_coordinates(ip):
    '''
    converts ip addresses to latitude and longitude coordinates using ipwho.is API
    '''
    params = {'ip': ip}
    url = 'http://ipwho.is/'
    response = requests.get(url, params=params).json()
    lat = response.get('latitude')
    long = response.get('longitude')
    return lat, long

def load_test_data(file):
    '''
    loads csv file of ip addressses to be used as example data
    '''
    coordinates = {}
    counter = 0
    str = 'C:\\Users\\Kathryn\\Desktop\\fp\\' + file
    with open(f'{str}', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ip = row['ip']
            lat, long = ip_to_coordinates(ip)
            coordinates[counter] = {
                'lat': lat,
                'long': long,
            }
            counter += 1
    return coordinates

def main():
    '''
    main() connects all of the previous functions and forms the main part of our final project.
    It takes a dictionary of coordinates, analyzes it to find the location with the most "users"
    within 100m of each other, and outputs these coordinates and their corresponding street addresses
    and number of users.
    '''

    #choose to use the example data from either load_test_data('test.csv'), load_test_data('test2.csv'),
    # or build_test_data

    coordinates = load_test_data('test.csv')
    #coordinates = load_test_data('test2.csv')
    #coordinates = build_test_data()

    #build lists of latitude and longitude coordinates from dictionary of coordinates
    lat, long = build_lists(coordinates)
    
    #begin processing the coordinates

    #initiates loc as a dictionary of the latitudes of popular locations and their number of users
    loc = {}

    #initiates pt as an exact copy of lat, which will function as our frontier
    pt = lat[:]

    #creates explored dictionary, which associates latitude coordinates with other latitude coordinates
    # close to them to check for overlaps
    explored = {}
    while len(pt) != 0:

        # initiates list as list of coordinates to be associated with one latitude coordinate in the 
        # explored dictionary
        list = []
        for i in range(len(pt)-1):
            #use distance formula between two coordinates
            result= ((((pt[i+1] - pt[0])**2) + ((long[i+1]-long[0])**2) )**0.5)

            #key is latitude coordinate of location being currently explored
            key = pt[0]

            #checks if distance is less than or equal to 100m (aka .0009 degrees)
            if result <= .0009 and result != 0:

                #associate pt[i+1] with key for explored dictionary
                list.append(pt[i+1])

                #checks explored dictionary to see if this location overlaps with others
                overlap = analyze_library.check_dict(pt[0], explored)
                if overlap != None:

                    #checks to see if overlap location is also within 100m of key
                    result2= ((((overlap - key)**2) + ((long[lat.index(overlap)] - long[lat.index(key)])**2) )**0.5)
                    if result2 <= .0009 and result != 0:
                        #adds 1 to the number of users in loc list for overlap location
                        loc[overlap] += 1
                elif key in loc:
                    #if key is already in list, increase its numnber of users by 1
                    loc[key] += 1
                else:
                    #if key not in list, create entry at key location equal to 1 user
                    loc[key] = 1

            #checks if two locations are identical
            elif result == 0:
                list.append(pt[i+1])
                overlap = analyze_library.check_dict(pt[0], explored)
                if overlap == None:
                    if key in loc:
                        loc[key] += 1
                    else:
                        loc[key] = 1

        #associates list of explored values with explored location in dictionary
        explored[key] = list
        #moves onto next location to explore
        pt.pop(0)                
   
    fin_lat = []

    #adds locations with maximum number of users to final latitude list
    fin_lat.append(max(loc, key=loc.get))
  
    #checks to make sure there are no other locations with the same number of users because max
    #returns the first item if there is a tie. If there are other locations with the same number of 
    #users, this code will add these locations to the final latitude list
    copy = dict(loc)
    copy_last = max(loc, key=loc.get)
    while len(copy) > 1:
        copy.pop(copy_last)
        copy_max = max(copy, key=copy.get)
        if copy[copy_max] == loc[copy_last]:
            fin_lat.append(copy_max)
            copy_last = copy_max
        else:
            break
    
    #makes dictionary of final coordinates
    fin_coordinates = {}
    for s in range(len(fin_lat)):
        fin_long = long[lat.index(fin_lat[s])]
        fin_coordinates[s] = {
            'lat' : fin_lat[s],
            'long' : fin_long
            }   

    #converts fin_coordinates to printed latitude and longitude coordinates, number of users, and 
    # street addresses
    for t in range(len(fin_coordinates)):
        lat = fin_coordinates[t].get('lat')
        long = fin_coordinates[t].get('long')
        result = analyze_library.coordinates_to_address(lat, long)
        print(f"{loc[lat]+1} people at ({lat}, {long})")
        print(f'Street Address is {result} \n')

if __name__ == '__main__':
    main()