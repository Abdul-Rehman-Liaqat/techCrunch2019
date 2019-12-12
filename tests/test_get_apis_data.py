from get_apis_data import get_pollution_data, get_thryve_data, get_weather_data
import os

print(get_pollution_data(city="Berlin"))
print(get_pollution_data(location={"lat":52.554192,"long":13.344960}))
print(get_thryve_data(os.path.abspath(os.path.join(os.getcwd(),"data/activity_4325638680.csv"))).head())
print(get_weather_data(location = {"lat":52.554192,"long":13.344960}))