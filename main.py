import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import webbrowser
import googlesearch
import doYourTask

# Voice API and voice engine module
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # JAK KTOS USTAWI GLOS JARVISA MA ODEMNIE PIWO ~~ Szmitek
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# welcome function that check the time and greets us politely depending on the time of day
def welcome_function():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 19:
        speak("Dzień dobry ser!")
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
        elif "wyszukaj" in query and "wikipedii" in query:
            speak(doYourTask.searchInWikipedia(query))


        # function to call a weather forecast
        elif "prognoza pogody" in query:
            speak(doYourTask.checkWeatherForecast(query))


        # function calling number of current covid-19 infections
        elif "zakażeń covid" in query:
            speak(doYourTask.checkCovidStatistics(query))
