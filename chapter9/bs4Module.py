# bs4 module: used in web scrapping
# beautiful soup module, a python library to pull out HTML & XML files
# A parser to provide idomatic ways of navigating searching, navigating, modifying the parser tree

import requests
from bs4 import BeautifulSoup

res =requests.get("https://www.google.com");

# create a soup -> create tree lijke HTML structure from response.text
soup = BeautifulSoup(res.text, 'html.parser');

# print(soup);
# print(soup.prettify());   # beautifies the HTML tree

for heading in soup.find_all("span"):
    print(heading.text);
