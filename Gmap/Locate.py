from googleplaces import GooglePlaces, types, lang 
import folium
import requests
import configparser
def KEY():
    configParser = configparser.RawConfigParser()   
    configFilePath = r'Gmap/key.txt'
    configParser.read(configFilePath)
    key = configParser.get('your-config', 'API_KEY')
    return key

API_KEY='AIzaSyBeQ8EMs01Cnt9IHZXwqzUQOVqwra-WPJk'
def GetUserGeoLocation():
    url = 'http://ipinfo.io/json '
    payload = {}
    files = {}
    headers= {}
    
    response = requests.request("GET", url, headers=headers, data = payload, files = files)
    data = response.json()
    list1=data["loc"].split(sep=",")
    return list1
def GetHospitalLocation():  
    # Initialising the GooglePlaces constructor 
    google_places = GooglePlaces(API_KEY) 
    list1=GetUserGeoLocation()
    # call the function nearby search with 
    # the parameters as longitude, latitude, 
    # radius and type of place which needs to be searched of  
    # type HOSPITAL
    query_result = google_places.nearby_search(  
            lat_lng ={'lat': list1[0], 'lng': list1[1]}, 
            radius = 2000,  
            types =[types.TYPE_HOSPITAL]) 
    
    # If any attributions related  
    # with search results print them 
    if query_result.has_attributions: 
        print (query_result.html_attributions) 
    
    latlng=[]
    for place in query_result.places:
        latlng.append([str(place.name),float(place.geo_location['lat']),float(place.geo_location['lng'])]) 
    return latlng 
def main():
    Userloc=GetUserGeoLocation()
    hosname=[]
    # Here we pass coordinates of User  
    # and starting Zoom level = 11 
    my_map2 = folium.Map(location = Userloc, zoom_start = 30) 
    HospitalLoc=GetHospitalLocation()
    #we now obtain a list of hospital names and locations  
    for valu in HospitalLoc:
        #Splitting the hospital name from location
        hosname.append(valu.pop(0))
    # save method of Map object will create a map 
    # Creating multiple Parachute Marker with hospitalname popups   
    folium.Marker(location = Userloc,popup ="You", icon=folium.Icon(color='red',icon_color='white',icon='cloud')).add_to(my_map2) 
    for loc,Hsname in zip(HospitalLoc,hosname):
        folium.Marker(location = loc,popup =Hsname,draggable=True).add_to(my_map2) 
        
        # save as html 

    html=my_map2.get_root().render()
    my_map2.save("Hospitals.html")

if __name__ == "__main__":
    main()