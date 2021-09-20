import time
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import os

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
        time.sleep(0.5)
        r.pause_threshold = 1.5
        audio = r.listen(source,timeout=2,phrase_time_limit=10)

        try:
            print("Recognizing...")
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

    speak("How Can i Help you!")



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