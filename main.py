from sys import path
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import time
import os
import webbrowser
import cv2
from requests import get


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)

# Converts text to voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Converts voice to text and even speaks
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        time.sleep(0.5)
        r.pause_threshold = 1.5
        audio = r.listen(source,timeout=2,phrase_time_limit=10)
 
    try:
        print("Recognizing..")
        time.sleep(1)
        query = r.recognize_google(audio , language='en-in')
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

    speak("How Can i Help you!")


if __name__ == "__main__":
    # Wish function
    # wish()

    while True:
        query = take_command().lower()

        #Logic for tasks

        # feature to open notepad

        if ("open notepad") in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)


        # feature to open cmd

        elif ("open command prompt") in query:
            os.system("start cmd")

    
        # feature to open web-browser

        elif ("open web browser") in query:
            # speak("What do you want me to search!")
            # search = take_command().lower()
            webbrowser.open(f"https://www.google.co.in")


        # feature to open camera

        elif ("open camera") in query:
            speak("Opening Camera!")

            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()


        # feature to get own ipaddress

        elif ("ip address") in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")      

