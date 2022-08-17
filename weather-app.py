import requests
from pprint import *
import matplotlib.pyplot as plt
import numpy as np

places = []
templist = []
lol = []
API_Key = 'f276904f74631c4b0c2a0ae932d44124'
cit = input("How Many cities do you want to compare? ")
for i in range(int(cit)):
    city = input("Enter a city: ")
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
    weather_data = requests.get(base_url).json()
    weather_data.items()
    places.append(city.title())
    lol.append(0.5)
    for key, value in weather_data.items():
        if key == "main":
            temp_pair = value.items()
            for j,k in temp_pair:
                if j == "temp":
                    ctemp = k-273.15
                    print(k-273.15)
                    templist.append(ctemp)

fig, ax = plt.subplots()

ax.scatter(x=places, y=templist, c=lol, s=np.abs(lol)*500)
plt.show()