#!/bin/python
#  API key https://openweathermap.org/appid
import urllib.request, json

city = "Glasgow"
api_key = "15a5c55de3753396c33db195340fc8b7"
units = "Metric"
unit_key = "C"

weather = eval(str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units={}".format(city, api_key, units)).read())[2:-1])

info = weather["weather"][0]["description"].capitalize()
temp = int(float(weather["main"]["temp"]))
print ("Glasgow")
print("%s, %i °%s" % (info, temp, unit_key))