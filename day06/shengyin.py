import pyttsx3
import win32com.client
# engine=pyttsx3.init()
# engine.say('hello 11111111111111111111111111')
# engine.runAndWait()



engine=pyttsx3.init()

vs=engine.getProperty('voices')
for voice in vs:
    engine.say('hahhahahhhahh')
    engine.setProperty('rate',130)

engine.runAndWait()