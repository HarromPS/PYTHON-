# Create a program to encrypt a message & decode a message the same message to original english message
# program should ask if want to code or decode


# Set of rules
# Coding
# if word contains atleast 3 chars, remove 1st letter and append it at the end now append three random
# characters at the starting and the end
# else simply reverse the string

def code():
    userInp = input("Enter your message\n=> ");
    lst = list(userInp);
    codedMsg="";
    if(len(userInp)>=3):
        strt = lst[0];
        lst.remove(strt);
        lst.insert(len(lst),strt);
        # OR lst.extend(strt);
        randChars = ('w','e','d','q','c','y');  # hard-coded tuple
        for i in range(6):
            if(i<3):
                lst.insert(0,randChars[i]);
            else:
                lst.insert(len(lst),randChars[i]);
    else:
        lst.sort(reverse=True);

    for chars in lst:
        codedMsg += chars;
    return codedMsg;



# Decoding
# if the word contains less than 3 characters , reverse it
# else remove 3 random characters from the start & end, now remove the last letter & append
# it to the start

def decode():
    userInp = input("Enter your message\n=> ");
    lst = list(userInp);
    decodedMsg="";
    if(len(userInp)>=3):
        for i in range(6):
            if(i<3):
                lst.remove(lst[0]);
            else:
                lst.remove(lst[len(lst)-1]);
        strt = lst[len(lst)-1];
        lst.remove(lst[len(lst)-1]);
        lst.insert(0,strt);
    else:
        lst.sort(reverse=True);

    for chars in lst:
        decodedMsg += chars;
    return decodedMsg;

# our application
def application():
    choice = input("1 for code\n0 for decode\n=> ");
    output='';
    if(choice=='1'):
        output=code();
    elif(choice=='0'):
        output=decode();
    else:
        print("Invalid Input Please Restart the application");

    print(output);

application();