import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import doYourTask

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #JAK KTOS USTAWI GLOS JARVISA MA ODEMNIE PIWO ~~ Szmitek
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<19:
        speak("Dzień dobry ser!")
    else:
        speak("Dobry wieczór ser!")

    speak("Jestem Jarvis. Jak mogę ci pomóc?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "bye" in query: break

        if "search" in query and "in wikipedia" in query:
            doYourTask.searchInWikipedia(query)