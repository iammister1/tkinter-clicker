import pickle
from tkinter import *

SAVE_FILE = "clicker_data.pkl"

def load_data():
    global clicks, multiplier, autoclicker
    try:
        with open(SAVE_FILE, "rb") as file:
            clicks, multiplier, autoclicker = pickle.load(file)
    except FileNotFoundError:
        clicks, multiplier, autoclicker = 0, 1, 1

def save_data():
    with open(SAVE_FILE, "wb") as file:
        pickle.dump((clicks, multiplier, autoclicker), file)

application = Tk()
application.title("clicker")
application.geometry("600x600")

clicks = 0
multiplier = 1
autoclicker = 1

load_data()

def updateClicksLabel():
    clicks_label.config(text=f"Clicks: {clicks}")

def updateAutoclicker():
    autoclicker_label.config(text=f"Autoclicker: {autoclicker - 1}")
    autoclicker_button.config(text=f"Autoclicker: {autoclicker * 250} Clicks")

def updateMultiplier():
    multiplier_button.config(text=f"Multiplier: {multiplier * 50} Clicks")
    multiplier_label.config(text=f"Multiplier: {multiplier}")

def multiplierFunc():
    global clicks, multiplier
    if clicks >= multiplier * 50:
        clicks -= multiplier * 50
        multiplier += 1
        updateMultiplier()
        updateClicksLabel()

def autoclickerFunc():
    global clicks, autoclicker
    if clicks >= autoclicker * 250:
        clicks -= autoclicker * 250
        autoclicker += 1
        updateAutoclicker()
        updateClicksLabel()

def autoclickFunc():
    global clicks, autoclicker
    if autoclicker > 1:
        clicks += autoclicker - 1
        updateClicksLabel()
    application.after(1000, autoclickFunc)

def clickFunc():
    global clicks, multiplier
    clicks += multiplier
    updateClicksLabel()

clicks_label = Label(application, text=f"Clicks: {clicks}", font=("Arial", 18))
clicks_label.pack(padx=10, pady=10)

clicks_button = Button(application, text="Click", font=("Arial", 18), command=clickFunc)
clicks_button.pack(padx=10, pady=10)

multiplier_button = Button(application, text=f"Multiplier: {multiplier * 50} Clicks", font=("Arial", 18), command=multiplierFunc)
multiplier_button.pack(padx=10, pady=10)

autoclicker_button = Button(application, text=f"Autoclicker: {autoclicker * 250} Clicks", font=("Arial", 18), command=autoclickerFunc)
autoclicker_button.pack(padx=10, pady=10)

autoclicker_label = Label(application, text=f"Autoclicker: {autoclicker - 1}", font=("Arial", 18))
multiplier_label = Label(application, text=f"Multiplier: {multiplier}", font=("Arial", 18))

multiplier_label.place(x=20, y=30)
autoclicker_label.place(x=20, y=60)

autoclickFunc()

application.protocol("WM_DELETE_WINDOW", lambda: (save_data(), application.destroy()))

application.mainloop()
