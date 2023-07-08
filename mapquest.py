import urllib.parse
import requests 
main_api = "https://www.mapquestapi.com/directions/v2/route?"
while True:
    orig = input("Ubicacion Inicial: ")
    if orig == "quit" or orig == "s":
        break
    dest = input("Destino: ")
    if dest == "quit" or dest == "s":
        break

    key = "tSeRkAzLIZFYm6JJKjmI7R2tfdYd6nOE"
    url = main_api + urllib.parse.urlencode ({"key" :key, "from" :orig, "to" :dest}) 
    json_data = requests.get (url) .json ()
    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
        print ("API Status:” + str (json_status) + “= Una llamada de ruta exitosa.\ n")
        print("=============================================")
        print("Direcion desde " + (orig) + " hasta " + (dest))
        print("Duracion de viaje: " + (json_data["route"]["formattedTime"]))
        print ("Millas:" + str ("{:.1f}".format((json_data ["route"] ["distance"]))))
        #print ("Combustible usado (Gal): "+ str (json_data ["route"] ["FuelUsed"]))# Ya no soporta combustible
        print("Kilometros: " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        #print ("Combustible usado (Ltr): + str "((json_data ["route"] ["FuelUsed"])3.78))#

    print("=============================================")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
