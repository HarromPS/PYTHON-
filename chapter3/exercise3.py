# Exercise: Koun Banega Crorepati
# Use list datatype to store the questions and theire correct answers, Display the final amount the
# person is taking home after playing the game

# score
score=0;

# answer validation function
def validate(ans):
    print("\nYour Answer ==> ",sep="",end=" ");
    a = input();
    if(ans==a):
        return 1;
    else:
        return 0;

# lets play
def play():

    # our storage of questions and answers
    computerji = [
        ["What is the Capital of India?","\na) Delhi\nb) Mumbai\nc) Kolkata\nd) Hydrabad","a"],
        ["Which of the following is the National Language of India?","\na) Hindi\nb) Telgue\nc) Marathi\nd) English","a"],
        ["Who is the current Prime Minister of India?","\na) Rahul Gandhi\nb) Sonia Gandhi\nc) Narendra Modi\nd) Manmohan Singh","c"],
        ["Which of the following is the highest mountain peak in the world?","\na) Kangchenjunga\nb) K2\nc) Lhotse\nd) Mount Everest","d"],
        ["Who is the author of the book 'Gandhi: His Life and Message'","\na) Jawaharlal Nehru\nb) Louis Fischer\nc) Mahadev Desai\nd) Vinoba Bhave","b"],
        ["Which of the following is the National Game of India?","\na) Cricket\nb) Football\nc) Badminton\nd) Hockey","d"],
        ["Which of the following is the National Anthem of India?","\na) Sarva Dharma Sambhava\nb) Ashoka Chakra\nc) Vande Mataram\nd) Jana Gana Mana","d"],
        ["Which of the following is the National Dish of India?","\na) Pulav\nb) Dosa\nc) Naan\nd) Biryani","d"],
        ["Who is the National Animal of india?","\na) Lion\nb) Tiger\nc) Elephant\nd) Fox","b"],
        ["What is the National Fruit of india?","\na) Mango\nb) Banana\nc) Apple\nd) Orange","a"],
    ];

    rs=20000;
    for i in range(10):
        # question and answer
        print("** Question for",rs," **\n");
        rs=rs*2;
        print(i+1,") ",computerji[i][0],computerji[i][1],sep="");
        x=validate(computerji[i][2]);
        print();
        if(x==1):
            # just googled
            global score;
            score=rs;
        else:
            break;
    return i+1;

print("\n\t---- Welcome to Kaun Banega Crorepati ----\n");
print("\t\tThere will be 10 Questions");
print("\tChoose 1 correct from 4 options a/b/c/d\n\t\t  Best of Luck\n");
print("Press 5 to start");

strt = int(input("==> "));
if(strt==5):
    result=play();
else:
    print("------ END ----");

print("\n\tThank You for playing Kaun Banega Crorepati");
print("\n\tQuestions Answered",result,"\n\tYou Won Rs.",score,'\n');