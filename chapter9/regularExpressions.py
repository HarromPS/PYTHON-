# Regular Expressions: for finding complex patterns

import re

pattern = r"[A-Z a-z]ing";      # r""  raw string(ignores escape seq chars)
text = "Companies can also use Web scraping for email marketing. They can collect Email ID’s from various sites using web scraping and then send bulk promotional and marketing Emails to all the people owning these Email ID’s."
# 1) re.search(pattern, text); -> 1st occurance
matches = re.search(pattern, text);
print(matches);

matches = re.finditer(pattern,text);
for items in matches:
    print(items,items.span());
    print(text[items.span()[0]:items.span()[1]]);