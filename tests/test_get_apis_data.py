from get_apis_data import get_pollution_data
import os

print(get_pollution_data(city="Berlin"))
print(get_pollution_data(location={"lat":52.554192,"long":13.344960}))


