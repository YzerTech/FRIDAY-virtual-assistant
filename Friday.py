import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import random
from requests import get
import requests
import webbrowser
import pywhatkit as kit
import sys
from pyautogui import time
import instadownloader
import instaloader

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 174)


# Friday's text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Voice to text
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold = 3
        audio = listener.listen(source, timeout=1000, phrase_time_limit=100)

    try:
        print("Recognizing...")
        query = listener.recognize_google(audio, language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    query = query.lower()
    return query


# commands while on rest mosde
def rest_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold = 3
        audio = listener.listen(source, timeout=1000, phrase_time_limit=100)

    try:
        print("Recognizing...")
        query = listener.recognize_google(audio, language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        return "none"
    query = query.lower()
    return query

# For getting news
def news():
    main_url = "https://newsapi.org/v2/everything?q=tesla&from=2023-04-19&sortBy=publishedAt&apiKey=52dd107251c6473f8b45a6e0432475d3"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


# To wish
def greet():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good morning sir, I'm Friday. How may i help you today?")
    elif hour > 12 and hour < 18:
        speak("Good afternoon sir, I'm Friday. How may i help you today?")
    else:
        speak("Good evening sir, I'm Friday. How may i help you today?")

##
def run_system():
    greet()
    while True:
        query = take_command().lower()

        # Logic building for tasks
        if "open notepad" in query:
            speak("Sure sir, opening notepad")
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2303.40.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)

        # For closing notepad using friday
        elif "close notepad" in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im Notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play a music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        # For opening websites
        elif "open google" in query:
            webbrowser.open("https://www.google.com/")
            url = "Google is now opened sir, what should i search on google?"
            speak(url)
            cm = take_command().lower()
            gglreply = ("searching " + cm + " on google...")
            speak(gglreply)
            webbrowser.open(f"{cm}")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            url1 = "Facebook is now opened."
            speak(url1)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            url2 = "Youtube is now opened."
            speak(url2)

        # instagram
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
            url3 = "Insta gram is now opened."
            speak(url3)

        elif "instagram profile" in query or "profile on instagram" in query or "profile in instagram" in query:
            speak("Sure sir, please enter the username of the profile you want to check.")
            insname = input("Enter username here: ")
            webbrowser.open(f"https://www.instagram.com/{insname}")
            time.sleep(5)
            speak("Sir would you like to download the profile picture of this insta gram account?")
            inscondition = take_command().lower()
            if "yes" in inscondition:
                mod = instaloader.Instaloader()
                mod.download_profile(insname, profile_pic_only=True)
                speak(
                    "I'm done sir, profile of these instagram account is now saved in your main folder, anything else sir?")
            else:
                speak("Ok sir. Anything else?")
                pass

        elif "open twitter" in query:
            webbrowser.open("https://twitter.com/")
            url4 = "Twitter is now opened."
            speak(url4)

        elif "open shopee" in query:
            webbrowser.open("https://shopee.ph")
            url5 = "Shopee is now opened"
            speak(url5)

        elif "open lazada" in query:
            webbrowser.open("https://www.lazada.com.ph")
            url6 = "Lazada is now opened"
            speak(url6)

        elif "open tiktok" in query:
            webbrowser.open("https://www.tiktok.com/")
            url7 = "Tiktok is now opened"
            speak(url7)

        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/")
            url8 = "G-mail is now opened"
            speak(url8)

        elif "open google classroom" in query:
            webbrowser.open("https://classroom.google.com")
            url9 = "Google classroom is now opened"
            speak(url9)

        elif "open google meet" in query:
            webbrowser.open("https://meet.google.com/")
            url10 = "Google meet is now opened"
            speak(url10)

        elif "open zoom" in query:
            webbrowser.open("https://zoom.us")
            url11 = "Zoom is now opened"
            speak(url11)

        elif "open reddit" in query:
            webbrowser.open("https://www.reddit.com/")
            url12 = "Reddit is now opened"
            speak(url12)

        elif "open twitch" in query:
            webbrowser.open("https://www.twitch.tv/")
            url13 = "Twitch is now opened"
            speak(url13)

        elif "open pinterest" in query:
            webbrowser.open("https://www.pinterest.com")
            url14 = "Pinterest is now opened"
            speak(url14)

        elif "open google calendar" in query:
            webbrowser.open("https://calendar.google.com")
            url15 = "google calender is now opened"
            speak(url15)

        # For playing something on youtube
        elif "on youtube" in query:
            ytsong = query.replace("play", "")
            ytreply = ("Sure sir, playing" + ytsong)
            speak(ytreply)
            kit.playonyt(ytsong)

        # For turning off, restarting, and sleeping the system
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # For switching tabs
        elif "switch tab" in query or "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        # For news
        elif "tell me the news" in query or "can you check the news for me" in query or "check the news" in query:
            speak("please wait sir, I'm fetching the latest news for you...")
            news()

        # For finding my location
        elif "where am i" in query or "where are we" in query:
            speak("please wait for a moment sir, I'm checking our location...")
            try:
                ipadd = requests.get("https://api.ipify.org").text
                print(ipadd)
                url = "https://get.geojs.io/v1/ip/geo/" + ipadd + ".json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data["city"]
                country = geo_data["country"]
                speak(f"I have found our location sir, we are in {city} of {country} country.")
            except Exception as e:
                speak("I'm really sorry sir, due to network issues i am not able to find our location.")
                pass

        # For taking a screenshot
        elif "take screenshot" in query or "take a screenshot" in query or "capture a picture of my screen" in query:
            speak("Sir, what should i name this screenshot file?")
            scrname = take_command().lower()
            speak("Keep your screen steady sir, I'm taking a screenshot...")
            time.sleep(3)
            scrimg = pyautogui.screenshot()
            scrimg.save(f"{scrname}.png")
            speak("Sir, I'm done taking screenshot, the file is now save in your main folder, anything else sir?")

        elif "you can sleep now" in query or "sleep for now" in query:
            goodbye = "I understand sir, you can call me anytime if you need me. Friday sleeping..."
            speak(goodbye)
            break

        # time, day, and date
        elif "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak("the current time is " + time)

        elif "date" in query:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak("Today is " + date)

        elif "day" in query:
            day = datetime.datetime.now().strftime("%A")
            speak("Today is " + day)


if __name__ == "__main__":
    while True:
        permission = rest_command()
        if "wake up" in permission or "hey" in permission:
            run_system()
        elif "exit" in permission:
            goodbye = "it was an honor to serve you sir, i'll talk to you again soon, Exiting friday."
            speak(goodbye)
            sys.exit("AI-Friday is successfully terminated.")