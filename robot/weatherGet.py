# encoding:UTF-8
import urllib
import urllib.request
import json


def getJsonFromHttp():
    data = {"location": "auto_ip", "key": "b2e77245d3424482ad0984ccb82f4b99"}
    url_param = urllib.parse.urlencode(data)
    url = "https://free-api.heweather.net/s6/weather?"
    url += url_param
    request_data = urllib.request.urlopen(url).read()
    record = request_data.decode('UTF-8')
    return record

def parseJson(json_str):
    json_direct = json.loads(json_str)
    # 遍历字典
    for (k, v) in json_direct.items():
        # 输出第一层级 v[0] 为数据内容 没有v[1]
        content_str = v[0]
        if content_str["status"] == "ok":
            return content_str
        return ""

def parseJsonMsg(json_str):
    json_direct = json.loads(json_str)
    # 遍历字典
    for (k, v) in json_direct.items():
        # 输出第一层级 v[0] 为数据内容 没有v[1]
        content_str = v[0]
        if content_str["status"] == "ok":
            msg = content_str['basic']['location']
            msg += content_str['now']['cond_txt']
        return ""



def get_weather_data():
    return parseJson(getJsonFromHttp())

# def get_weather_msg():
#     data = parseJson(getJsonFromHttp())
#     msg = data['basic']['location']
#     msg += data['now']['cond_txt']
#     msg = data['now']['cond_txt'] + "室外"+ data['now']['hum'] + data['now']['wind_dir']}}{{data['now']['wind_spd']
