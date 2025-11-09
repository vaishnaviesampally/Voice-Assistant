import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source, phrase_time_limit=6)
    try:
        query = r.recognize_google(audio, language='en-in')
        print("You:", query)
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except Exception as e:
        print("Error:", e)
        return ""

def main():
    speak("Hello vaishnavi , I am your assistant. Say 'stop' to exit.")
    time.sleep(0.5)
    while True:
        query = listen()
        if not query:
            continue
        if 'time' in query:
            t = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {t}")
        elif 'wikipedia' in query:
            topic = query.replace('wikipedia', '').strip()
            if topic:
                try:
                    result = wikipedia.summary(topic, sentences=2)
                    speak(result)
                except Exception as e:
                    speak("I couldn't find that on Wikipedia.")
            else:
                speak("What should I search on Wikipedia?")
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube.")
        elif 'stop' in query or 'exit' in query:
            speak("Goodbye!")
            break
if __name__== "__main__":
    main()