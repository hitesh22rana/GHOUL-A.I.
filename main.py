import time
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import os
from requests import get
import cv2
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[1].id)
engine.setProperty('rate',175)


def speak(audio):
    print("    ")
    print(f"Ghoul : {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()


def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        time.sleep(0.2)
        r.pause_threshold = 1.5
        audio = r.listen(source,timeout=2,phrase_time_limit=10)

        try:
            print("Recognizing...\n")
            time.sleep(0.5)
            query = r.recognize_google(audio , language='en-in')
            print(f"User said : {query}")
    
        except Exception as e:
            speak("Sorry! Can't able to understand you! Say that again please!...")
            return "none"
    
        return query



def TakeCommand_Hindi():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        time.sleep(0.5)
        r.pause_threshold = 1.5
        audio = r.listen(source,timeout=2,phrase_time_limit=10)

        try:
            print("Recognizing...")
            time.sleep(0.5)
            query = r.recognize_google(audio , language='hi')
            print(f"User said : {query}")
    
        except Exception as e:
            speak("Sorry! Can't able to understand you! Say that again please!...")
            return "none"
    
        return query


# Wish Function
def wish():
    hour = int(datetime.datetime.now().hour)

    if(hour > 0 and hour < 12):
        speak("Good Morning Sir!")

    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Ghoul! Your Personal AI Assistant.. How Can I Help you!")



if __name__ == "__main__":
    wish()
    while(True):
    
        query = TakeCommand().lower()
        
        #Logic for tasks

        # feature to open notepad

        if ("open notepad") in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)


        # feature to open cmd

        elif ("open command prompt") in query:
            os.system("start cmd")

        
        # feature to open camera

        elif ("open camera") in query or ("open web camera") in query:
            speak("Opening Camera!")

            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()

        
        # feature to get your own ipaddress

        elif ("ip address") in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is : {ip}")      


        # feature to open wikipedia

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia : ")
            speak(results)
            print(results)

        # feature to open youtube

        elif "open youtube" in query:
            speak("What should i search on youtube!")
            try:
                task = TakeCommand().lower()
                webbrowser.open(f"https://www.youtube.com/results?search_query={task}")
            
            except Exception as e:
                speak("Unable to Search! sorry!")


        # feature to open Google and search on it

        elif "open google" in query:
            speak("What should i search on Google!")
            try:
                task = TakeCommand().lower()
                webbrowser.open(f"{task}")

            except Exception as e:
                speak("Unable to Search! sorry!")