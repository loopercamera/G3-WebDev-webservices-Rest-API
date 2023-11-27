import requests

r = requests.get("https://restcountries.com/v3.1/name/switzerland")

if r.status_code == 200:
    data = r.json()
    print(data[0]['name']['common'])
    print(data[0]['capital'][0])


r = requests.get("https://restcountries.com/v3.1/currency/chf")

if r.status_code == 200:
    data = r.json()
    print("Anazahl Länder mit CHF:", len(data))
    print(data[0]['name']['common'])
    print(data[0]['capital'][0])