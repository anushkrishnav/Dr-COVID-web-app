import requests
import json
def GetUserGeoLocation():
    url = 'http://ipinfo.io/json '
    payload = {}
    files = {}
    headers= {}
    
    response = requests.request("GET", url, headers=headers, data = payload, files = files)
    data = response.json()
    list1=data["loc"].split(sep=",")
    return list1

GetUserGeoLocation()