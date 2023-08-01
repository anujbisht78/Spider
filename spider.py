import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get  # we are only importing the get function from request
import wikipedia  # searching the wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
from smtplib import SMTP


engine = pyttsx3.init('sapi5')  # creating a voice engine
voices = engine.getProperty('voices')
# print(voices[1].id) id of the voices 0:david and 1:zira
# it will activate the voices from engine
engine.setProperty('voices', voices[0].id)

# making a function that will convert text into speech
def speak(audio):  # creating an audio file
    print('Spider:', audio)
    engine.say(audio)
    # The runAndWait () method waits until the speech is complete before returning control to the program.
    engine.runAndWait()
    # return "none"

# To take input from the user, to convert voice into text
def takecommand():
    r = sr.Recognizer()  # to define the recognizer
    with sr.Microphone() as source:  # connecting the microphone
        print('Listening.....')
        r.pause_threshold = 1  # for this time period spidy can listen
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print('Recognizing...')
        # taking the query of google search engine
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    # if spidy doesnt recognize you
    except Exception as e:
        speak('Say that again Please..!')
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 15:
        speak("Good Afternoon Sir!")
    elif hour > 15 and hour <= 20:
        speak("Good Evening Sir!")
    else:
        speak("Hello Sir!")

    speak("I am Spider. Please tell me How can i help you!")

"""sending email function"""
def sendemail(id,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('anujbisht3540@gmail.com','#anuj@7840')
    server.sendmail('anujbisht3540@gmail.com',id,content)
    server.close()

if __name__ == "__main__":
    # takecommand()
    wish()
    # speak()
    # speak("Hi I am Spidy!")
    # while True:
    if 1:  # to work only one time because in while it is running again and again

        # whenever user is giving querry, that querry will be stored
        query = takecommand().lower()  # lowercase

        # logic building for tasks

        if "spider can you please open youtube" in query:
            # YTpath = "https://www.youtube.com/"
            # os.startfile(YTpath)
            webbrowser.open("www.youtube.com")

        elif "spider can you please open google" in query:
            speak("Sir what do you want me to search on google")
            cmmnd=takecommand().lower()
            # Gpath = "https://www.google.com/"
            # os.startfile(Gpath")
            webbrowser.open(f"{cmmnd}")

        elif "spider can you please open gmail" in query:
            Gmpath = "https://www.gmail.com/"
            os.startfile(Gmpath)

        elif "spider can you please open command prompt" in query:
            os.system("start cmd")

        elif "spider can you please open facebook" in query:
            Fbpath = "https://www.facebook.com/"
            os.startfile(Fbpath)

        elif "spider can you please open camera" in query:
            cap = cv2.VideoCapture(0)  # 0:internal camera, 1:external camera
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()  # releasing the camera
            cv2.destroyAllWindows()

        elif "spider can you please play music" in query:
            Spath = "https://www.spotify.com/"
            os.startfile(Spath)
        
        # performing the online task
        # to get the ip address from the get function of request module
        elif "spider what is the ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Adress is {ip}")

        # elif "wikipedia" in query:
        #     speak("Searching on wikipedia....")
        #     query = query.replace("wikipedia","")  # want to replace my query
        #     results = wikipedia.summary(query, sentences=1)
        #     speak("According to wikipedia:")  # spider will speak
        #     speak(results)  # speaking the result from the website
        #     # print(results)  # and printing it
        
        elif "spider can you please open wikipedia" in query:
            speak("Sir what do you want me to search on wikipedia")
            cmnd=takecommand().lower()
            # query = query.replace("wikipedia","")  # want to replace my query
            results = wikipedia.summary(f"{cmnd}",sentences=1)
            speak("According to wikipedia:")  # spider will speak
            speak(results)  # speaking the result from the website
            # print(results)  # and printing it
            
        #to send whatsapp message 
        elif "spider can you please send a message" in query:
            # speak("sir to whome i send message ?")
            # msg=takecommand().lower()
            kit.sendwhatmsg("+919311671110","Good Evening",22,15) 
        
        #playing song on youtube    
        elif "spider play a song on youtube" in query:
            speak("sir which song you want me to play")
            song=takecommand().lower()
            kit.playonyt(f"{song}")
        
        #sending email to anyone
        # elif "spider send an email" in query:
        #     try:
        #         speak("sir to whome i send email")
        #         cmmd=takecommand().lower()
        #         speak("sir whats the gmail id")
        #         id=str(input())
        #         speak("sir what should i say")
        #         content=takecommand().lower()
        #         sendemail(id,content)
        #         speak("email has been sent")
                   
        #     except Exception as e:
        #         print(e)
        #         speak("sorry sir i am not able to send")
        
        elif "send email to anuj" in query:
            try:
                speak("what should i say")
                to="anujbisht3540@gmail.com"
                content=takecommand().lower()
                sendemail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send")
                
                
             
            
        
            
            
         
            
           
            
            
        
