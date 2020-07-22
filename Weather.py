import pyowm
from pyowm.weatherapi25 import observation

owm = pyowm.OWM('7b7d3f95a0dd4fcaa6bc430cb78f2a10')  # You MUST provide a valid API key


class Weather:
    def __init__(self, city):
        self.c = city
        self.w = (owm.weather_at_place(self.c)).get_weather()
        self.outfit = None
        self.number = None

    city = "Edinburgh,GB"

    def set_outfit(self, ):
        print("1")
        print(self.w.get_temperature('celsius')['temp'])
        if self.w.get_temperature('celsius')['temp'] <= 8:
            self.outfit = "Jacket"
            self.number = 1
        elif 11 < (self.w.get_temperature('celsius')['temp']) < 14:
            self.outfit = "shorts"
            self.number = 2
        else:
            self.outfit = "Shorts and sunglasses"
            self.number = 3

        print(self.number, self.outfit)



