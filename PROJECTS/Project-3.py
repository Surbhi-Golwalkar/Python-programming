
import speech_recognition as s
sr = s.Recognizer()
print("I am your Alexa and listening you..")

with s.Microphone() as m:
    audio = sr.listen(m)
    query = sr.recognize_google(audio,language='eng-in')
    print(query)


import speech_recognition as s
sr=s.Recognizer()   #constructor
print("I am your script and listening you................")
with s.Microphone() as m:   # object with keyword automatic close Microphone
    audio = sr.listen(m)
    query = sr.recognize_google(audio,language='eng-in')
    print(query)