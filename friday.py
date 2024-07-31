import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
print(voices[1].id) 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Convert text to speech"""
    engine.say(audio)
    engine.runAndWait()

def wishME():
    """Greet the user based on the current time"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    
    speak("I am Friday. Please tell me how may I assist you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Could you please say it again?")
        return "None"
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the recognition service.")
        return "None"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "None"
    
    return query

if __name__ == "__main__":
    wishME()
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for this search, please be more specific.")
                print(e.options)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find any results for that search.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")
                print(f"An error occurred: {e}")

        elif 'open youtube' in query:
            speak('Opening YouTube')
            webbrowser.open("https://www.youtube.com")
        
        elif 'open instagram' in query:
            speak('Opening Instagram')
            webbrowser.open("https://www.instagram.com")

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("https://www.google.com")

        elif 'open spotify' in query:
            speak('Opening Spotify')
            webbrowser.open("https://www.spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open visual studio code' in query:
            codepath = "C:\\Users\\HP\\Desktop\\Visual Studio Code.lnk"
            speak('Opening VS code')
            os.startfile(codepath)

        elif 'open game' in query:
            gta5path = "Z:\\Grand Theft Auto V\\GTA5.exe"
            speak('Opening GTA 5')
            try:
                os.startfile(gta5path)
            except Exception as e:
                speak(f'Failed to open GTA 5: {e}')
                print(f'Error: {e}')

       