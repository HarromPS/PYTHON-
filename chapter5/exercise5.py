import random
# Snake Water Gun

# snake 0, water 1, gun 2
def validate(user,computer):

    # draw the game if user and computer chooses same choice
    if(user==computer):
        return "Draw";

    validate_data =[
        [0,1,"user"],     # s-w (user-computer) (snake)
        [0,2,"comp"],     # s-g    (gun)
        [1,2,"user"],     # w-g    (water)
        [1,0,"comp"],     # w-s    (snake)
        [2,0,"user"],     # g-s    (gun)
        [2,1,"comp"]     # g-w    (water)
    ];


    for condition in validate_data:
        if((user==condition[0]) and (computer==condition[1])):
            return condition[2];    # return name of who won
    return -1;

def play():

    # start the game
    strt = int(input("Press 5 to Start\nPress 0 to Cancel\n=>"));
    if(strt==5):
        while(True):
            print("\n0 - snake\t1 - water\t2 - gun");
            usr = int(input("\nEnter your choice=> "));
            comp=random.randrange(0,3);

            # print(comp)
            if(usr>=0 and usr<=2):
                res = validate(usr,comp);
                if(comp==0):
                    val="snake";
                elif(comp==1):
                    val="water";
                elif(comp==2):
                    val="gun";

                if(res=="user"):
                    print(f"\nComputer: {val}\n-----You Won-----\n");
                elif(res=="comp"):
                    print(f"\nComputer: {val}\n-----You Lose-----\n");
                elif(res=="Draw"):
                    print(f"\nComputer: {val}\n-----Game {res}-----\n");
                strt = int(input("\nPress 5 to Restart\nPress 0 to End\n=> "));

                if(strt!=5):
                    break;
            else:
                strt = int(input("\n\nInvalid Input\nPress 5 to Restart\nPress 0 to End\n=> "));
                if(strt!=5):
                    break;

# exception handeling
try:
    play();
    print("\nThank you for playing the game\n");
except Exception as e:
    print("\nSomething Went Wrong ... \n");
