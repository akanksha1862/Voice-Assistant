import speech_recognition as sr
import webbrowser
import time
from time import ctime
import os
import os.path
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")  
  
    else:
        speak("Good Evening !") 
    speak("I am your voice Assistant")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r=sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
                
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
                           
         
        except sr.UnknownValueError:
            speak("sorry i did not get that")
        except sr.RequestError:
            speak("sorry my speech service is down")
        return voice_data

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('my name is alexis')
    if 'what time is it' in voice_data:
        speak(ctime())        
    if 'search' in voice_data:
        search=record_audio('what do you want to search for')
        url ='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('here is what i found for ' + search)
    if 'find location' in voice_data:
        location=record_audio('what is the location')
        url ='https://google.nl/maps/place/' + location +'/&amp;'
        webbrowser.get().open(url)
        speak('here is the location of ' + location)

    if "what are today's headlines" in voice_data:
        url ='https://www.hindustantimes.com/'
        webbrowser.get().open(url)
        speak("here are today's headlines") 

    if "open Youtube" in voice_data:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")   

    if 'open camera' in voice_data:
        speak("turning your camera on")
        os.system('start explorer shell:appsfolder\Microsoft.WindowsCamera_8wekyb3d8bbwe!App')
    
    if 'how is the weather' in voice_data:
        speak("here is the weather update")
        os.system('start explorer shell:appsfolder\Microsoft.BingWeather_8wekyb3d8bbwe!App')
    
    if 'set alarm' in voice_data:
        speak("when would you like to set the alarm")
        os.system('start explorer shell:appsfolder\Microsoft.WindowsClock_8wekyb3d8bbwe!App')

    if 'make a note'in voice_data:
        speak("What would you like me to write down? ")
        write_down = record_audio()
        note(write_down)
        speak("I've made a note of that.")

    if 'exit' in voice_data:
        speak("okay bye! have a nice day")
        exit()
        
    
    if 'which class' in voice_data:
        hour = int(datetime.datetime.now().hour)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = days[datetime.datetime.today().weekday()]
        if(day=='Monday'):
            if(hour>9 and hour < 12):
                speak("You have Operating systems lab now")
            elif(hour>12 and hour<13):
                speak("it's time for lunch")
            elif(hour>13 and hour<16):
                speak("You have professional elective lab now")
            else:
                speak("You have no classes to attend now")
        elif(day=="Tuesday"):
            if(hour>9 and hour < 10):
                speak("You have Design and analysis of algorithms class now")
            elif(hour>10 and hour<11):
                speak("You have Operating systems class now")
            elif(hour>11 and hour<12):
                speak("You have Formal language and automata theory  class now")
            elif(hour>12 and hour<13):
                speak("it's time for lunch")
            elif(hour>13 and hour<14):
                speak("You have professional elective class now")
            elif(hour>14 and hour<15):
                speak("you have open elective class now")
            elif(hour>15 and hour<16):
                speak("you have mentoring session now")
            else:
                speak("You have no classes to attend now")
        elif(day=="Wednesday"):
            if(hour>9 and hour < 12):
                speak("You MINI PROJECT lab now")
            elif(hour>12 and hour<13):
                speak("it's time for lunch")
            elif(hour>13 and hour<16):
                speak("You have design and analysis of algorithms lab now")
            else:
                speak("You have no classes to attend now")
        elif(day=="Thursday"):
            if(hour>9 and hour < 10):
                speak("You have Formal language and automata theory  class now")
            elif(hour>10 and hour<11):
                speak("You have Design and analysis of algorithms class now")
            elif(hour>11 and hour<12):
                speak("You have professional elective class now")
            elif(hour>12 and hour<13):
                speak("it's time for lunch")
            elif(hour>13 and hour<14):
                speak("You have open elective class now")
            elif(hour>14 and hour<15):
                speak("you have Operating systems class now")
            elif(hour>15 and hour<16):
                speak("you have Library now")
            else:
                speak("You have no classes to attend now")
        
        elif(day=="Friday"):
            if(hour>9 and hour < 10):
                speak("You have professional elective class now")
            elif(hour>10 and hour<11):
                speak("You have Formal language and automata theory  class now")
            elif(hour>11 and hour<12):
                speak("You have open elective class now")
            elif(hour>12 and hour<13):
                speak("it's time for lunch")
            elif(hour>13 and hour<14):
                speak("You have Operating systems class now")
            elif(hour>14 and hour<15):
                speak("you have Design and analysis of algorithms class now")
            else:
                speak("You have no class to attend now")
        else:
            speak("its a holiday today")
            
                   
#commit
time.sleep(1)     
wishMe()             
speak("How can i help you?")
while 1:
    voice_data=record_audio()
    respond(voice_data)
