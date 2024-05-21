# Python Weather Comparison App

This Python application allows users to compare the current temperature of multiple cities using the OpenWeatherMap API. The app provides a simple command-line interface to input the cities and visualize their temperatures on a scatter plot.

![image](https://github.com/MankaranRooprai/weather-app/assets/13322471/408d5a33-095e-4efd-bd2a-224f5ed83ac2)

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/Weather-Comparison-App.git
```

2. Navigate to the project directory:

```
cd Weather-Comparison-App
```

## Usage

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/) by signing up and generating a free API key.

2. Replace the placeholder API key in the `weather.py` file with your own API key:

```
API_Key = 'your_api_key_here'
```

3. Run the script

```
python weather.py
```

4. Follow the prompts to enter the number of cities you want to compare and the names of those cities.

5. The application will retrieve the current temperature for each city and display it in Celsius.

6. Finally, a scatter plot will be generated, visualizing the temperatures of the entered cities.
