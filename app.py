import requests
from typing import Dict, Optional
import os


def get_pollution(city: Optional[str]=None,location: Optional[Dict[str,float]] = None):

    def _append_api_token(url):
        return url + "/?token=" + os.getenv("POLLUTION_API_TOKEN")

    pollution_api_url = "http://api.waqi.info/feed/"
    if location is not None:
        api_path = _append_api_token("geo" + ":" + str(location["lat"]) + ";" + str(location["long"]))
        return requests.get(pollution_api_url + api_path).json()
    elif city is not None:
        api_path = _append_api_token(city)
        return requests.get(pollution_api_url+api_path).json()
    else:
        return None

print(get_pollution(city="Berlin"))
print(get_pollution(location={"lat":52.554192,"long":13.344960}))