import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hi Sasha")
engine.say("How can i help you sir ?")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "jarvis" in command:
            print(command)
except:
    pass