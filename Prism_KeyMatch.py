import pygame
from pygame.locals import *
import random
import time
from Prism_sql import insert_score
from Prism_Resources import Key
pygame.init()

gameMusic = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_KeyMatcher_inGame.ogg')


#COLOURS
WHITE = (255,255,255)
BLACK = (0,0,0)
CYAN = (8,163,255)
YELLOW =(208,232,7)
RED = (255,51,21)
BLUE = (12,67,235)
GREEN = (105,255,8)

#TEXT

#IMAGES                                                                                                                                

keyBG = pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_KeyMatcherkeyBG.jpg')
keyBG = pygame.transform.scale(keyBG,(64,64))
howTo = pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_KeyMatcher_HowToPlay.jpg')
gameBG = pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_KeyMatcherBG.png')
getReady = pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_NewKeymatch_GetReady.png')
loseScreen = pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_KeyMatcher_LoseScreen.jpg')
startScreen = pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_KeyMatcher_StartScreen.jpg')
startScreen2 = pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_KeyMatcher_StartScreen1.jpg')
waitImg =  pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_KeyMatcher_WAIT.jpg')
goImg = pygame.image.load('Prism_assets/Prism_img/Prism_keyMatcher/Prism_KeyMatcher_GO.jpg')

#sound
loseSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_KeyMatcher_loseSound.wav')
loseSound.set_volume(0.1)
keySound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_KeyMatcher_correctKeySound.wav')
keySound.set_volume(0.3)
menuMusic = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_KeyMatcher_MainMusic.ogg')

#STARTING GAME STUFF

secs = 1.1
score = 0
pts = 0

#CLOCK
clock = pygame.time.Clock()

#FONT STUFF


#START

def infoGame(screen): # Explain to the user how to play the game
    global getReady, howTo, gameBG
    counter = 0
    timer = 0
    loop = True
    while loop:
        timer += 1
        counter += 1
        if counter == 20:
            counter = 0
        elif 0<= counter <= 10: # For this interval, display 'GET READY'
            getReadyImg = True
        elif 11 <= counter <= 20: # For this interval, don't ^^^
            getReadyImg = False
        screen.blit(howTo,(0,0))
        if getReadyImg == True:
            screen.blit(getReady,(0,0))
        else:
            screen.blit(howTo,(0,0))
        screen.blit(gameBG,(0,0))
        pygame.display.update()
        if timer == 150: # When the timer finishes, run the main game
            loop = False
    menuMusic.stop()
    val = runGame(screen)
    return val

def pressKey(key,pts): # Check if the user has pressed a key / the correct key.
    if key == 'a':
        ans = K_a
    elif key == 'b':
        ans = K_b
    elif key == 'c':
        ans = K_c
    elif key == 'd':
        ans = K_d
    elif key == 'e':
        ans = K_e
    elif key == 'f':
        ans = K_f
    elif key == 'g':
        ans = K_g
    elif key == 'h':
        ans = K_h
    elif key == 'i':
        ans = K_i
    elif key == 'j':
        ans = K_j
    elif key == 'k':
        ans = K_k
    elif key == 'l':
        ans = K_l
    elif key == 'm':
        ans = K_m
    elif key == 'n':
        ans = K_n
    elif key == 'o':
        ans = K_o
    elif key == 'p':
        ans = K_p
    elif key == 'q':
        ans = K_q
    elif key == 'r':
        ans = K_r
    elif key == 's':
        ans = K_s
    elif key == 't':
        ans = K_t
    elif key == 'u':
        ans = K_u
    elif key == 'v':
        ans = K_v
    elif key == 'w':
        ans = K_w
    elif key == 'x':
        ans = K_x
    elif key == 'y':
        ans = K_y
    elif key == 'z':
        ans = K_z

    for event in pygame.event.get(): # When the user presses a key, play a sound
        if event.type == KEYDOWN:
            keySound.play()
            
            if event.key == (ans): # If the user pressed the correct key, return that they passed
                pts = 'PASS'

                
            else:
                pts = 'FAIL'
        
    return pts

def gameScreen(screen): # Show the start menu of the game
    keyMatcher = screen # 
    menuMusic.set_volume(0.3)
    menuMusic.play(-1)
    run = True
    counter = 0
    while run: # Loop the game
        counter += 1
        if counter == 201: ## This IF SERIES determines whether or not to show the Text. To give the effect of a flashing screen
            counter = 0
        elif  0 <= counter <= 100:
            keyMatcher.blit(startScreen,(0,0))
        elif 101 <= counter <= 200:
            keyMatcher.blit(startScreen2,(0,0))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN: # If the user presses a key, stop the loop
                keySound.play()
                if event.key == K_ESCAPE:
                    run = False
                    
                else:
                    run = False

def runGame(screen): # Run the game
    global gameMusic,WHITE,BLACK,CYAN,YELLOW,RED,BLUE,GREEN,keyBG,gameBG,loseScreen,startScreen,startScreen2,loseSound,keySound,menuMusic,secs,score,pts,clock
    score = 0 # RESET SCORE ##BUGFIXING
    regularFont = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 32)
    gameFont = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 50)
    scoreFont = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 38)
    smallFont = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 18)
    loseText = scoreFont.render(str(score),True, RED)
    keyFont = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 64)
    keyMatcher = screen
    run = True
    gameMusic.set_volume(0.5)
    gameMusic.play(-1)
    while run:
        for event in pygame.event.get(): # Get user key input
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    gameMusic.stop()
                if event.key == K_ESCAPE:
                    keySound.set_volume(0)
                    loseSound.set_volume(0)
        if secs >0.1:
            secs -= 0.01
        else:
            secs = 0.4
        for event in pygame.event.get(): # Get user key input
            if event.type == KEYDOWN:
                keyMatcher.fill(BLACK)
                loseSound.play()
                keyMatcher.blit(loseScreen,(0,0))
                keyMatcher.blit(loseText,(428,297))
                pygame.display.update()
                gameMusic.stop()
                time.sleep(5)
            
                run = False
        pauseTime = int(secs * 500)
        keyMatcher.blit(waitImg,(0,0))
        keyMatcher.blit(gameBG,(0,0))
        
        pygame.display.update()
        
        for event in pygame.event.get():  # Get user key input
            if event.type == KEYDOWN:
                keyMatcher.fill(BLACK)
                loseSound.play()
                keyMatcher.blit(loseScreen,(0,0))
                keyMatcher.blit(loseText,(428,297))
                pygame.display.update()
                gameMusic.stop()
                time.sleep(5)
            
                run = False
            
            else:
                pass
        currentScore = gameFont.render(str(score), True, RED) 
        pygame.time.delay(pauseTime)
        keyMatcher.blit(goImg,(0,0))
        keyMatcher.blit(currentScore,(350,50))
        keyMatcher.blit(gameBG,(0,0))
        keyObj = Key()
        newKey = keyObj.genKey(keyBG,keyMatcher)   
        pygame.display.update() # Generate a new key
        
        time.sleep(secs)
        
        
        passFail = pressKey(newKey,pts) # Determine if the player has passed
        newScore = gameFont.render(str(score), True, RED)
        keyMatcher.blit(newScore,(338,25))
        pygame.time.delay(pauseTime)
        
        if passFail == 'PASS':
            score += 100
        else: # Lose Menu
            keyMatcher.fill(BLACK)
            loseSound.play()
            keyMatcher.blit(loseScreen,(0,0))
            keyMatcher.blit(loseText,(428,297))
            pygame.display.update()
            gameMusic.stop()
            time.sleep(5)
            
            run = False
        
        loseText = scoreFont.render(str(score),True, RED)
        insert_score('KeyMatcher', score) # Save highscore to Database
        pygame.display.update() # Update the screen again
        if score >= 1000:
            game = True
        else:
            game = False
            
    return game

def run(): # Function that runs the game. For use in arcade.py
    keyMatcher = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Prism')
    programIcon = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Logo.png')
    pygame.display.set_icon(programIcon)
    keyMatcher.blit(gameBG,(0,0))
    gameScreen(keyMatcher)
    game = infoGame(keyMatcher)
    return game # Return the value of if the user won or lost back to arcade.py
pygame.quit()