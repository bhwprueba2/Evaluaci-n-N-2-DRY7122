import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "BQMimJJPRskM7rCtFSMok7rRL5H2uMEs"

while True:
   orig = input("Ciudad de origen: ")
   if orig == "quit" or orig == "q":
    break
   dest = input("Ciudad de destino: ")
   if orig == "quit" or orig == "q":
    break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("=============================================")
       print("Directions from " + (orig) + " to " + (dest))
       print("Duracion del viaje: " + (json_data["route"] ["formattedTime"]))
       print("Kilometros:" + str ("{:.2f}" .format((json_data ["route"] ["distance"]) *1.61)))
       print("Combustible usado (Ltr):32")
       print("=============================================")
    for each in json_data ["route"] ["legs"] [0] ["manoeuvres"]: 
       print (each ["narrative"]) + "(" + str ("{:.2f}" .format (((each ["distancia"]) *1.61) + "km)"))
       print ("=====================================================\ n")

 

