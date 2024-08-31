from flask import Flask, render_template, request, jsonify
import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import requests
from playsound import playsound  
from deep_translator import GoogleTranslator
from gtts import gTTS 
import os
from apikey import *


flag = 0

# A tuple containing all the language and 
# codes of the language will be detcted 
dic = ('afrikaans', 'af', 'albanian', 'sq', 
	'amharic', 'am', 'arabic', 'ar', 
	'armenian', 'hy', 'azerbaijani', 'az', 
	'basque', 'eu', 'belarusian', 'be', 
	'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
	'bg', 'catalan', 'ca', 'cebuano', 
	'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
	'zh-cn', 'chinese (traditional)', 
	'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
	'czech', 'cs', 'danish', 'da', 'dutch', 
	'nl', 'english', 'en', 'esperanto', 'eo', 
	'estonian', 'et', 'filipino', 'tl', 'finnish', 
	'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
	'gl', 'georgian', 'ka', 'german', 
	'de', 'greek', 'el', 'gujarati', 'gu', 
	'haitian creole', 'ht', 'hausa', 'ha', 
	'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
	'hi', 'hmong', 'hmn', 'hungarian', 
	'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian', 
	'id', 'irish', 'ga', 'italian', 
	'it', 'japanese', 'ja', 'javanese', 'jw', 
	'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
	'km', 'korean', 'ko', 'kurdish (kurmanji)', 
	'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
	'latin', 'la', 'latvian', 'lv', 'lithuanian', 
	'lt', 'luxembourgish', 'lb', 
	'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
	'ms', 'malayalam', 'ml', 'maltese', 
	'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
	'mn', 'myanmar (burmese)', 'my', 
	'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
	'pashto', 'ps', 'persian', 'fa', 
	'polish', 'pl', 'portuguese', 'pt', 'punjabi', 
	'pa', 'romanian', 'ro', 'russian', 
	'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
	'serbian', 'sr', 'sesotho', 'st', 
	'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si', 
	'slovak', 'sk', 'slovenian', 'sl', 
	'somali', 'so', 'spanish', 'es', 'sundanese', 
	'su', 'swahili', 'sw', 'swedish', 
	'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
	'te', 'thai', 'th', 'turkish', 
	'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
	'ug', 'uzbek', 'uz', 
	'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
	'yiddish', 'yi', 'yoruba', 
	'yo', 'zulu', 'zu') 


#from gtts import gTTS

app = Flask(__name__)

engine = pyttsx3.init(driverName='nsss') 
voices = engine.getProperty("voices")
engine.setProperty("voice", [1])
engine.setProperty("rate", 170) #170 words per minute


def speak(audio):
    translated_text = GoogleTranslator(source='en', target='hi').translate(audio)
    print(f"Translated Text: {translated_text}")
    
    # Convert translated text to speech
    tts = gTTS(text=translated_text, lang='hi')
    tts.save("translated_speech.mp3")
    
    # Play the saved audio file
    playsound("translated_speech.mp3")
    os.remove("translated_speech.mp3")

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    elif hour >= 18 and hour < 20:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("Hi, I am your news assistant. please tell me how may i help you ")


def takeCommand():
    
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        # r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4) #timeout(wait after speech listen)= 0, phrasetime-limit(wait for speech listen)= 4
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='hi')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please...")

        return "None"
    return query

def process_command(query):
    trans_query = GoogleTranslator(source='hi', target='en').translate(query)
    print(f"Translated Query: {trans_query}")

    

        # Logic for executing tasks based on query
    if 'wikipedia' in trans_query.lower():  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            trans_query = trans_query.replace("search wikipedia", "")
            results = wikipedia.summary(trans_query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in trans_query.lower():
            speak("Ok boss")
            webbrowser.open("youtube.com")


    elif 'open google' in trans_query.lower():
            speak("Ok boss")
            webbrowser.open("google.com")

    elif 'commands list' in trans_query.lower():
            speak("my commands are")
            speak("you can say open google")
            speak("you can say open youtube")
            speak("you can ask time")
            speak("you can say search wikipedia related any topic")
            speak("you can ask the latest news")
            speak("you can say search any topic on google")
            speak("you can say play any video on youtube")
            speak("you can ask weather")
            speak("you can hear the facts")
            speak("you can say exit when your search is done")
            speak("you can give your feedback")



    elif 'time' in trans_query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

    elif 'date' in trans_query.lower():
            str_date = datetime.datetime.now().strftime("%d-%m-%Y")
            speak(f"the date is {str_date}")


    elif "search" in trans_query.lower():
            from automation import searchGoogle
            searchGoogle(trans_query)

    elif "play" in trans_query.lower():
            from automation import searchYoutube
            searchYoutube(trans_query)

    elif "latest news" in trans_query.lower():
        news()
        speak("Ok , Now I will read news for you")
        for i in range(len(ar)):
                print(ar[i])
                speak(ar[i])





    elif "weather" in trans_query.lower():
          api_key = "8ef61edcf1c576d65d836254e11ea420"
          base_url = "https://api.openweathermap.org/data/2.5/weather?"
          speak("whats the city name")
          city_name = takeCommand()
          complete_url = base_url + "appid=" + api_key + "&q=" + city_name
          response = requests.get(complete_url)
          x = response.json()
          if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
          else:speak(" City Not Found ")






    # elif "stop".lower() in trans_query.lower():
    #         speak("Ok")
    #         exit()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    user_command = takeCommand()
    if user_command:
        response = process_command(user_command)
        return jsonify({"response": response})
    return jsonify({"response": "Sorry, I couldn't understand you."})

if __name__ == "__main__":
    app.run(debug=True)
