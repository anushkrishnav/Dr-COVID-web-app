import requests

url = "https://covid-19-india-data-by-zt.p.rapidapi.com/GetIndiaStateWiseData"

headers = {
    'x-rapidapi-host': "covid-19-india-data-by-zt.p.rapidapi.com",
    'x-rapidapi-key': "5139db90a1msh0317f26ee12fd8ap1f9d71jsne25be33a7910"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)