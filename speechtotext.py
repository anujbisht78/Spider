# WE WILL MAKE A PROGRAM USING THE SPEECH RECOGNITION PYTHON TO EXECUTE THE FOLLOWING :
# => CONVERTING SPEECH TO TEXT USING SPEECH RECOGNITION
# => USING THE TEXT TO OPEN THE URL USING WEB BROWSER 
# => SERACHING THE QUERY INSIDE THE URL 

import speech_recognition as sr
import webbrowser as wb

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
     print('[search edureka: search python]')
     print('Speak Now')
     audio=r3.listen(source)
     
    
     
if 'google' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.google.com/'
    with sr.Microphone() as source:
        print('Search your query')
        audio=r2.listen(source)

        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("failed".formay(e))

    
    