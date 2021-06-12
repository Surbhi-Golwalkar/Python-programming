from pyttsx3 import speak
import speech_recognition as sr
import pyttsx3


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

        
    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except Exception: #For Error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return MyText
#SpeakText('hello, hello sir')
def TaskExe():
    
    while True:
        query =takecom()

        if 'hello' in query:
            speak("Hello sir , I am vihaan")
            speak("your Personal AI Assistant!")
            speak("How May I help you")
        elif 'how are you' in query:
            speak("I am fine papa!")
            speak("what about you?")
        elif 'kya haal hai vihaan' in query:
            speak("Good")       
        elif 'bye' in query:
            speak("ok papa")
    TaskExe()   