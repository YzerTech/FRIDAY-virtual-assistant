import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyaudio
from datetime import datetime
import wikipedia
import pyjokes
import random
from tkinter import *
import math as m
import sys
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
import requests
import pytz
from time import *
import webbrowser

def run_calculator():
    root = Tk()
    root.title("Computer Programming Final Project (BSCpe - 1203) - Scientific Calculator")
    e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="black", bg="white")
    e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

    def click(to_print):
        old = e.get()
        e.delete(0, END)
        e.insert(0, old + to_print)
        return

    def sc(event):
        key = event.widget
        text = key["text"]
        no = e.get()
        result = ""
        if text == "deg":
            result = str(m.degrees(float(no)))
        if text == "sin":
            result = str(m.sin(float(no)))
        if text == "cos":
            result = str(m.cos(float(no)))
        if text == "tan":
            result = str(m.tan(float(no)))
        if text == "lg":
            result = str(m.log10(float(no)))
        if text == "ln":
            result = str(m.log(float(no)))
        if text == "Sqrt":
            result = str(m.sqrt(float(no)))
        if text == "x!":
            result = str(m.factorial(int(no)))
        if text == "1/x":
            result = str(1 / (float(no)))
        if text == "pi":
            if no == "":
                result = str(m.pi)
            else:
                result = str(float(no) * m.pi)
        if text == "e":
            if no == "":
                result = str(m.e)
            else:
                result = str(m.e ** float(no))

        e.delete(0, END)
        e.insert(0, result)

    def clear():
        e.delete(0, END)
        return

    def bksps():
        current = e.get()
        length = len(current) - 1
        e.delete(length, END)

    def evaluate():
        ans = e.get()
        ans = eval(ans)
        e.delete(0, END)
        e.insert(0, ans)

    lg = Button(root, text="lg", padx=28, pady=10, relief=RAISED, command=lambda: click)
    lg.bind("<Button-1>", sc)
    ln = Button(root, text="ln", padx=29, pady=10, relief=RAISED, command=lambda: click)
    ln.bind("<Button-1>", sc)
    par1st = Button(root, text="(", padx=29, pady=10, relief=RAISED, command=lambda: click("("))
    par2nd = Button(root, text=")", padx=30, pady=10, relief=RAISED, command=lambda: click(")"))
    dot = Button(root, text=".", padx=29, pady=10, relief=RAISED, command=lambda: click("."))

    exp = Button(root, text="^", padx=28, pady=10, relief=RAISED, command=lambda: click("**"))

    degb = Button(root, text="deg", padx=23, pady=10, relief=RAISED, command=lambda: click)
    degb.bind("<Button-1>", sc)
    sinb = Button(root, text="sin", padx=24, pady=10, relief=RAISED, command=lambda: click)
    sinb.bind("<Button-1>", sc)
    cosb = Button(root, text="cos", padx=23, pady=10, relief=RAISED, command=lambda: click)
    cosb.bind("<Button-1>", sc)
    tanb = Button(root, text="tan", padx=23, pady=10, relief=RAISED, command=lambda: click)
    tanb.bind("<Button-1>", sc)

    sqrtm = Button(root, text="Sqrt", padx=22, pady=10, relief=RAISED, command=lambda: click)
    sqrtm.bind("<Button-1>", sc)
    ac = Button(root, text="C", padx=29, pady=10, relief=RAISED, fg="white", bg="orange", command=clear)
    bksp = Button(root, text="bksp", padx=19, pady=10, relief=RAISED, fg="white", bg="orange", command=bksps)
    mod = Button(root, text="mod", padx=19, pady=10, relief=RAISED, fg="white", bg="orange", command=lambda: click)
    div = Button(root, text="÷", padx=29, pady=10, relief=RAISED, command=lambda: click("/"))

    fact = Button(root, text="x!", padx=28, pady=10, relief=RAISED, command=lambda: click)
    fact.bind("<Button-1>", sc)
    seven = Button(root, text="7", padx=30, pady=10, relief=RAISED, fg="white", bg="dimgrey",
                   command=lambda: click("7"))
    eight = Button(root, text="8", padx=29, pady=10, relief=RAISED, fg="white", bg="dimgrey",
                   command=lambda: click("8"))
    nine = Button(root, text="9", padx=29, pady=10, relief=RAISED, fg="white", bg="dimgrey", command=lambda: click("9"))
    mult = Button(root, text="x", padx=29, pady=10, relief=RAISED, command=lambda: click("*"))

    frac = Button(root, text="1/x", padx=24, pady=10, relief=RAISED, command=lambda: click)
    frac.bind("<Button-1>", sc)
    four = Button(root, text="4", padx=30, pady=10, relief=RAISED, fg="white", bg="dimgrey", command=lambda: click("4"))
    five = Button(root, text="5", padx=29, pady=10, relief=RAISED, fg="white", bg="dimgrey", command=lambda: click("5"))
    six = Button(root, text="6", padx=29, pady=10, relief=RAISED, fg="white", bg="dimgrey", command=lambda: click("6"))
    minus = Button(root, text="-", padx=29, pady=10, relief=RAISED, command=lambda: click("-"))

    pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, command=lambda: click)
    pib.bind("<Button-1>", sc)
    one = Button(root, text="1", padx=30, pady=10, relief=RAISED, fg="white", bg="dimgrey", command=lambda: click("1"))
    two = Button(root, text="2", padx=29, pady=10, relief=RAISED, fg="white", bg="dimgrey", command=lambda: click("2"))
    three = Button(root, text="3", padx=29, pady=10, relief=RAISED, fg="white", bg="dimgrey",
                   command=lambda: click("3"))
    plus = Button(root, text="+", padx=29, pady=10, relief=RAISED, command=lambda: click("+"))

    e_b = Button(root, text="e", padx=29, pady=10, relief=RAISED, command=lambda: click("e"))
    e_b.bind("<Button-1>", sc)
    zero = Button(root, text="0", padx=29, pady=10, relief=RAISED, fg="white", bg="dimgrey", command=lambda: click("0"))
    equal = Button(root, text="=", padx=29, pady=10, relief=RAISED, command=evaluate)

    lg.grid(row=1, column=0)
    ln.grid(row=1, column=1)
    par1st.grid(row=1, column=2)
    par2nd.grid(row=1, column=3)
    dot.grid(row=1, column=4)

    exp.grid(row=2, column=0)
    degb.grid(row=2, column=1)
    sinb.grid(row=2, column=2)
    cosb.grid(row=2, column=3)
    tanb.grid(row=2, column=4)

    sqrtm.grid(row=3, column=0)
    ac.grid(row=3, column=1)
    bksp.grid(row=3, column=2)
    mod.grid(row=3, column=3)
    div.grid(row=3, column=4)

    fact.grid(row=4, column=0)
    seven.grid(row=4, column=1)
    eight.grid(row=4, column=2)
    nine.grid(row=4, column=3)
    mult.grid(row=4, column=4)

    frac.grid(row=5, column=0)
    four.grid(row=5, column=1)
    five.grid(row=5, column=2)
    six.grid(row=5, column=3)
    minus.grid(row=5, column=4)

    pib.grid(row=6, column=0)
    one.grid(row=6, column=1)
    two.grid(row=6, column=2)
    three.grid(row=6, column=3)
    plus.grid(row=6, column=4)

    e_b.grid(row=7, column=1)
    zero.grid(row=7, column=2)
    equal.grid(row=7, column=3)

    root.mainloop()
    return

def run_weather():
    root = Tk()
    root.title("Weather Api App: Final Project")
    root.geometry("900x500+300+200")
    root.resizable(False, False)

    def getWeather():
        try:
            city = textfield.get()

            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

            api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=70ca5fe30b7cf42dbc89e679efb63ccd"

            json_data = requests.get(api).json()
            condition = json_data["weather"][0]["main"]
            description = json_data["weather"][0]["description"]
            temp = int(json_data["main"]["temp"] - 273.15)
            pressure = json_data["main"]["pressure"]
            humidity = json_data["main"]['humidity']
            wind = json_data["wind"]["speed"]

            t.config(text=(temp, "°"))
            c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)
        except Exception as e:
            messagebox.showerror("Error", "Invalid City Name.")

    Search_image = PhotoImage(file="search.png")
    myimage = Label(image=Search_image)
    myimage.place(x=20, y=20)

    textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0,
                         fg="white")
    textfield.place(x=50, y=36)
    textfield.focus()

    Search_icon = PhotoImage(file="search_icon.png")
    myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
    myimage_icon.place(x=400, y=34)

    Logo_image = PhotoImage(file="logo.png")
    logo = Label(image=Logo_image)
    logo.place(x=150, y=120)

    Frame_image = PhotoImage(file="box.png")
    frame_myimage = Label(image=Frame_image)
    frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

    name = Label(root, font=("arial", 15, "bold"))
    name.place(x=30, y=100)
    clock = Label(root, font=("Helvetica", 20))
    clock.place(x=30, y=130)

    label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
    label1.place(x=120, y=400)

    label1 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
    label1.place(x=225, y=400)

    label1 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
    label1.place(x=400, y=400)

    label1 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
    label1.place(x=630, y=400)

    t = Label(font=("arial", 70, "bold"), fg="#ee666d")
    t.place(x=400, y=150)
    c = Label(font=("arial", 15, "bold"))
    c.place(x=400, y=270)

    w = Label(text="  ...", font=("arial", 20, "bold"), bg="#1ab5ef")
    w.place(x=120, y=430)
    h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    h.place(x=255, y=430)
    d = Label(text="         ...", font=("arial", 20, "bold"), bg="#1ab5ef")
    d.place(x=380, y=430)
    p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    p.place(x=670, y=430)

    root.mainloop()
    return

def run_digiclo():

    window = Tk()

    def on_closing():
        window.quit()

    def update():
        time_string = strftime("%I:%M:%S %p")
        time_label.config(text=time_string)

        day_string = strftime("%A")
        day_label.config(text=day_string)

        date_string = strftime("%B %d, %Y")
        date_label.config(text=date_string)

        time_label.after(1000, update)

    time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
    time_label.pack()

    day_label = Label(window, font=("Arial", 25))
    day_label.pack()

    date_label = Label(window, font=("Arial", 30))
    date_label.pack()

    update()

    window.mainloop()
    return

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 174)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = ""
            command = listener.recognize_google(voice)
            if "friday" in command:
                command = command.replace("friday", "")
                print(command)
    except:
        pass
    return command

greet = "Hello, I'm friday, your personal voice assistant. how may i help you today?"
print(greet)
talk(greet)

def run_system():
    command = take_command()
    print(command)

    if "hello" in command:
        response = "hi, how are you?"
        print(response)
        talk(response)

    if "how are you" in command:
        response1 = ["Never better.", "I'm fine, how about you?", "I'm great, thank you for asking."]
        get_res1 = random.choice(response1)
        print(get_res1)
        talk(get_res1)

    if "de boda" in command:
        mas = "Welcome back sir, what are we gonna do today?"
        print(mas)
        talk(mas)

    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.now().strftime("%I:%M %p")
        print(time)
        talk("the current time is " + time)

    elif "date" in command:
        date = datetime.now().strftime("%B %d, %Y")
        print(date)
        talk(date)

    elif "day" in command:
        day = datetime.now().strftime("%A")
        print("today is " + day)
        talk("today is " + day)

    elif "who is" in command:
        person = command.replace("who", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "joke" in command:
        joke = (pyjokes.get_joke())
        print(joke)
        talk(joke)

    elif "great to hear your voice" in command:
        talk("its great to hear your voice too")

    elif "story" in command:
        when = ["a few years ago", "yesterday", "last night", "a long time ago", "on 28th of march"]
        who = ["a person", "an old person", "a teenager", "a student", "a worker", "a programmer"]
        name = ["yzer", "yeoj", "janine", "andrei", "isabela"]
        residence = ["philippines", "america", "japan", "korea", "france"]
        went = ["cinema", "university", "seminar", "school", "laundry"]
        happened = ["made a lot of friends", "eats a burger", "found a secret key", "solved a mystery", "wrote a book"]
        story = ("here's a story. " + random.choice(when)+ ", " + random.choice(who) + " named " + random.choice(name) + " that lived in " + random.choice(residence) + " went to " + random.choice(went) + " and " + random.choice(happened)) + "."
        print(story)
        talk(story)

    elif "calculator" in command:
        talk("Running calculator.")
        run_calculator()

    elif "weather" in command:
        talk("Running weather searcher.")
        run_weather()

    elif "clock" in command:
        talk("Running digital clock.")
        run_digiclo()

    elif "google in browser" in command:
        webbrowser.open("https://www.google.com/")
        url = "Google is now opened."
        print(url)
        talk(url)

    elif "facebook in browser" in command:
        webbrowser.open("https://www.facebook.com/")
        url1 = "Facebook is now opened."
        print(url1)
        talk(url1)

    elif "youtube in browser" in command:
        webbrowser.open("https://www.youtube.com/")
        url2 = "Youtube is now opened."
        print(url2)
        talk(url2)

    elif "instagram in browser" in command:
        webbrowser.open("https://www.instagram.com/")
        url3 = "Insta gram is now opened."
        print(url3)
        talk(url3)

    elif "twitter in browser" in command:
        webbrowser.open("https://twitter.com/")
        url4 = "Twitter is now opened."
        print(url4)
        talk(url4)

    elif "shopee in browser" in command:
        webbrowser.open("https://shopee.ph")
        url5 = "Shopee is now opened"
        print(url5)
        talk(url5)

    elif "lazada in browser" in command:
        webbrowser.open("https://www.lazada.com.ph")
        url6 = "Lazada is now opened"
        print(url6)
        talk(url6)

    elif "tiktok in browser" in command:
        webbrowser.open("https://www.tiktok.com/")
        url7 = "Tiktok is now opened"
        print(url7)
        talk(url7)

    elif "gmail in browser" in command:
        webbrowser.open("https://mail.google.com/")
        url8 = "G-mail is now opened"
        print(url8)
        talk(url8)

    elif "google classroom in browser" in command:
        webbrowser.open("https://classroom.google.com")
        url9 = "Google classroom is now opened"
        print(url9)
        talk(url9)

    elif "google meet in browser" in command:
        webbrowser.open("https://meet.google.com/")
        url10 = "Google meet is now opened"
        print(url10)
        talk(url10)

    elif "zoom in browser" in command:
        webbrowser.open("https://zoom.us")
        url11 = "Zoom is now opened"
        print(url11)
        talk(url11)

    elif "reddit in browser" in command:
        webbrowser.open("https://www.reddit.com/")
        url12 = "Reddit is now opened"
        print(url12)
        talk(url12)

    elif "twitch in browser" in command:
        webbrowser.open("https://www.twitch.tv/")
        url13 = "Twitch is now opened"
        print(url13)
        talk(url13)

    elif "pinterest in browser" in command:
        webbrowser.open("https://www.pinterest.com")
        url14= "Pinterest is now opened"
        print(url14)
        talk(url14)

    elif "google calendar in browser" in command:
        webbrowser.open("https://calendar.google.com")
        url15= "google calender is now opened"
        print(url15)
        talk(url15)

    elif "who are you" in command:
        friday_det = "I'm glad you asked, my name is friday, an AI built by Yzer De Boda, Yeoj valdez, Janine aguisanda, andrei mansueto, and Isabela capalaran for the final project of Computer programming in B.S.U., The National Engineering University."
        print(friday_det)
        talk(friday_det)

    elif "exit" in command:
        goodbye = "it was an honor to serve you, i'll talk to you again soon, Exiting friday."
        print(goodbye)
        talk(goodbye)
        sys.exit("AI-Friday is succesfully terminated.")

while True:
    run_system()

##