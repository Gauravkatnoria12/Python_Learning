import speech_recognition as sr
import pyttsx3
import os
import subprocess
import random
import pygame

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200) # Slightly faster speech

# Global recognizer
recognizer = sr.Recognizer()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        recognizer.pause_threshold = 0.6 # Faster detection of end of speech
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
    except:
        return "None"
    return query.lower()

def open_application(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "browser": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "edge": "msedge.exe"
    }
    
    if app_name in apps:
        # Execute FIRST, then speak for "fast" feel
        try:
            if "\\" in apps[app_name]: 
                os.startfile(apps[app_name])
            else:
                subprocess.Popen(apps[app_name])
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Error: {str(e)}")
    else:
        try:
             subprocess.Popen(f"start {app_name}", shell=True)
             speak(f"Trying to open {app_name}")
        except:
             speak(f"Could not find {app_name}")

# Cache music list once
MUSIC_DIR = os.path.join(os.environ['USERPROFILE'], 'Music')
SONGS_CACHE = []

def play_music():
    global SONGS_CACHE
    if not os.path.exists(MUSIC_DIR):
         speak("Music folder not found.")
         return

    if not SONGS_CACHE:
        SONGS_CACHE = [f for f in os.listdir(MUSIC_DIR) if f.endswith('.mp3')]
    
    if not SONGS_CACHE:
        speak("No mp3 files found.")
        return

    song = random.choice(SONGS_CACHE)
    # Start playing immediately
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(MUSIC_DIR, song))
    pygame.mixer.music.play()
    speak(f"Playing {song}")

if __name__ == "__main__":
    speak("Hello! I am your AI Assistant. How can I help you today?")
    
    while True:
        query = listen_command()

        if 'open' in query:
            app = query.replace('open ', '').strip()
            open_application(app)
            
        elif 'play music' in query or 'play song' in query:
            play_music()
            
        elif 'stop music' in query:
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
                speak("Music stopped.")
            else:
                speak("Music is not playing.")

        elif 'exit' in query or 'stop' in query or 'quit' in query:
            speak("Goodbye!")
            break
        
        elif 'none' == query:
            continue
        
        else:
            speak("I'm sorry, I don't know that command yet.")
