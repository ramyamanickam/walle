import pyowm

owm = pyowm.OWM('c97a50329ac666229f8a0d85dc11a95b')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
##forecast = owm.daily_forecast("Milan,it")
#tomorrow = pyowm.timeutils.tomorrow()
#forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
def welcome_weather(city):
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    status = w.get_detailed_status()
    temperature = w.get_temperature('celsius')
    weather_data = {'status' : status, "temperature" : str(temperature.get('temp_max'))}
    return weather_data

#fc=owm.three_hours_forecast(city)

#if(fc.will_have_sun() == True):
#    print('It will be sunny')               
                
#if(fc.will_have_snow() == True):
#    print('It will snow today')                 # <Weather - reference time=2013-12-18 09:20, 

#f = fc.get_forecast()
#for weather in f:
#      print (weather.get_status())

#print(fc.when_rain())
# status=Clouds>

# Weather details
#w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#w.get_humidity()              # 87
#w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of 
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)