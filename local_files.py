# file to load programs that are on your pc
# change routes to work
import os

paths = {
    'pycharm': "D:\\Program Files\\JetBrains\\PyCharm 2021.3.3\\bin\\pycharm64.exe",
    'discord': "C:\\Users\\Kamil\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'spotify': "C:\\Users\\Kamil\\AppData\\Roaming\\Spotify\\Spotify.exe",

}


def open_pycharm():
    os.startfile(paths['pycharm'])


def open_discord():
    os.startfile(paths['discord'])


def open_calculator():
    os.startfile(paths['calculator'])


def open_spotify():
    os.startfile(paths['spotify'])
