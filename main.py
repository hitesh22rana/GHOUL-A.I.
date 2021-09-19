import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)

# Converts text to voice
def speak(audio):
    engine.say(audio)
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

def wish():
    hour = int(datetime.datetime.now().hour)

    if(hour > 0 and hour < 12):
        speak("Good Morning Sir!")

    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")



if __name__ == "__main__":
    wish()
