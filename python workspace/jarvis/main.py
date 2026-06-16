import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(text):
    if text:
        print("Jarvis:", text)
        engine.say(text)
        engine.runAndWait() 


listener = sr.Recognizer()

def take_command(timeout=5):
    command = ""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Listening...")
            voice = listener.listen(source, timeout=timeout, phrase_time_limit=timeout)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You:", command)
    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    except Exception as e:
        print(e)
    return command

def run_jarvis(command):
    if "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "search" in command:
        search = command.replace("search", "").strip()
        speak(f"Searching for {search}")
        pywhatkit.search(search)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        if person:
            try:
                info = wikipedia.summary(person, sentences=2)
                for sentence in info.split('. '):
                    speak(sentence)
            except wikipedia.exceptions.DisambiguationError:
                speak(f"Multiple results found for {person}, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I could not find information about {person}.")
        else:
            speak("Please say the name of the person.")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "stop" in command:
        speak("Going back to sleep")
        return "stop"

    else:
        speak("I can play music, search Google, or search Wikipedia")

while True:
    wake = take_command(timeout=10)
    if "jarvis" in wake:
        speak("Yes, I am listening")
        while True:
            cmd = take_command(timeout=5)
            if cmd:
                result = run_jarvis(cmd)
                if result == "stop":
                    break
