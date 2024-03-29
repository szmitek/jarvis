import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import webbrowser
from local_files import open_spotify, open_discord, open_calculator, open_pycharm

import doYourTask

# Voice API and voice engine module
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# welcome function that check the time and greets us politely depending on the time of day
def welcome_function():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 19:
        speak("Dzień dobry ser!")
        # speak("ah shit here we go again")
    else:
        speak("Dobry wieczór ser!")

    speak("Jestem Jarvis. Jak mogę ci pomóc?")


# It takes microphone input from the user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Slucham...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Rozpoznaje...")
        query = r.recognize_google(audio, language='pl')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Proszę powtórz...")
        return "None"
    return query


if __name__ == "__main__":
    welcome_function()
    while True:
        query = takeCommand().lower()
        # function calling to open youtube
        if 'otwórz youtube' in query:
            webbrowser.open("youtube.com")

        elif 'wyszukaj w youtube' in query:
            speak("szukam")
            url = 'https://www.youtube.com/search?q='
            search_url = url + query
            webbrowser.open(search_url)

        # function calling to google
        elif 'otwórz google' in query:
            webbrowser.open("google.com")

        # function that allows you to find specific results for a google search
        elif 'wyszukaj w google' in query:
            speak("szukam")
            url = 'https://www.google.com/search?q='
            search_url = url + query
            webbrowser.open(search_url)

        # function calling to close the program
        if "do widzenia" in query:
            break

        # function calling for a wikipedia search
        #elif "wyszukaj" in query and "wikipedii" in query:
            # składnia: {słowo związane z wyszukiwaniem} {co chcemy wyszukać} na wikipedii
        elif "wikipedii" in query:
            speak(doYourTask.searchInWikipedia(query))

        # function to call a weather forecast
        # prognoza pogody w {miejsce}
        elif "prognoza pogody" in query:
            speak(doYourTask.checkWeatherForecast(query))

        # function calling number of current covid-19 infections
        # {cokolwiek} zakażen covid w
        # województwo {województwo}
        # powiat {powiat}
        # w innym przypadku będą dla całego kraju
        elif "zakażeń covid" in query:
            speak(doYourTask.checkCovidStatistics(query))

        # functions to open local files
        elif 'otwórz python' in query:
            open_pycharm()

        elif 'otwórz spotify' in query:
            open_spotify()

        elif 'otwórz discord' in query:
            open_discord()

        elif 'otwórz kalkulator' in query:
            open_calculator()

        elif "ranking" in query and ("filmów" in query or "seriali" in query):
            speak(doYourTask.checkTrendingMovies(query))
