import requests
from pprint import *
import matplotlib.pyplot as plt
import numpy as np

#initialize lists
places = []
templist = []
scale = []

API_Key = 'f276904f74631c4b0c2a0ae932d44124'

num_cities = input("How many cities do you want to compare? ")

#run the loop through however many cities user wants
for i in range(int(num_cities)):
    city = input("Enter a city: ")
    #url used for requests
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
    #store data as a dictionary in json
    weather_data = requests.get(base_url).json()
    #separate the key-value (KV) pairs
    weather_data.items()
    places.append(city.title())
    scale.append(0.5)
    
    #finds the temperature for the given city
    for key, value in weather_data.items():
        if key == "main":
            #value of main is a dictionary so separate into KV pairs
            temp_pair = value.items()
            #finds temperature associated with the city
            for temp,kelvin in temp_pair:
                if temp == "temp":
                    #convert temp from kelvin to celcius
                    ctemp = kelvin-273.15
                    print(ctemp)
                    templist.append(ctemp)

#create subplots
fig, ax = plt.subplots()

#create and display scatter plot using previous lists
ax.scatter(x=places, y=templist, c=scale, s=np.abs(scale)*500)
plt.show()
