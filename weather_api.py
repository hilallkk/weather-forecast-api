import requests
import json

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

city=input("City:")
api_key="9f67c911d44c05cd9c3b7956ca81a43b"
url_1="https://api.openweathermap.org/data/2.5/weather?q="
url= url_1 + city + "&appid=" + api_key
data = requests.get(url)
response = data.json()


if(response["cod"] == "404"):
    city=input("Error!\nCity:")

else :
    temp = round((response['main']['temp']-273.15),2) #kelvini celcius a çevirip tam sayıya yuvarladım
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    print('Temperature:',temp,'°C')
    print('Humidity: ',humidity,'%')
    print('Description:',description)

    


