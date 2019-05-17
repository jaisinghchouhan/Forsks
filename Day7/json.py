import requests
cty_name=input("enter city name")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+cty_name
url3 = "&appid=20617b20416c1dd202ec669812ae60b6"
url=url1+url2+url3
response = requests.get(url)
response.content
jsondata = response.json()
print("longitude :",jsondata['coord']['lon'])
print("longitude :",jsondata['coord']['lat'])
print("weathe condition :",jsondata['weather'][0]['main'])
print("wind speed :",jsondata['wind']['speed'])
print("sunrise :",jsondata['sys']['sunrise'])
print("sunset :",jsondata['sys']['sunset'])


