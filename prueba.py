import requests

URL = "http://www.omdbapi.com/?i=tt3896198&apikey=d86b620b"

peli = input("Buscar: ")

respuesta = requests.get(URL.format(peli))

mijson = respuesta.json()

print(mijson.get("Search")[0].get("Title"))
print(mijson.get("Search")[0].get("Poster"))