import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "0dpINo2OY2Cm1x78wsazzxIGXXnaLE7T"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)

