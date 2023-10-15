# Welcome to Robo Speaker Created by Hariom

import win32com.client

if __name__ == "__main__":      # means for this program, it starts from here
    speak = win32com.client.Dispatch("SAPI.SpVoice").Speak;
    while(True):
        user = input("Enter what you want to say: ");
        if(user == "q"):
            speak("program ends");
            break;
        speak(user);