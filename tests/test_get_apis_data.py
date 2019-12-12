from get_apis_data import get_pollution_data, get_thryve_data, get_weather_data
import os

latitude = 52.497139
longitude = 13.453778


# print(get_pollution_data(city="Berlin"))
# print(get_pollution_data(location={"lat":latitude,"long":longitude}))
# print(get_thryve_data(os.path.abspath(os.path.join(os.getcwd(),"data/activity_4325638680.csv"))).head())
print(get_weather_data(location = {"lat":latitude,"long":longitude}))