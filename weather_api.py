import requests
import json
import pandas as pd
import numpy as np 

url="https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"
response = requests.get(url)
weather_data = response.json()

file_path = "data/json/response.json"

#open json file 
with open(file_path, "w") as json_file:
#save json file 
    json.dump(weather_data, json_file, indent=4)  

print(f"JSON data saved to {file_path}")


#create  dictionnary filtler wanted columns 
new_weather_data = {"time": weather_data["hourly"]["time"],
                    "temperature": weather_data["hourly"]["temperature_2m"],
    "relative humidity": weather_data["hourly"]["relative_humidity_2m"],
    "precipitation": weather_data["hourly"]["precipitation"],
    "surface pressure": weather_data["hourly"]["surface_pressure"]}
df = pd.DataFrame(new_weather_data)

df.to_csv("data/csv/weather_data_filtered.csv")






