import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir its" + str(int(hour)) + " " + str(min) + "am")
    elif (hour >= 12 and hour < 16):
        speak("Good Afternoon Sir its" + str(int(hour) - 12) + " " + str(min) + "pm")
    elif (hour >= 17 and hour < 19):
        speak("Good Evening Sir its" + str(int(hour) - 12) + " " + str(min) + "pm")
    else:
        speak("Good Night Sir its" + str(int(hour) - 12) + " " + str(min) + "pm")
    speak("I am jarvish sir how can i help you")


def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listenning...")
        r.pause_threshold = 1
        r.energy_thershold = 3378
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You Said", query)
        speak("You said ," + str(query))
        speak("Please wait i am trying to solve your problem")

    except Exception as e:
        print(e)
        print("Say Again....")
        return "None"
    return query



def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        
        query=takecmd().lower()
        if("wikipedia" in query):
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia"+result)
            print(result)
        elif("open youtube") in query:
            webbrowser.open('youtube.com')
        elif("open google") in query:
            webbrowser.open('google.com')
        elif("play music") in query:
            music_dir='D:\\Songs\punjabi songs'
            song=os.listdir(music_dir)
            i=random.randint(0,len(song)-1)
            os.startfile(os.path.join(music_dir,song[i]))
        elif("the date") in query:
            date=datetime.date.today().strftime("%B %d, %Y")
            print(date)
            speak("Sir the date is,"+date)
        elif "send email" in query:
            try:
               speak("Tell me what you want to send")
               content=takecmd()
               to="yashno25@gnail.com"
               sendEmail(to,content)
               speak("email send sucessfully")
            except Exception as e1:
                speak("sorry")
            
        elif('leave') in query:
            speak("weclome sir,  i am very glad to help you. i think your porblem had been sloved. good bye, sir")
            os.system("TASKKILL /F /IM pythonw.exe")
