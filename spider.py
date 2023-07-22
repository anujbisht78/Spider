import pyttsx3
import speech_recognition as sr
import datetime
import os 
import cv2 


engine=pyttsx3.init('sapi5') #creating a voice engine
voices=engine.getProperty('voices')
# print(voices[1].id) id of the voices 0:david and 1:zira
engine.setProperty('voices',voices[1].id)  #it will activate the voices from engine

#making a function that will convert text into speech
def speak(audio): #creating an audio file
    print('Spider:', audio)
    engine.say(audio) 
    engine.runAndWait() #The runAndWait () method waits until the speech is complete before returning control to the program.
    # return "none"

#To take input from the user, to convert voice into text
def takecommand():
    r=sr.Recognizer() #to define the recognizer
    with sr.Microphone() as source: #connecting the microphone   
        print('Listening.....')
        r.pause_threshold=1 #for this time period spidy can listen
        audio=r.listen(source,timeout=1,phrase_time_limit=5)

    try:  
        print('Recognizing...')
        #taking the query of google search engine
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
     
    #if spidy doesnt recognize you
    except Exception as e:   
        speak('Say that again Please..!')
        return "none"
    return query
    

#to wish
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning Sir!")      
    elif hour>=12 and hour<=15:
        speak("Good Afternoon Sir!")
    elif hour>15 and hour<=18:
        speak("Good Evening Sir!")  
    else:
        speak("Good Night Sir!")  
    
    speak("I am Spider. Please tell me How can i help you!")
    
if __name__=="__main__":
    # takecommand()
    wish()
    # speak()
    # speak("Hi I am Spidy!")
    # while True:
    if 1: #to work only one time because in while it is running again and again
        
        #whenever user is giving querry, that querry will be stored
        query=takecommand().lower() #lowercase
        
        #logic building for tasks
        
        if  "spider can you please open youtube" in query:
            YTpath="https://www.youtube.com/"
            os.startfile(YTpath)
            
        elif "spider can you please open google" in query:
            Gpath="https://www.google.com/"
            os.startfile(Gpath)
            
        elif "spider can you please open gmail" in query:
            Gmpath="https://www.gmail.com/"
            os.startfile(Gmpath)
            
        elif "spider can you please open command prompt" in query:
            os.system("start cmd")
            
        elif "spider can you please open camera" in query:
            cap=cv2.VideoCapture(0) #0:internal camera, 1:external camera
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release() #releasing the camera
            cv2.destroyAllWindows()
            
        elif "spider can you please play music" in query:
            Spath="https://www.spotify.com/"
            os.startfile(Spath)
            
            
            
        
            
            
            
        
    
