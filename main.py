import datetime
import requests 
import pytz
import os
def weather_forecasting():
  API_KEY = os.environ['API_KEY']
  city = input('City\n>')
  city = f'{city[0].upper()}{city[1:]}'
  ws = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric').json()
  wl = ws['weather'][0]
  w = wl['main'].lower()
  if w == 'clouds':
    w = 'It is cloudy'
  elif w == 'clear':
    w = 'There is a clear sky'
  elif w == 'rain':
    w = 'It is raining'
  elif w == 'snow':
    w = 'It is snowing'
  elif w == 'drizzle':
    w = 'It is drizzling'
  elif w == 'thunderstorm':
    w = 'There is a thunderstorm'
  wm = ws['main']
  temp = wm['temp']
  feels_like = wm['feels_like']
  pressure = wm['pressure']
  humidity = wm['humidity']
  visib = str(int(ws['visibility'])/1000)
  w_s = str(ws['wind']['speed']*0.06)
  wind_speed = f'{w_s} kilometers/hour'
  del w_s
  w_d = ws['wind']['deg']
  wind_deg = f'{w_d}°'
  c = ws['clouds']['all']
  cloudiness = f'{c}%'
  del c
  sys = ws['sys']
  gmt = pytz.timezone('GMT')
  def convert(_):
    _ = str(datetime.datetime.fromtimestamp(_).astimezone(gmt))
    return _[11:19]
  country = sys['country']
  sunrise = convert(sys['sunrise'])
  sunset = convert(sys['sunset'])
  t = str(int(ws['timezone'])/3600)
  timezone = f'UTC {t} hours'
  del t
  os.system('clear')
  return f'''{city}, {country}'s Forecast\n{w}.\nTemperature: {temp}\nFeels like temperature: {feels_like}\nPressure: {pressure}\nHumidity: {humidity}\nVisisbility: {visib}\nWind Speed: {wind_speed}\nWind Direction: {wind_deg}\nCloudiness: {cloudiness}\nTimezone: {timezone}\nSunrise (GMT): {sunrise}\nSunset (GMT): {sunset}'''

print(weather_forecasting())