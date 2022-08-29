from logging import exception
from posixpath import split
from time import strftime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    h = int(datetime.datetime.now().hour)
    if h >= 0 and h < 12:
        speak("Good Morning")

    elif h >= 12 and h < 18:
        speak("Good Afternoon")

    else:
        speak("Good evening")
    speak("Hello sir! Tell me what to do")


def takecommand():
    '''
    this function will take voice as input by the user and convert it into string for further use...
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except:
        print("say that again please...")
        return "none"

    return query


if __name__ == "__main__":
    print("for using this please use these commands:-")
    print("To open a link:- use something like \"open youtube\"")
    print("for search in google:- use something like \"search microsoft\"")
    print("and use this!!!!")
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipwdia', '')
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipwdia...")
            print(results)
            speak(results)

        elif 'the time' in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {t}")

        elif 'open' in query:
            q = query.split()
            webbrowser.open(f"https://www.{q[1]}.com/")

        elif 'search' in query:
            qu = query.split()
            webbrowser.open(f"https://google.com/search?q={qu[1]}")

        elif 'sing' in query:
            so=query.split()
            webbrowser.open(f"https://open.spotify.com/search/{so[1]}")

        elif 'exit' in query:
            exit()

