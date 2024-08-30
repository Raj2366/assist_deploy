import requests
import json
import pyttsx3
import speech_recognition
from deep_translator import GoogleTranslator
from gtts import gTTS 
from playsound import playsound  
import os



engine = pyttsx3.init("sapi5")
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
    while True:
        try:
            r = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                print("Listening.....")
                r.pause_threshold = 1
                r.energy_threshold = 300
                audio = r.listen(source,0,4)
                print("Understanding..")
                query  = r.recognize_google(audio,language='hi')
                print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again please...") 

            return "None"
        return query


#if __name__ == "__main__":
# num = takeCommand()    

# query = takeCommand().lower()  # Converting user query into lower case

# trans_query = GoogleTranslator(source='hi', target='en').translate(query)
# print(f"Translated Query: {trans_query}")

api_address = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c65745a42f1748929f6091fa31907940"

json_data = requests.get(api_address).json()

ar = []

def news():
    
    #speak("please enter the no.")
    
    for i in range (3):
        ar.append("Number" + str(i+1)+"," + json_data["articles"][i]["title"]+".")
    return ar
    
        


     
     

     


    

    

    
    

         

    
         
    
    


    


     

         
        

    
    
    

    
        
        
    
'''speak("for continue the news say yes")
if 'yes' in query:
    pass
elif'no' in query:
    break'''
         
    


                  
          
  
               
               




     


     




          