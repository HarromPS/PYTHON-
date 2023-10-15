# # using shutil module copy this main file to two new folders
# import shutil

# # shutil.copy(src,dest): exact copy of a file, if exists override, matadata not preserved
# for i in range(10,12):
#     shutil.copy(f"A:\VS Codes\Programming\PYTHON\chapter9\Exercise9\main.py",f"A:\VS Codes\Programming\PYTHON\chapter9\Exercise{i}");


# Exercise 9
# -------------------
# write a program to pronounce a list of names using win32 api
# e.g list = ["amit", "amar", "raja"];
# Hello amit
# Hello amar
# Hello raja

from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

string = "A simple approach to introduce oneself or the guest speaker to a crowd is with an introduction speech. The primary goal is to capture the audience's interest by demonstrating your credibility";
lst = string.split(" ");
# print(lst);

for word in lst:
    speak(word);


# speak("Hello")
