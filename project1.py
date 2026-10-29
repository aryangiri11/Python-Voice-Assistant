import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

voice = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    voice.say(text)
    voice.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except:
        speak("Sorry, I did not understand.")
        return ""

speak("Hello! I am your voice assistant.")
speak("How can I help you?")

while True:
    command = listen()

    if "time" in command:
        current_time = datetime.datetime.now()
        time = current_time.strftime("%I:%M %p")
        speak("The time is " + time)

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "play" in command:
        song = command.replace("play", "").strip()

        if song:
            speak("Searching for " + song)
            webbrowser.open(
                "https://www.youtube.com/results?search_query=" + song
            )
        else:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break

    else:
        speak("I don't know that command.")