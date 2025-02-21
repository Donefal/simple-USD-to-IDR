# For the GUI
import tkinter as tk
import ttkbootstrap as ttk

# For Web Scrapping
from bs4 import BeautifulSoup
import requests

# For time
from datetime import datetime

url = "https://www.google.com/finance/quote/USD-IDR?sa=X&ved=2ahUKEwiU47DPnrWKAxX21zgGHbQaE0EQmY0JegQICxAu"

def scrapeData():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    div = soup.find("div", class_= "YMlKec fxKbKc")
    data = div.text
    dataFinal = float(data.replace(",", ""))
    
    return dataFinal


def getTime():
    now = datetime.now()
    currentTime = now.strftime("%D (%H:%M:%S)")
    timeString.set(f"Convertion rate as of {currentTime}\nData scrapped from Google Finance")


def convert():
    getTime()
    convertionRate = scrapeData()
    usd = entryInt.get()
    idr = usd * convertionRate
    outputString.set(f"Rp.{idr:,.2f}")


# MAIN FUNCTION
# window
window = ttk.Window(themename= "journal")
window.title("A Start")
window.geometry("400x300")

# tittle 
titleLabel = ttk.Label(master= window, text= "(Live) USD to IDR", font= "Arial 20 bold")
titleLabel.pack(pady= 10)

# input field
inputFrame = ttk.Frame(master= window)
entryInt = tk.IntVar()
entry = ttk.Entry(master= inputFrame, textvariable= entryInt)
button = ttk.Button(master= inputFrame, text= "Convert", command= convert)

entry.pack(side= "left", padx= 10)
button.pack(side= "left")
inputFrame.pack(pady= 10)

# output
outputString = tk.StringVar()
outputLabel = ttk.Label(
    master= window, 
    text= "out", 
    font= "Arial 15", 
    textvariable= outputString
    )
outputLabel.pack(pady= 10)

timeString = tk.StringVar()
timeLabel = ttk.Label(
    master= window,
    text= "test",
    font= "Arial 10",
    textvariable= timeString,
    justify= "center"
    )
timeLabel.pack()

# run
window.mainloop()

