from pyttsx3 import speak
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import os


#initializing the recognizer
r = sr.Recognizer()

def SpeakText(command):   #bolna
    #initialize the engine
    e = pyttsx3.init()
    e.say(command)
    e.runAndWait()

# Loopz
def takecom():  #sunnna
    try:
        #use the microphone for input
        with sr.Microphone() as source2:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source2)

            #listen to the input from user
            print("Listening ...")
            audio2 = r.listen(source2)

            # using google to recognize audio
            MyText = r.recognize_google(audio2)
            
            MyText = MyText.lower()
            print(MyText)
        
    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except Exception: #For Error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return MyText
#SpeakText('hello, hello sir')
#takecom()

def TaskExe():

    def music():
        speak('tell me the name of the song...')
        MusicName = takecom()
        if 'my song' in MusicName:
            os.startfile('we.mp3')
        elif 'mew song' in MusicName:
            os.startfile('badshah.mp3')
        else:
            pywhatkit.playonyt(MusicName)
        speak(' song has been started....')

    while True:

        query =takecom()

        if 'hello' in query:
            speak("Hello sir , I am Saket")
            speak("your Personal AI Assistant!")
            speak("How May I help you")
        elif 'how are you' in query:
            speak("I am fine papa!")
            speak("what about you?")
        elif 'Hey saket! how are you' in query:
            speak("Good")       
        elif 'bye' in query:
            speak("ok papa")
        elif 'youtube search' in query:
            speak('Ok Sir,This is what I found for you in serach')
            query = query.replace('Saket',"")
            query = query.replace('youtube search',"")
            web = "https://www.youtube.com/results?search_query="+ query
            webbrowser.open(web)
            speak("Done Sir")
        elif 'google search' in query:
            speak('Ok Sir,This is what I found for you in serach')
            query = query.replace('Saket',"")
            query = query.replace('google search',"")
            pywhatkit.search(query)
            speak("Done Sir")
        elif 'open website' in query:
            speak('Tell me the name of the website..')
            name = takecom()
            web ='https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done ma'am")
        elif 'facebook' in query:
            speak("ok mam")
            webbrowser.open('https://www.facebook.com/')
            speak("Done mam")
        elif 'music' in query:
            music()
        
            
TaskExe()