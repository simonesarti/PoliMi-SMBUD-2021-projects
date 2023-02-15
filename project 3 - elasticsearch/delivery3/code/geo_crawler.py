import requests
import json
import loadbar
import pandas as pd

# worker of the thread
def add_geo(item):
    document, cache, acc, regions = item
    location = document["nome_area"]

    if location in cache.keys():
        document["latitude"] = cache[location][0]
        document["longitude"] = cache[location][1]
    else:
        response = requests.get('https://nominatim.openstreetmap.org/search/' + location +'?format=json').json()
        lat, lon = response[0]["lat"], response[0]["lon"]
        cache[location] = [lat, lon]
        document["latitude"] = lat
        document["longitude"] = lon

    document["region_code"] = regions[location]
    acc.append(document)

# set up the data structures needed for the parallelization
new_data = []

coordinates = {}

codes = {
	"Lombardia":"IT-25",
	"Piemonte":"IT-21",
	"Friuli-Venezia Giulia": "IT-36", 
	"Lazio":"IT-62",
	"Liguria": "IT-42",
	"Marche":"IT-57",
	"Molise": "IT-67", 
	"Provincia Autonoma Bolzano / Bozen": "IT-32",
	"Provincia Autonoma Trento": "IT-32", 
	"Puglia":"IT-75",
	"Sardegna":"IT-88",
	"Sicilia":"IT-82",
	"Toscana": "IT-52",
	"Valle d'Aosta / Vallée d'Aoste":"IT-23",
	"Umbria": "IT-55",
	"Calabria": "IT-78", 
	"Veneto": "IT-34" , 
	"Emilia-Romagna": "IT-45",
	"Basilicata":"IT-77", 
	"Campania": "IT-72", 
	"Abruzzo": "IT-65"
}

file = json.load(open("somministrazioni-vaccini-latest.json"))
data = file["data"]

# parallelization
items = []
for document in data:
    items.append([document, coordinates, new_data, codes])

loadbar.multithread(items, add_geo, 10)

# save the result as a csv
df = pd.DataFrame(new_data)
df.to_csv("result_geo.csv")