import pyttsx3
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[1].id)
engine.setProperty('rate',180)


# Converts text to voice
def speak(audio):
    print("    ")
    print(f"Ghoul : {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Good after noon sir!")