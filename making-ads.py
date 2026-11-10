import requests

met_url = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"

met_data = {
    "q": "George Washington",
    "medium": "Paintings",
}

# no header data no need key or json
# GET request to the API
# find url, data, and header form documentation 
response = requests.get(met_url, data = met_data)
if repsonse.status == 200:
    data = response.json()
    print(data)
else: 
    print("BROKEN")