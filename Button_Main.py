# Main Button

import sys
import random
import pygame
import button
import memory_puzzle
import level1
import level3
import pandas as pd
from pygame import mixer
from pygame.locals import *

# create display window
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
blue = (0,0,255)
green = (102,204,0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('Memory_Background1.jpg')  # Set the background image
pygame.display.set_caption('Memory Puzzle')

# load button images
level1_img = pygame.image.load('level1.png').convert_alpha()
level2_img = pygame.image.load('level2.png').convert_alpha()
level3_img=pygame.image.load('level3.png').convert_alpha()
exit_img = pygame.image.load('exit.jpg').convert_alpha()
Welcome_img = pygame.image.load('Welcome1.png').convert_alpha()
screenshot_img=pygame.image.load('screenshot_game.jpeg').convert_alpha()
scoresImg=pygame.image.load('highscores.jpg').convert_alpha()



# create button instances
Welcome_button = button.Button(30,20,Welcome_img,0.8)
level1_button = button.Button(30, 100, level1_img, 0.8)
level2_button = button.Button(30, 200, level2_img, 0.8)
level3_button=button.Button(30, 300, level3_img, 0.8)
exit_button = button.Button(400, 350, exit_img, 0.8)
scoresButton=button.Button(200, 300, scoresImg, 0.8)

userID="User"+str(random.randint(1000,25000000))


def Scores():
    
    "displays score board."
    
    scoreDF=pd.read_csv("scoreboard.csv")
    
    scoreDF=scoreDF.sort_values(by=["Level","TimeTaken"])
    
    scoreDF["Level"]=[int(x) for x in list(scoreDF["Level"])]
    
    levels=[1,2,3]
    
    scores=[]
    
    for level in levels:
        
        scores.append("".ljust(40,"*"))
        
        scoresTop3=list(scoreDF["Time"][scoreDF.index[scoreDF["Level"]==level]])
        
        usersTop3=list(scoreDF["UserID"][scoreDF.index[scoreDF["Level"]==level]])[:3]
        
        for i in range(len(usersTop3)):
            
            scores.append("  Level:%s"%str(level)+" | "+"User:%s"%str(usersTop3[i]).ljust(20," ")+" | "+"Score:%s"%str(scoresTop3[i]))
            
            
     
    
    return scores


def ScoreBoard():
    
    "displays score board"
    
    pygame.init()
    
    screen= pygame.display.set_mode((600, 500))
    
    fontScore=pygame.font.Font("freesansbold.ttf",20)
    
    pygame.display.set_caption('Score Board.')
    
    backIcon=pygame.image.load("back.png")
    
    scores=Scores()
    
    backPos=(300,450)    
    
    while True:
        
        screen.fill((60,60,100)) # drawing the window
        
        # scores render
        
        posY=0
        
        for score in scores:
            
            #print(score)
            
            posY+=30
    
            textScore=fontScore.render(score,True,(255,255,255))          
        
            screen.blit(textScore,(50,posY))
        
        screen.blit(backIcon,backPos)
        
        
        for event in pygame.event.get():
            
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                
                return None

            elif event.type == MOUSEBUTTONUP:
                
                x,y = event.pos                                
                
                if backPos[1]<=y<=backPos[1]+50 and backPos[0]<=x<=backPos[0]+50:
                    
                    return None
        
        pygame.display.update()

# game loop

run = True
while run:

    screen.fill((202, 228, 241))
    screen.blit(background, (0, 0))
    
    screen.blit(screenshot_img,(375,100))

    if Welcome_button.draw(screen):
        print('Welcome to memory puzzle!!')

    if level1_button.draw(screen):
        
        resp=level1.main(userID)
        
        mixer.music.load('Background.wav') # initialized background music
        
        mixer.music.play(-1) # playing music continously
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        pygame.display.set_caption('Memory Puzzle')
        
        
    if level2_button.draw(screen):
        
        resp=memory_puzzle.main(userID)
        
        mixer.music.load('Background.wav') # initialized background music

        mixer.music.play(-1) # playing music continously
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Memory Puzzle')
     
    if level3_button.draw(screen):
        
        resp=level3.main(userID)
        
        mixer.music.load('Background.wav') # initialized background music

        mixer.music.play(-1) # playing music continously
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Memory Puzzle')
        
        
    
    if scoresButton.draw(screen):
        
        resp=ScoreBoard()
        
        mixer.music.load('Background.wav') # initialized background music

        mixer.music.play(-1) # playing music continously
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Memory Puzzle')
        
        
        
    
    
    if exit_button.draw(screen):
        print('EXIT')
        sys.exit(0)
    if level3_button.draw(screen):
        pass
    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
