import pyttsx3
from reference import b, c
#from pytube import YouTube
import wikipedia


while True:
    engine = pyttsx3.init()
    a = input()
    if a == c[0]:
        engine.say(b[0])
        engine.runAndWait()

    if a == c[1]:
        engine.say(b[1])
        engine.runAndWait()

    if a == c[2]:
        engine.say(b[2])
        engine.runAndWait()

    if a == c[3]:
        engine.say(b[3])
        engine.runAndWait()

    if a == c[4]:
        engine.say(b[4])
        engine.runAndWait()
        result = str(input())
        result = wikipedia.summary(result, sentences = 3)
        print(result)
        engine.say(result)
        engine.runAndWait()
    #except Exception as e:
     #   engine.say('cant seem to get this data')
    #    engine.runAndWait() 

    if a == c[5]:
        engine.say(b[5])
        engine.runAndWait()


    
output.say()



    
    #print('chat ended')
    
    


