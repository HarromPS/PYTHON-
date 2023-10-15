# Jarvis Project

import os
import smtplib      # mail sending module
import datetime
import wikipedia    # wikipedia module (pip install wikipedia)
import webbrowser   # to do operations related to browser

# speech recognizer library
import speech_recognition as sr

# module/library used for text to speech conversion
import pyttsx3

# sapi 5 is a speech api by microsoft (in built voice in windows)
engine = pyttsx3.init("sapi5");

# get all the voices from the windows
voices = engine.getProperty("voices");

# print(v\n\noices[0].id);  only 0 & 1 indexed is present

# set the voice in the engine
engine.setProperty("voices", voices[0].id);

def speak(audio):
    ''' Gives the output as voice '''

    engine.say(audio);
    engine.runAndWait();

contacts = {
    "amit": "123amit@gmail.com",
    "pavan": "pavan123@gmail.com",
    "tanaj": "wewe@gmail.com"
};

# sending mails
def sendMail(to, contact):
    # hover to know more
    server = smtplib.SMTP("smtp.gmail.com", 587);
    server.ehlo();  # say hello
    server.starttls();  # secure connection
    pswd = ""
    with open("imp.txt",'r') as f:
        for txt in f:
            pswd+=txt;
    print(pswd);

    server.login("2021bit046@gmail.com",pswd);      # login from sending account
    server.sendmail("2021bit046@sggs.ac.in", to ,contact);
    server.close()
    pass

def wish():
    ''' Wishes Good Morning, Good AfterNoon, Good Evening, Good Night as per time'''

    # returns String of current time (0-12 or 13-23)
    hour = int(datetime.datetime.now().hour);
    # print(h\n\nour);

    if(hour>=0 and hour<=12):
        print("\n\nGood Morning!");
        return "Good Morning";
    elif(hour>12 and hour<=17):
        print("\n\nGood AfterNoon!");
        return "Good AfterNoon";
        return "Good AfterNoon";
    elif(hour>17 and hour<=19):
        print("\n\nGood Evening!");
        return "Good Evening";
    elif(hour>19 and hour<=24):
        print("\n\nGood Night!");
        return "Good Night";

def takeCommand():
    ''' Takes user input from microphone & returns string output'''
    r = sr.Recognizer();

    # get the user input from microphone
    with sr.Microphone() as source:
        print("\n\nListening ...");
        r.pause_threshold=1;        # seconds of non speaking audio

        # spoken audio
        audio = r.listen(source);

    # using try except to aviod crashing of program
    try:
        print("\n\nRecognizing ...");

        # use google recognizer- uses google cloud to recognize the audio
        query = r.recognize_google(audio, language="en-in");
        print(f"User said: {query}",type(query));
        return query;

    except Exception as e:
        # print(e\n\n);
        print("\n\nSay that again please... ");
        return "None";

if __name__ == "__main__":
    speak(f"{wish()} I am Jarvis");

    # Continuously taking user commands until user stops jarvis
    while (True):
        speak("Tell me a command");
        # for better recog. use lowercase
        query = takeCommand().lower();

        # logic for various tasks to execute
        if "wikipedia" in query:
            speak("searching wikipedia ...");
            query = query.replace("wikipedia","");  # replace wikipedia word from query
            results = wikipedia.summary(query, sentences=2);
            print(f"\n\n{results}");
            speak(results);

        # open google
        elif 'open google' in query:
            webbrowser.open("google.co.in");

        # open youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com");

        # open stackoverflow
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com");

        # play music
        elif 'play music' in query:
            # escape single slash character else gives path error
            path = os.listdir("list");
            song = path[0];
            os.startfile(os.path.join(path, song));

        # show time
        elif 'the time' in query:
            srtTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(srtTime);

        # open code
        elif 'open code' in query:
            code = "C:\\Users\\shivh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe";
            os.startfile(code);

        # send emails
        elif 'email to' in query:
            try:
                speak("whom to send?");
                _to = takeCommand();
                speak("what to send?");
                # person = contacts[_to];
                person = 'shivhareharry99@gmail.com'; # e.g from dict
                sendMail(_to,person);
                print("\n\nEmail sent Successfully");
                speak("Email sent Successfully");
            except Exception as e:
                print("\n\nEmail send Failed");

        elif 'quit' in query:
            speak("Ending Program");
            break;
