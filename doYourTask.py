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

def checkCovidStatistics(query):
    type = query.split(" ")[-2]
    place = query.split(" ")[-1]
    if type == "województwo":
        get_req = f"https://koronawirus-api.herokuapp.com/api/covid19/province/{place}"
    elif type == "powiat":
        get_req = f"https://koronawirus-api.herokuapp.com/api/covid19/district/{place}"
    else:
        get_req = f"https://koronawirus-api.herokuapp.com/api/covid19/daily"
        type = "kraj"
        
    try:
        req = requests.get(get_req)
    except Exception as e:
        textToRead = "Przykro mi. Nie znalazłem tego o co prosisz."
    else:
        req_json = req.json()
        if type == "kraj":
            total_inf = req_json["general"]["infections"]
            new_inf = req_json["today"]["newInfections"]
            textToRead = f"jest {new_inf} nowych zakażeń, łącznie {total_inf} w całym kraju"
        elif type == "województwo":
            total_inf = req_json["general"]["infections"]
            new_inf = req_json["today"]["infections"]
            textToRead = f"jest {new_inf} nowych zakażeń, łącznie {total_inf} w tym województwie"
        else:
            new_inf = req_json["today"]["infections"]
            textToRead = f"jest {new_inf} nowych zakażeń w tym powiecie"
    finally:
        return textToRead


def checkTrendingMovies(query):
    api_key = "83a86d449fabecb4b0d43f0f19cf3ec9"
    
    if "filmów" in query: type = "movie"
    elif "seriali" in query: type = "tv"
    
    try:
        req = requests.get(f"https://api.themoviedb.org/3/trending/{type}/day?api_key={api_key}")
    except Exception as e:
        textToRead = "Przykro mi. Nie znalazłem tego czego o co prosisz."
    else:
        req_json = req.json()
        name = "original_title" if type == "movie" else "original_name"
        list_of_top = [film.get(name) for film in req_json.get("results")]
        textToRead = "; ".join(list_of_top)
    finally:
        return textToRead