# Exercise 10:
# Use NewsAPI and requests module to fetch the daily news related to different topics
import json
import requests

query = input("What news you want to see: ");
req = requests.get(f"https://newsapi.org/v2/everything?q={query}&from=2023-06-27&sortBy=publishedAt&apiKey=664a8ec6e80e485985913ddf2c481cdb");

with open("A:\VS Codes\Programming\PYTHON\chapter9\Exercise10\_news.txt",'a',encoding="utf-8") as f:
    s = json.loads(req.text);
    lst =[];
    f.write(f"Status: {s['status']}\n");
    f.write(f"Total News: {s['totalResults']}");

    for news in s["articles"]:
        n = news;
        f.write(f'\n\nSource Id: {n["source"]["id"]}\nSource Name: {n["source"]["name"]}\nAuthor: {n["author"]}\nTitle: {n["title"]}\nDescription: {n["description"]}\nURL: {n["url"]}\nURLtoImg: {n["urlToImage"]}\nPublished at: {n["publishedAt"]}\nContent: {n["content"]}\n-------------------------------------------------------------------------------');
