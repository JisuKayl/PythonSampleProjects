import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"

key = "0dpINo2OY2Cm1x78wsazzxIGXXnaLE7T"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        #print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")




"""
{'route': {'distance': 38.089, 'hasHighway': True, 'hasUnpaved': False, 'hasAccessRestriction': False, 'options': {'mustAvoidLinkIds': [], 'maxWalkingDistance': -1, 'manmaps': 'true', 'urbanAvoidFactor': -1, 'stateBoundaryDisplay': True, 'cyclingRoadFactor': 1, 'routeType': 'FASTEST', 'countryBoundaryDisplay': True, 'drivingStyle': 2, 'highwayEfficiency': 22, 'narrativeType': 'text', 'routeNumber': 0, 'tryAvoidLinkIds': [], 'generalize': -1, 'returnLinkDirections': False, 'doReverseGeocode': True, 'avoidTripIds': [], 'timeType': 0, 'sideOfStreetDisplay': True, 'filterZoneFactor': -1, 'walkingSpeed': -1, 'useTraffic': False, 'unit': 'M', 'tr 
[output omitted]
>>>
"""
