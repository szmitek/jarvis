# J.A.R.V.I.S.
J.A.R.V.I.S. is a voice assistant program that can perform a variety of tasks, such as searching the web, providing weather forecasts, and retrieving COVID-19 statistics. It uses Text-to-Speech (TTS) and Speech Recognition (SR) to communicate with the user.

# Features
Greet the user and provide a brief introduction to the program
Accept voice commands and perform actions based on the commands
Open websites, such as YouTube and Google, in the default web browser
Search Wikipedia and provide a summary of the results
Provide a weather forecast for a specified location
Retrieve COVID-19 statistics for a specified location or the entire country
Retrieve the names of trending movies or TV shows
Retrieve the top headlines from a specified news source
Open local programs, such as PyCharm, Discord, the calculator, and Spotify
# Requirements
* Python 3.7 or later
* The following Python libraries:
  * pyttsx3
  * speech_recognition
  * wikipedia
  * requests
* An API key for OpenWeatherMap and TheMovieDB (optional)
# Usage
1. Clone or download this repository
2. Install the required libraries: pip install -r requirements.txt
3. (Optional) Obtain API keys for OpenWeatherMap and TheMovieDB and place them in local_files.py
4. Modify the file paths in local_files.py to match the paths to the programs on your computer
5. Run the jarvis.py script: python jarvis.py
Commands
* "otwórz youtube" (open YouTube)
* "wyszukaj w youtube" (search YouTube)
* "otwórz google" (open Google)
* "wyszukaj w google" (search Google)
* "wyszukaj {query} na wikipedii" (search Wikipedia)
* "prognoza pogody w {city}" (get weather forecast for a city)
* "liczba zakażeń covid w {region}" (get COVID-19 statistics for a region)
* "top {number} filmów" (get the top trending movies)
* "top {number} seriali" (get the top trending TV shows)
* "top wiadomości z {source}" (get the top headlines from a news source)
* "otwórz python" (open PyCharm)
* "otwórz discord" (open Discord)
* "otwórz kalkulator" (open the calculator)
* "otwórz spotify" (open Spotify)
* "do widzenia" (goodbye)
# Notes
* The program may not recognize all commands accurately, especially if there is background noise or if the user's speech is not clear. In such cases, the user may need to repeat the command.
* The program is currently set to use the Polish language for TTS and SR. To use a different language, modify the language parameter in the r.recognize_google call in jarvis.py and the wikipedia.set_lang call in local_files
