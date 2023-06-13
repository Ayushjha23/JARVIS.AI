from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import datetime
import webbrowser
import datetime
import wolframalpha
import wikipedia
import ctypes
import subprocess
import random
import operator
import winshell
import shutil
import win32com.client as wincl
import pyjokes
from ecapture import ecapture as ec
import pywhatkit 
import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak ("I am jarvis sir. Please tell me how may I help you")


class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()

    
    def run(self):
        self.JARVIS()

    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()

            if 'good bye' in self.query or 'thank you jarvis' in self.query:
                speak("Thanks sir for giving me time")
                sys.exit()

            elif 'send message'in self.query:
              pywhatkit.sendwhatmsg_to_group_instantly("", "Hey hiii i am jarvis this msg is sent by me in behalf of mr.ayush stark ")

             
            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir ="D:\\music_dir"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))

            elif 'calculate' in self.query:
             speak('I can answer to computational and geographical questions  and what question do you want to ask now')
             question=self.STT()
             app_id="374K4T-KQHTHLRR8G"
             client = wolframalpha.Client('374K4T-KQHTHLRR8G')
             res = client.query(question)
             answer = next(res.results).text
             speak(answer)
             print(answer)

            elif 'the time' in self.query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
             speak(f"Sir, the time is {strTime}")
             print(strTime)

            elif 'open code' in self.query:
             codePath = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)

            elif "where is" in  self.query:
             self.query = self.query.replace("where is", "")
             location = self.query
             speak("User asked to Locate")
             speak(location)
             webbrowser.open("https://www.google.co.in/maps/place/" + location + "")

            elif "i love you" in self.query:
             speak("sorry but i only love cartoons!")

            elif "who am i" in self.query:
             speak("If you talk then definitely your human.")

            elif "why you came to this world" in self.query:
             speak("Thanks to Ayush. further It's a secret")

            elif "will you be my gf" in self.query or "will you be my bf" in self.query:  
             speak("I'm not sure about, may be you should give me some time")

            elif  'wikipedia' in self.query:  #if wikipedia found in the query then this block will be executed
             speak('Searching Wikipedia...')
             self.query = self.query.replace("wikipedia", "")
             results = wikipedia.summary(self.query, sentences=2) 
             speak("According to Wikipedia")
             print(results)
             speak(results)

            elif 'joke' in self.query:
             speak(pyjokes.get_joke())

            elif 'is love' in self.query:
             speak("It is 7th sense that destroy all other senses")

            elif "who are you" in self.query:
             speak("I am your virtual assistant created by narendra modi")

            elif 'open stackoverflow' in self.query:
             speak("Here you go to Stack Over flow.Happy coding")
             webbrowser.open("stackoverflow.com")

            elif "camera" in self.query or "take a photo" in self.query:
             ec.capture(0, "Jarvis Camera ", "img.jpg")

            elif 'how are you' in self.query:
             speak("I am fine, Thank you")
             speak("How are you, Sir")

            elif 'fine' in self.query or "good" in self.query:
             speak("It's good to know that your fine")
             speak("what can i do for you sir")

            elif 'search' in self.query or 'show' in self.query:
             
             self.query = self.query.replace("search", "")
             query = self.query.replace("play", "")         
             webbrowser.open(self.query)

            elif "play" in self.query:
             print(self.query)
             songs= self.query.replace('play',"") 
             speak("playing"+ songs)
             pywhatkit.playonyt(songs)

            elif 'what is love' in self.query:
             speak("It is 7th sense that destroy all other senses")

            elif 'jor se bolo' in self.query:
               speak("jay maa ta dee")

            
             
            elif"weather" in self.query:
               city = self.query.split("in", 1)  
               soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+ {city[1]}").text,"html.parser") 
               region = soup.find("span" , class_="BNeawe tAd8D AP7Wnd")
               temp = soup.find("div" , class_="BNeawe iBp4i AP7Wnd")
               day = soup.find("div" , class_="BNeawe tAd8D AP7Wnd")
               weather= day.text.split("m", 1)
               temperature= temp.text.split("C", 1)
               speak("Its Currently" +weather[1]+ " and " + temperature[0] + "celcius"+" in "+region.text)
               print("Its Currently"+weather[1]+" and " +temperature[0] +"celcius"+" in "+region.text)

            elif"write a note" in self.query:
               speak("what should i write sir")
               writes = self.STT()
               time = datetime.datetime.now().strftime("%H:%M")
               filename = str(time).replace(":","-") +"-note.txt"
               with open(filename,"w") as file:
                  file.write(writes)
               path_1 ="C:\\Users\\ADMIN\\Desktop\\JARVIS.AI\\" + str(filename)
               path_2 ="C:\\Users\\ADMIN\\Desktop\\JARVIS.AI\\notepad\\" + str(filename)
               os.rename(path_1,path_2) 
               os.startfile(path_2)
               speak("done")

            elif "restart" in self.query:
             subprocess.call(["shutdown", "/r"])
             
            elif "hibernate" in self.query or "sleep" in self.query:
             speak("Hibernating")
             subprocess.call("shutdown / h")
 
            elif "log off" in self.query or "sign out" in self.query:
             speak("Make sure all the application are closed before sign-out")
             time.sleep(5)
             subprocess.call(["shutdown", "/l"])

            elif 'advice' in self.query:
             res = requests.get("https://api.adviceslip.com/advice").json()
             speak(res['slip']['advice'])
             
           
        
      

            






            













FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())