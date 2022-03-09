#!/usr/bin/python3

import requests
import time

lat = float(input("Enter lat: "))
# sea = 47.6
lon = float(input("Enter lon: "))
#sea = -122.3

# define base URL
SEAURL = f"http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}"

def main():

    # Make HTTP GET request 
    seattle = requests.get(f"{SEAURL}")
    seattle = seattle.json()

    for sea in seattle["response"]:

        risetime = sea.get("risetime")
        duration = sea.get("duration")
        print(f"The ISS will be over head at: {time.ctime(risetime)} for {duration} seconds")
    

if __name__ == "__main__":
    main()
