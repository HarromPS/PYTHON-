import requests # like fetch - get/post requests

# get requests
r = requests.get("https://www.google.com");
# r = requests.get("'https://jsonplaceholder.typicode.com/todos/1");
# print(r.text);

# post request
url = "https://jsonplaceholder.typicode.com/posts";
headers = {
    'Content-type': 'application/json; charset=UTF-8'
};

data = {
    'title': 'Title',
    'body': 'This is a body',
    'userId': '100'
};

response = requests.post(url, headers=headers,json=data);
print(response.text);