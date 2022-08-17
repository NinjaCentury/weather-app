import requests
from pprint import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

places = []
API_Key = 'f276904f74631c4b0c2a0ae932d44124'
cit = input("How Many cities do you want to compare? ")
for i in range(int(cit)):
    city = input("Enter a city: ")
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
    weather_data = requests.get(base_url).json()
    weather_data.items()
    for key, value in weather_data.items():
        if key == "main":
            #print(value.split())
            temp_pair = value.items()
            for j,k in temp_pair:
                if j == "temp":
                    print(k-273.15)
            #print(value)
    #places.append(city)

# city = input("Enter a city: ")

# base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

# weather_data = requests.get(base_url).json()

#pprint(weather_data)

#print(weather_data.items())



# window = tk.Tk()
# window.mainloop()
# greeting = tk.Label(text="Hello, Tkinter")
# greeting.pack()