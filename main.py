import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)



def command():
    
    r=sr.Recognizer #to define the recognizer
    with sr.Microphone as source: #connection the microphone
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
        
        speak('Say that again..!')
        return "none"
    return query