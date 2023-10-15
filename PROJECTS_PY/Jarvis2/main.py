# Cloning Jarvis 1

import datetime
import wikipedia
import webbrowser
import os
import random

# module for sending emails
import smtplib

# module for speech recognition
import speech_recognition as spRec

# text to speech recognition module
import pyttsx3

# initialize the speech api
engine = pyttsx3.init("sapi5");

# get the audio of the engines
voice = engine.getProperty("voices");
# voice[0].id;
# voice[1].id;

# set the voice 0 or 1
engine.setProperty("voices",voice[0].id);

# speak function
def speak(text):
    ''' Speaking the text as audio'''
    engine.say(text);

    # wait until all the text is spoken
    engine.runAndWait();

# wishing function
def wish():

    # returns a string
    hour = int(datetime.datetime.now().hour);
    if(hour>=0 and hour<=12):
        speak("good morning");
        print("good morning");
    elif (hour>12 and hour<=17):
        speak("good afternoon");
        print("good afternoon");
    elif (hour>17 and hour<=19):
        speak("good evening");
        print("good evening");
    elif (hour>19 and hour<=24):
        speak("good night");
        print("good night");

# implementing speech recognition functions from user inputs
def userCommands():
    # creating a object for speech recognition
    recognizer = spRec.Recognizer();

    # opening Microphone
    with spRec.Microphone() as Mic:

        # adjusting pause time
        recognizer.pause_threshold = 1;

        # getting audio
        print("Listening ...");
        audio = recognizer.listen(Mic);

        # recognizing the audio using google cloud audio ercognizer
        try:
            print("\n\nRecognizing ...");
            query = recognizer.recognize_google(audio,language='en-in');
            print(query);
            return query;
        except:
            print("Audio Recognition Falied\nTry Again");
            speak("I dont understand please say that again");
            return "None";

contacts = {
    "amit": "123amit@gmail.com",
    "pavan": "pavan123@gmail.com",
    "tanaj": "wewe@gmail.com"
};

# function to send emails
def sendMail(to,contact):
    server = smtplib.SMTP("smtp.gmail.com",587);

    # say hi
    server.ehlo();
    # secure connection
    server.starttls();

    # login
    pswd = "";
    with open("../Jarvis/imp.txt") as f:
        for chars in f:
            pswd+=chars;

    server.login("2021bit046@gmail.com",pswd);      # login from sending account
    server.sendmail("2021bit046@sggs.ac.in", to ,contact);
    server.close();


if __name__ == "__main__":
    wish();
    speak(f"hi I am jarvis");

    # tasks to perform
    while True:
        query = userCommands();

        # if query=="None":
        #     continue;

        # to make it speak
        if "say" in query:
            query.repalce("say","");
            speak(query);
        elif "speak" in query:
            query.repalce("speak","");
            speak(query);

        # show time
        elif "the time" in query:
            tm = datetime.datetime.now().strftime("%H: %M :%S");
            speak(f"current time is {tm}");


        # to search something from wikipedia
        elif "wikipedia" in query:
            speak("searching wikipedia ");
            query.repalce("wikipedia","");
            results = wikipedia.summary(query,sentences = 1);
            print(results);
            speak(f"According to wikipedia, {results}");

        # opening any webpage
        elif "open google" in query:
            webbrowser.open("www.google.com");

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com");

        elif "open leetcode" in query:
            webbrowser.open("www.leetcode.com");

        elif "open geeksforgeeks" in query:
            webbrowser.open("www.geeksforgeeks.com");

        # open code using os module
        elif "code" in query:
            vscode = "C:\\Users\\shivh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe";
            os.startfile(vscode);

        # play music
        elif "play music" in query:
            songs = os.listdir("A:\\VS Codes\\Programming\\PYTHON\\chapter5\\modules\\os_module\\music\\list");
            rand = random.randrange(0,len(songs));
            os.startfile(os.path.join(songs, songs[0]));

        # sending emails
        elif "send mail" in query:
            try:
                speak("Whom to send");
                _to = userCommands();
                speak("What to send");
                person = userCommands();
                for keys in contacts:
                    if(keys in person):
                        sendMail(_to,person);
                        print("\n\nEmail sent Successfully");
                        speak("Email sent Successfully");
                        break;

            except Exception :
                print("Email Not Sent\nRetry");
                speak("email sending failed");

        elif 'quit' in query:
            speak("Program ends");
            break;

        else:
            results = wikipedia.summary(query,sentences = 1);
            print(results);
            speak(f"According to wikipedia, {results}");
