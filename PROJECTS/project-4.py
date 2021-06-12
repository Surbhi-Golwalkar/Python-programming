# https://pypi.org/project/SpeechRecognition/
# https://www.lfd.uci.edu/~gohlke/pythonlibs/
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



# while(1):
    try:
        with sr.Microphone() as source2:
             # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source2)

            # listen to the user
            print("Hello sir How can i help you ")

            audio2 = r.listen(source2)

            mytext = r.recognize_google(audio2)
            mytext = mytext.lower()

            print("did you say "+ mytext)
            speakText(mytext)
    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown Error occured")