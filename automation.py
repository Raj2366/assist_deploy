import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
from playsound import playsound  
from deep_translator import GoogleTranslator
from gtts import gTTS 
import os

engine = pyttsx3.init(driverName='nsss') 
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    translated_text = GoogleTranslator(source='en', target='hi').translate(audio)
    print(f"Translated Text: {translated_text}")
    
    # Convert translated text to speech
    tts = gTTS(text=translated_text, lang='hi')
    tts.save("translated_speech.mp3")
    
    # Play the saved audio file
    playsound("translated_speech.mp3")
    os.remove("translated_speech.mp3")


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...") 

        return "None"
    return query






# query = takeCommand().lower()
# trans_query = GoogleTranslator(source='hi', target='en').translate(query)
# print(f"Translated Query: {trans_query}")

def searchGoogle(query):
        
        
    #if "search" in query:
        import wikipedia as googleScrap
        #query = query.replace("search","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,sentences=2)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
        
        
    #if "play" in query:
        speak("This is what I found for your search!") 
        #query = query.replace("play","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


