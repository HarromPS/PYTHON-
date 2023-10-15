# Create a prompt to greet Good morning, Good afternoon, Good evening
# Use time module
import time

timestamp = time.strftime("%H:%M:%S");
print(timestamp);

# Note: time returns a string date , needed to typecast
hr = int(time.strftime("%H"));
min =int(time.strftime("%M"));
sec =int(time.strftime("%S"));

if(hr>=0 and hr<=12 ):
    print("Good Morning Sir");
elif(hr>12 and hr<=16 ):
    print("Good Afternoon Sir");
elif(hr>16 and hr<=19 ):
    print("Good Evening Sir");
elif(hr>19 and hr<=11 ):
    print("Good Night Sir");
else:
    print("Good Late Night Sir");
