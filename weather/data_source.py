import requests
from lxml import etree
import re
import urllib.request
from json import loads

_APPID = 48771443
_APPSERET = "h6GrHhrd"

url = f"https://tianqiapi.com/api?version=v6&appid={_APPID}&appsecret={_APPSERET}"


async def get_weather_of_city(city: str) -> str:
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    kw = {"appid": _APPID, "appsecret": _APPSERET, "city": city}

    r = requests.get(url, kw)
    json = r.json()
    print(json)
    result = f"""time: {json["date"]} {json["week"]} {json["update_time"]}
city: {json["city"]}
weather: {json["wea"]}
temperature_now: {json["tem"]}
temperature: {json["tem1"]}~{json["tem2"]}
win: {json["win"]} {json["win_speed"]} {json["win_meter"]}
humidity: {json["humidity"]}
air_level: {json["air_level"]} {json["air_tips"]} 
    """

    return result



