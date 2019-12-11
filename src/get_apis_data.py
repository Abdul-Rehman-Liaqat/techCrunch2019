import requests
from typing import Dict, Optional
import os
import pandas as pd

def get_pollution_data(city: Optional[str]=None,location: Optional[Dict[str,float]] = None):

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



def get_thryve_data(df_path:str):
    return pd.read_csv(df_path)