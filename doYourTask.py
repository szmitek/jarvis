from unittest import result
import wikipedia #pip install wikipedia
import requests

def searchInWikipedia(query):
    listWikiQuery = query.split(" ")[1:-2]
    stringWikiQuery = " ".join(listWikiQuery)
    try:
        results = wikipedia.summary(stringWikiQuery, sentences=2)
    except Exception as e:
        results = "sorry! i couldn't find anything"
    finally:
        return results

def checkWeatherForecast(query):
    city = query[-1]
    api_key = "76828ae745a0d53168c90ade45ca334d"
    req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city},yourCountryCode&APPID={api_key}")
    if req == 404:
        results = "Przepraszam! Nie znalazłem prognozy pogody dla tego miasta"
    else:
        results = req.json()
    return results
