import random;      # generates randoms
import sys;         # variables for controling inputs & outputs
import pygame;      # basic imports of pygame
from pygame.locals import *;      # imports everything

# Global variables for the game
FPS = 32;
SCREENWIDTH = 289;      # ADJUSTED RESOLUTION FOR MOBILE VIEW
SCREENHEIGHT = 511;

# pygame.display.set_mode = initialize a window or screen fOR display
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT));

# base image for the game
GROUNDY = SCREENHEIGHT * 0.8;    # 80% of screen height

# objects/dictionary
GAME_IMAGES = {};
GAME_SOUNDS = {};
PLAYER = 'imgs/bird.png';
BACKGROUND ='imgs/background.png';
PIPES = 'imgs/pipe.png';


# Functions of our game
def welcomeScreen():

    # positions of the headings & images of a starting screen of the display screen

    # position of player(bird) in XY
    playerx = int(SCREENWIDTH/5);
    playery = int(SCREENHEIGHT - GAME_IMAGES["player"].get_height()/2);  # centre

    # position of message box in XY
    messX = int((SCREENWIDTH -GAME_IMAGES["message"].get_width())/2);
    messY = int(SCREENHEIGHT * 0.13);

    # position of base ground in XY
    basex = 0;      # tounched to the base

    # Events in program like keyboard/mouse
    while(True):
        # get the events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit();
                sys.exit();

            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return;

            else:
                # blits(shows/renders) the images
                SCREEN.blit(GAME_IMAGES["background"], (0,0));
                SCREEN.blit(GAME_IMAGES["player"], (playerx,playery));
                SCREEN.blit(GAME_IMAGES["message"], (messX,messY));
                SCREEN.blit(GAME_IMAGES["base"], (basex,GROUNDY));

                # change the screen as the function runs until screen will not change
                pygame.display.update();

                # control the FPS
                FPSCLOCK.tick(FPS);

# random pipe generator
def getRandomPipe():
    # one for upside down
    # one for straight

    pipeHeight = GAME_IMAGES["pipe"][0].get_height();
    offSet = SCREENHEIGHT/3;
    y2 = offSet + random.randrange(0,int(SCREENHEIGHT - GAME_IMAGES['base'].get_height() - (1.2)*offSet));
    y1 = pipeHeight - y2 + offSet;
    pipeX = SCREENWIDTH + 10;

    # pipe list
    pipe = [
        {'x': pipeX, 'y': -y1},  # upper pipe
        {'x': pipeX, 'y': y2}  # lower pipe
    ];

    return pipe;

# function to check if the collision is occured
def isCollide(playerx, playery, upperPipe,lowerPipe):
    if playery > GROUNDY - 25 or playery < 0:
        GAME_SOUNDS['hit'].play();
        return True;

    # for pipe in upperPipe:
    #     pipeHeight = GAME_IMAGES['pipe'][0].get_height();
    #     if(playery < pipeHeight + pipe['y'] and (abs(playerx - pipe['x']) < GAME_IMAGES['pipe'][0].get_width())):
    #         GAME_SOUNDS['hit'].play();
    #         return True;

    # for pipe in lowerPipe:
    #     if((playery +  GAME_IMAGES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_IMAGES['pipe'][0].get_width()):
    #         GAME_SOUNDS['hit'].play();
    #         return True;

    return False;


# main game play
def mainGame():
    score = 0;
    playerx = int(SCREENWIDTH/5);
    playery = int(SCREENWIDTH/2);   # center
    basex = 0;

    # generate random pipes for blitting on screen
    Pipe1 = getRandomPipe();
    Pipe2 = getRandomPipe();

    # list of upper pipes
    upperPipe = [
        {'x': SCREENWIDTH + 200, 'y':Pipe1[0]['y']},
        {'x': SCREENWIDTH + 200 +(SCREENWIDTH/2), 'y':Pipe2[0]['y']}
    ];

    # list of lower pipes
    lowerPipe = [
        {'x': SCREENWIDTH + 200, 'y':Pipe1[1]['y']},
        {'x': SCREENWIDTH + 200 +(SCREENWIDTH/2), 'y':Pipe2[1]['y']}
    ];

    # pipe velocities
    pipeVelocity_X = -4;  # reversed speed

    playerVel_Y = -9;
    playerMaxVel_Y= 10;
    playerMinVel_Y= -8;
    playerAcc_Y= 1;

    # velocity while flapping
    playerFlapAcc = -8;

    # true when bird is flapping
    playerFlapped = False;

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVel_Y = playerFlapAcc;
                    playerFlapped = True;
                    GAME_SOUNDS['wing'].play();

        # check collision
        crash = isCollide(playerx, playery, upperPipe,lowerPipe);
        if crash:
            return;

        # check for the score
        playerMidPos = playerx + GAME_IMAGES['player'].get_width()/2;
        for pipe in upperPipe:
            pipeMidPos = pipe['x']+ GAME_IMAGES['pipe'][0].get_width()/2;
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score+=1;
                print(f"Your Score is {score}");
            GAME_SOUNDS['point'].play();

        if playerVel_Y < playerMaxVel_Y and not playerFlapped:
            playerVel_Y += playerAcc_Y;

        if playerFlapped:
            playerFlapped = False;

        playerHeight = GAME_IMAGES['player'].get_height();
        playery += min(playerVel_Y, GROUNDY - playery - playerHeight);

        # moving pipes to left
        for upperpipe, lowerpipe in zip(upperPipe,lowerPipe):
            upperpipe['x'] += pipeVelocity_X;
            lowerpipe['x'] +=pipeVelocity_X;

        # add a new pipe when 1st pipe is about to cross the leftmost part of the screen
        if 0 < upperPipe[0]['x']<5:
            newpipe = getRandomPipe();
            upperPipe.append(newpipe[0]);
            lowerPipe.append(newpipe[1]);

        # if pipe is out of screen, remove it
        if upperPipe[0]['x'] < -GAME_IMAGES['pipe'][0].get_height():
            upperPipe.pop(0);
            lowerPipe.pop(0);

        # lets blit our images
        SCREEN.blit(GAME_IMAGES['background'], (0,0));

        for upperPipe, lowerPipe in zip(upperPipe, lowerPipe):
            SCREEN.blit(GAME_IMAGES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_IMAGES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_IMAGES['base'], (basex,GROUNDY));
        SCREEN.blit(GAME_IMAGES['player'], (playerx,playery));

        # score digits in a list string format
        myDigits = [int(x) for x in list(str(score))];
        width = 0;
        for digit in myDigits:
            width += GAME_IMAGES['numbers'][digit].get_height();
        xOffSet = (SCREENWIDTH - width)/2;      # center of screen(1st digit)

        for digits in myDigits:
            SCREEN.blit(GAME_IMAGES['numbers'][digit], (xOffSet, SCREENHEIGHT*0.12));
            xOffSet += GAME_IMAGES['numbers'][digit].get_width();   # 2nd digits

        # updating the screen
        pygame.display.update()
        FPSCLOCK.tick(FPS);


# main runs if the program runs from the same code(this code)
if __name__ == "__main__":
    # Game starts

    # initialize the game modules
    pygame.init()

    # when clock.tick is clicked fps will not increase to 40
    FPSCLOCK = pygame.time.Clock(); # controls FPS

    # images keys - images values is a tuple
    GAME_IMAGES['numbers'] = (
        pygame.image.load("imgs/0.png").convert_alpha(),       # convert_alpha controls px & opacity
        pygame.image.load("imgs/1.png").convert_alpha(),
        pygame.image.load("imgs/2.png").convert_alpha(),
        pygame.image.load("imgs/3.png").convert_alpha(),
        pygame.image.load("imgs/4.png").convert_alpha(),
        pygame.image.load("imgs/5.png").convert_alpha(),
        pygame.image.load("imgs/6.png").convert_alpha(),
        pygame.image.load("imgs/7.png").convert_alpha(),
        pygame.image.load("imgs/8.png").convert_alpha(),
        pygame.image.load("imgs/9.png").convert_alpha()
    );

    # message key
    GAME_IMAGES['message'] = pygame.image.load("imgs/message.png").convert_alpha();

    # ground key
    GAME_IMAGES['base'] = pygame.image.load("imgs/base.png").convert_alpha();

    # pipe key
    GAME_IMAGES['pipe'] =(
        # upside down
        pygame.transform.rotate(pygame.image.load(PIPES).convert_alpha(), 180),
        pygame.image.load(PIPES).convert_alpha()
    )

    # background
    GAME_IMAGES['background'] = pygame.image.load(BACKGROUND).convert_alpha();

    # player
    GAME_IMAGES['player'] = pygame.image.load(PLAYER).convert_alpha();

    # game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound("sounds/die.wav");
    GAME_SOUNDS['hit'] = pygame.mixer.Sound("sounds/hit.wav");
    GAME_SOUNDS['point'] = pygame.mixer.Sound("sounds/point.wav");
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound("sounds/swoosh.wav");
    GAME_SOUNDS['wing'] = pygame.mixer.Sound("sounds/wing.wav");

    # GAME LOOP
    while(True):
        # main screen
        welcomeScreen();

        # main game
        mainGame();