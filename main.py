def weather_forecasting():
  import datetime
  import requests 
  import pytz
  import os
  def clear():
    os.system('clear')
  API_KEY = os.environ['API_KEY']
  while True:
    city = input('City\n>')
    ws = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric').json()
    if ws['cod'] != 200:
      clear()
      input(f'The city you entered "{city}" does not exist.')
      clear()
    else:
      break
  city = f'{city[0].upper()}{city[1:]}'
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
  elif w == 'haze':
    w = 'It is hazy'
  wm = ws['main']
  temp = wm['temp']
  feels_like = wm['feels_like']
  p = wm['pressure']
  pressure = f'{p} hPa'
  hum = wm['humidity']
  humidity = f'{hum}%'
  del hum
  v = str(int(ws['visibility'])/1000)
  visib = f'{v} out of 10'
  w_s = str(ws['wind']['speed']*0.06)
  wind_speed = f'{w_s} kilometers/hour'
  del w_s
  w_d = ws['wind']['deg']
  wind_deg = f'{w_d}°'
  c = ws['clouds']['all']
  cloudiness = f'{c}%'
  del c
  sys = ws['sys']
  def convert(_):
    _ = str(datetime.datetime.fromtimestamp(_).astimezone(pytz.timezone('GMT')))
    return _[11:19]
  dt = convert(ws['dt'])
  country = sys['country']
  sunrise = convert(sys['sunrise'])
  sunset = convert(sys['sunset'])
  t = ws['timezone']/3600
  if t > 0.0:
    t = f'+ {t}'
  else:
    t = f'- {t/-1}'
  timezone = f'GMT {t} hours'
  del t
  clear()
  return f'''{city}, {country}'s Forecast as of {dt} GMT:\n{w}.\nTemperature: {temp} °C\nFeels like temperature: {feels_like} °C\nPressure: {pressure}\nHumidity: {humidity}\nVisisbility: {visib}\nWind Speed: {wind_speed}\nWind Direction: {wind_deg}\nCloudiness: {cloudiness}\nTimezone: {timezone}\nSunrise: {sunrise} GMT\nSunset: {sunset} GMT'''

print(weather_forecasting())
