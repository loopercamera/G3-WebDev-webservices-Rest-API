import requests

def geocde (adress):
    url = "https://nominatim.openstresstmap.org/search"

    querry_parameter = {
        "q": adress,
        "format": "json"
    }

    headers = {
        "User-Agent" : "FHNW Webrowser V1.1 TIM TEST"
    }

    r = requests.get(url,params=querry_parameter,headers=headers)

    if r.status_code == 200:
        data = r.json()
        return data
    else:
        print(f"Fehler!!")

resultat = geocde("Hofackerstrasse 30, 4132 Muttenz, Schweiz")
print(resultat)