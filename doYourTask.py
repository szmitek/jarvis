import re
from unittest import result
import wikipedia #pip install wikipedia
import requests

def searchInWikipedia(query):
    wikipedia.set_lang("pl")
    listWikiQuery = query.split(" ")[1:-2]
    stringWikiQuery = " ".join(listWikiQuery)
    try:
        textToRead = wikipedia.summary(stringWikiQuery, sentences=2)
    except Exception as e:
        textToRead = "Przykro mi. Nie znalazłem tego czego o co prosisz."
    finally:
        return textToRead

def checkWeatherForecast(query):
    city = query.split(" ")[-1]
    api_key = "76828ae745a0d53168c90ade45ca334d"
    try:
        req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=pl&units=metric&APPID={api_key}")
    except Exception as e:
        textToRead = "Przykro mi. Nie znalazłem tego czego o co prosisz."
    else:
        req_json = req.json()
        description = req_json.get("weather")[0].get("description")
        temperature = req_json.get("main").get("temp")
        textToRead = f"W {city} jest {description} a temperatura wynosi {temperature} stopni Celsjusza"
    finally:
        return textToRead
