# fp
Final Project for CS32 - Popular Location Tracking

Author: Kathryn Gagnon

##
Update: 05/03/22
    
Brief Overview

    My final project tracks and analyzes multiple locations using ip addresses in order to find the location with the
    most "users" within 100 meters of each other.

Index of Files
  
  1.) final_analysis.py- main script of my final project
          
          - takes ip addresses, converts them into latitude and longitude coordinates, processes these
    coordinates to find the location with the most ip addresses within 100m of each other, converts 
    these latitude and longitude coordinates into addresses, and then outputs these most popular street
    locations along with their corresponding coordinates and the number of "people" at these locations
    
  2.) server.py - server aspect of the networking part of my final project
  
        - collects the ip addresses sent from the users, collects them into a list, and creates a csv file of ip addresses.
        
   3.) client.py - client aspect of the networking part of my final project
   
         - finds the users ip address using https://ident.me API, and then sends that ip address to the server
  

Future Functionality

      If I had more time, I would have adapted my code to a larger context in three main ways.
      
            1.) I would have created a network that can connect iphones to the main server run on my computer so that I can
                more easily track locations. 
                
            2.) I would have researched better, more accurate ways to track user location. IP addresses do not yield the most 
                accurate location tracking results, although this may also be a result of the poor service that free APIs offer.
                
            3.) I would have incorporated a way to display the results in a more visual manner, such as on a map.

Example:

    ##Input - csv file with ip addresses:
    ip
    65.112.8.60
    65.112.8.20
    18.2.146.20
    65.112.8.137
    65.112.8.138
    18.58.2.158
    18.58.2.129
    18.58.2.65
    18.58.2.65
    18.58.2.65


    ##Output
    5 people at (42.3736158, -71.1097335)
    Street Address is Cambridge Rindge & Latin School, Felton Street, Agassiz, Cambridge, 
    Middlesex County, Massachusetts, 02138-3824, United States 

    5 people at (41.8781136, -87.6297982)
    Street Address is 314, South Federal Street, Printer's Row, Loop, Chicago, Cook County, 
    Illinois, 60604, United States

Credits
  
    Reverse geocoding: https://www.natasshaselvaraj.com/a-step-by-step-guide-on-geocoding-in-python/
    Socket networking: https://alto-palo.com/blogs/connect-two-computers-using-secure-socket-programming-in
    -python/#:~:text=%20Connect%20Two%20Computers%20Using%20Secure%20Socket%20Programming,For%20a%20client%2
     0process%2C%20you%20need...%20More%20
##
Update: 04/24/22

      What I've done so far:
        1.) code that takes in longitude and latitude coordinates and outputs corresponding street addresses
        2.) data processing code that takes in latitude and longitude coordinates and outputs the location with the 
            most users within 100m of that location
        3.)code that gives a user’s ip address
        
      What I have left to do:
        1.) create networking part
        2.) code that converts ip addresses to latitude and longitude coordinates
        3.) link all my different pieces and parts of code together
        

  ###
Update: 04/10/22

    Goals:
  
        1.) convert ip addresses of multiple users into a data structure that maps 
        ip addresses to latitude and longitude coordinates (and maybe street addresses, too?)
  
        2.) find mean or mode of latitude/longitude coordinates to find most popular locations
  
        3.) convert most popular coordinate locations to most popular street addresses

    Timeline:
    
        By 04/17/22- write code to calculate the most popular locations from latitude/longitude
        coordinates (data processing)
        
        By 04/24/22- write code to take ip addresses from multiple users at once, convert to 
        latitude and longitude coordinates, and collate into data structure
        
        By 05/01/22- write code to convert output popular coordinate locations to most popular street addresses
          - connect all of the code
 ##         
Update 03/27/22:
    Computational Subtask for Project: Track and store locational data, use to create statistics

    I will be tracking the locations of multiple users over time and using these locations to find the most popular locations.

    Parts of this task:
       -how to access the locations of different users
       -storing the locations of these users
       -calculating statistics of these user locations (mode?)
