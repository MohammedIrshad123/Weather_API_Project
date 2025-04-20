import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv('API_KEY')
city=input("Please Enter your city:")

api_endpoint="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
def requesttrymethod():    

    api_request=requests.get(api_endpoint)
    api_json_responce=api_request.json() 
    if api_json_responce['cod']=='404':
        print("Invalid city {}, Please Enter the City".format(city))
    else:       
    #create variables to store and display data
        temperature = ((api_json_responce['main']['temp']) - 273.15)
        weather_desc = api_json_responce['weather'][0]['description']
        hmdt = api_json_responce['main']['humidity']
        wind_spd = api_json_responce['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print ("-------------------------------------------------------------")
        print ("Weather Stats for - {}  || {}".format(city.upper(), date_time))
        print ("-------------------------------------------------------------")

        print ("Current temperature is: {:.2f} deg C".format(temperature))
        print ("Current weather desc  :",weather_desc)
        print ("Current Humidity      :",hmdt, '%')
        print ("Current wind speed    :",wind_spd ,'kmph')
 
requesttrymethod()