#Name: Maged Armanios, Sebastian Deluca, Alden Demello, Adam Grabowsky
#Date: April 14th, 2020
#File Name: Prism_main.py
#Description: Prism_main.py is the connecting file for all of prism's games. 
#Prism is a videogame created in pygame and is based around the theme 
#'Light and Dark'. It features a young boy named Dylan stuck in an arcade 
#and to get out, he has to play his way out!
#Prism is designed to be small, replayable 


################################################################################
'''
  _____                            _       
 |_   _|                          | |      
   | |  _ __ ___  _ __   ___  _ __| |_ ___ 
   | | | '_ ` _ \| '_ \ / _ \| '__| __/ __|
  _| |_| | | | | | |_) | (_) | |  | |_\__ \
 |_____|_| |_| |_| .__/ \___/|_|   \__|___/
                 | |                       
                 |_|          
'''

#Imports 

import pygame
from pygame.locals import *
from Prism_Resources import Button, fade_in, fade_out, TextInput
import Prism_Arcade as arcade
import webbrowser
from Prism_sql import *

################################################################################

#Initialize Pygame
pygame.mixer.pre_init(16000,-16,2, 1024 * 3)
pygame.init()
#pygame.font.init()
pygame.mixer.init(16000)
################################################################################
'''
   _____      _                      
  / ____|    | |                     
 | |     ___ | | ___  _   _ _ __ ___ 
 | |    / _ \| |/ _ \| | | | '__/ __|
 | |___| (_) | | (_) | |_| | |  \__ \
  \_____\___/|_|\___/ \__,_|_|  |___/
'''                                     

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
D_GREEN = (48, 110, 3)
BLUE = (12,67,235)


################################################################################
'''
 __      __        _       _     _           
 \ \    / /       (_)     | |   | |          
  \ \  / /_ _ _ __ _  __ _| |__ | | ___  ___ 
   \ \/ / _` | '__| |/ _` | '_ \| |/ _ \/ __|
    \  / (_| | |  | | (_| | |_) | |  __/\__ \
     \/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
'''

#Screen 
loginHeight = 600
loginWidth = 800
loginScreen = pygame.display.set_mode((loginWidth, loginHeight))
pygame.display.set_caption('Prism')
programIcon = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Logo.png')

pygame.display.set_icon(programIcon)

#Clock
clock = pygame.time.Clock()

#Game Variables
run = True
#mode = 'welcome'
get_name = False

#Assets
loginImg = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_BG.jpg')
logo = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Logo.png')
logo = pygame.transform.scale(logo,(256,256))
helpImg = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_HelpBG.png')
helpImg2 = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_HelpBG2.png')
helpImg3 = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Main_Credit.jpg')
bg = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_BG.jpg')
fooLogo = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_FooLogo.png')
pyLogo = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_PygamePowered.png')
btnSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/button.wav')
menuMusic = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_MenuMusic.ogg')
prismOptions = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Options.png')
prismQuit = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Quit.png')
statsBG = pygame.image.load('Prism_assets/Prism_img/Prism_Stats/Prism_Stats.jpg')
statsSITD = pygame.image.load('Prism_assets/Prism_img/Prism_Stats/Prism_SITD.png')
statsKM = pygame.image.load('Prism_assets/Prism_img/Prism_Stats/Prism_STATS_KM.png')
statsLP = pygame.image.load('Prism_assets/Prism_img/Prism_Stats/Prism_STATS_LP.png')
statsSB = pygame.image.load('Prism_assets/Prism_img/Prism_Stats/Prism_STATS_SB.png')
userImg = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Main_Username.jpg')
resetImg = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Reset.png')
restartImg = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Restart.png')

################################################################################

'''
  ______                _   _                 
 |  ____|              | | (_)                
 | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
'''                                              
#Get username from the database

def get_username():
    check_name = username_set()
    
    if check_name == 1:
        return 'welcome'
    elif check_name == 0:
        return 'get_name'

#Open website to the faq page
def open_site():
    webbrowser.open('https://sites.google.com/view/foogames/games/prism/faq')

#Loading screen function to play a cool intro.
def loading_screen(img, img2):
    global bg
    runLoading = True 
    while runLoading: #While true
        #Make changes to the screen
        loginScreen.blit(bg, (0,0))
        loginScreen.blit(img, (0,0))
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runLoading = False
        #Make changes to the display
        pygame.display.update()
        pygame.time.delay(2000)
        #Fade function for the transistions
        fade_out(loginWidth, loginHeight, loginScreen)
        fade_in(loginWidth, loginHeight, loginScreen)
        loginScreen.blit(bg, (0,0))
        loginScreen.blit(img2, (0,0))
        #Update display
        pygame.display.update()
        pygame.time.delay(1000)
        runLoading = False #Disable loop

#Function to get the music values from the database and change the buttons accordingly

def musicPlay(musicBtn):
    playMusic = get_setting('Music') #Get value from database
    if playMusic == 0: #If met change the buttons
        change_setting('Music', 1)
        musicBtn.text = 'OFF'
        musicBtn.text_colour = RED
    elif playMusic == 1: #If met change the buttons
        change_setting('Music', 0)
        musicBtn.text = 'ON'
        musicBtn.text_colour = D_GREEN

#Function to get the sound values from the database and changes the buttons accordingly

def playSound(soundFXBtn):
    soundFX = get_setting('Sounds') #Get values from the database
    if soundFX == 0: #If met change the buttons
        change_setting('Sounds', 1)
        soundFXBtn.text = 'OFF'
        soundFXBtn.text_colour = RED
    elif soundFX == 1:#If met change the buttons
        change_setting('Sounds', 0)
        soundFXBtn.text = 'ON'
        soundFXBtn.text_colour = D_GREEN

#Functions to return values based on the values in the database

def getSound():
    sound = get_setting('Sounds')
    if sound == 0:
        return True
    elif sound == 1:
        return False

def getMusic():
    music_vol = get_setting('Music')
    if music_vol == 0:
        return 0.3
    elif music_vol == 1:
        return 0

################################################################################

'''
   _____                      
  / ____|                     
 | |  __  __ _ _ __ ___   ___ 
 | | |_ |/ _` | '_ ` _ \ / _ \
 | |__| | (_| | | | | | |  __/
  \_____|\__,_|_| |_| |_|\___|
'''
menuMusic.play(-1) #Play music infinitely
vol = getMusic() #Get volume from the music function
menuMusic.set_volume(vol) #Set the volume
loading_screen(fooLogo,pyLogo) #Call the loading screen
# variables for changing stuff in the game
sCount = 2
fxCount = 2
move = 10

#Load fonts 

font = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf',16)
font2 = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 32)
#Create buttons
musicBtn = Button(215, 300, 'ON', D_GREEN, 150, 50, loginScreen)
soundFXBtn = Button(435, 300, 'ON', D_GREEN, 150, 50, loginScreen)
#Get the sound
soundText = getSound()

if soundText == True: #If met change the values of the buttons
    soundFXBtn.text = 'ON'
    soundFXBtn.text_colour = D_GREEN
elif soundText == False: #If met change the values of the buttons
    soundFXBtn.text = 'OFF'
    soundFXBtn.text_colour = RED
#Get music playback
musicPlayBack = getMusic()
if musicPlayBack == 0.3: #If met change the values of the buttons
    musicBtn.text = 'ON'
    musicBtn.text_colour = D_GREEN
elif musicPlayBack == 0: #If met change the values of the buttons
    musicBtn.text = 'OFF'
    musicBtn.text_colour = RED

mode = get_username() #Check to see if the username has been set

while run: #Main Game loop
    soundFX = getSound() #Get the soundfx
    vol = getMusic() #Get the volume
    if soundFX == True: #If met change the values of the buttons
        soundFXBtn.text = 'ON'
        soundFXBtn.text_colour = D_GREEN
    elif soundFX == False:#If met change the values of the buttons
        soundFXBtn.text = 'OFF'
        soundFXBtn.text_colour = RED
    if vol == 0.3:#If met change the values of the buttons
        musicBtn.text = 'ON'
        musicBtn.text_colour = D_GREEN
    elif vol == 0: #If met change the values of the buttons
        musicBtn.text = 'OFF'
        musicBtn.text_colour = RED

    if mode == 'get_name': #Get name mode to get the name of the usewr
        username = TextInput(text_color=(WHITE)) #Create a TextInput object
        name_got = False 
        while name_got == False: #While conditions are met
            #Make changes to the screen
            loginScreen.blit(userImg, (0,0))
            #Create a button and draw it
            continueBtn = Button(325, 400, 'CONTINUE', BLUE, 150, 50, loginScreen)
            continueBtn.draw()
            events = pygame.event.get()
            #Event checker
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #If the user left clicks on a button
                    if continueBtn.btn.collidepoint(event.pos):
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        mode = 'welcome' 
                        save_username(username.input_string, 1)
                        name_got = True
                
                elif event.type == pygame.KEYDOWN: #If the user presses down on a key
                    if event.key == K_RETURN:
                        mode = 'welcome'  
                        save_username(username.input_string, 1)
                        name_got = True

                elif event.type == pygame.QUIT: #If the user hits the red X
                    name_got = True #Disable loop
                    run = False #Disable main loop
            username.update(events) #Update events of the text box
            #Make changes to the screen
            pygame.draw.rect(loginScreen, BLACK, [250, 280, 300, 40])
            loginScreen.blit(username.get_surface(), (260, 285))
            pygame.display.update() #Update the display
            clock.tick(60) #Tick the clock 60 frames

    elif mode == 'welcome': #Welcome screen mode
        #Make changes to the logo by blitting up and down (bouncing effect)
        loginScreen.blit(loginImg, (0,0))
        if move == 10:
            dec = False
            loginScreen.blit(logo,(272,move))
        elif move == 20:
            dec = True
            loginScreen.blit(logo,(272,move))
        else:
            loginScreen.blit(logo,(272,move))
        if dec == True:
            move -=1 
        else:
            move +=1
        #Create buttons and draw them
        optionsBtn = Button(50, 420, 'OPTIONS', BLACK, 125, 50, loginScreen)
        optionsBtn.draw()
        helpBtn = Button(50, 495, 'HELP', BLACK, 125, 50, loginScreen)
        helpBtn.draw()
        playBtn = Button(212.5, 420, 'PLAY', BLACK, 375, 125, loginScreen)
        playBtn.draw()
        statsBtn = Button(625, 420, 'STATS', BLACK, 125, 50, loginScreen)
        statsBtn.draw()
        quitBtn = Button(625, 495, 'QUIT', BLACK, 125, 50, loginScreen)
        quitBtn.draw()
        #Event checker
        for event in pygame.event.get(): #If the user hits the red X
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #If the user left clicks on a button then change the mode
                if helpBtn.btn.collidepoint(event.pos):
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'help'
                elif playBtn.btn.collidepoint(event.pos):
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'play'
                elif statsBtn.btn.collidepoint(event.pos):
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'stats'
                elif optionsBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'options'
                elif quitBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'are_you_sure'

        pygame.display.update() #Update the display
        clock.tick(60) #Tick the clock 60 frames

    elif mode == 'are_you_sure': #Are you sure you want to quit screen mode
        #Make changes to the screen
        loginScreen.blit(bg, (0,0))
        loginScreen.blit(prismQuit ,(0,0))
        #Create buttons and draw them
        yesBtn = Button(200, 300, 'YES', D_GREEN, 150, 50, loginScreen)
        yesBtn.draw()  
        noBtn = Button(450, 300, 'NO', RED, 150, 50, loginScreen)
        noBtn.draw()
        #Update display
        pygame.display.update()
        clock.tick(60)
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #If the user left clicks on a button
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if yesBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    run = False
                elif noBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'welcome'
    

    elif mode == 'are_you_sure_reset_stats': #Are you sure you want to reset stats page 
        #Make changes to the screen
        loginScreen.blit(bg, (0,0))
        loginScreen.blit(resetImg ,(0,0))
        #Create and draw buttons
        yesBtn = Button(200, 300, 'YES', D_GREEN, 150, 50, loginScreen)
        yesBtn.draw()  
        noBtn = Button(450, 300, 'NO', RED, 150, 50, loginScreen)
        noBtn.draw()
        #Update the display
        pygame.display.update()
        clock.tick(60)
        #Event checker 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #If the user left clicks on a button
                if yesBtn.btn.collidepoint(event.pos):
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    reset_scores()
                    mode = 'stats'
                elif noBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'stats'

    elif mode == 'are_you_sure_reset_game': #Are you sure you want to reset the game page
        #Make changes to the display
        loginScreen.blit(bg, (0,0))
        loginScreen.blit(resetImg ,(0,0))
        #Create and draw buttons
        yesBtn = Button(200, 300, 'YES', D_GREEN, 150, 50, loginScreen)
        yesBtn.draw()  
        noBtn = Button(450, 300, 'NO', RED, 150, 50, loginScreen)
        noBtn.draw()
        #Update the display
        pygame.display.update()
        clock.tick(60)
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #If the user left clicks on a button
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if yesBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    
                    loginScreen.blit(bg, (0,0))
                    loginScreen.blit(restartImg, (0,0))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    run = reset_game()
                elif noBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'options'

    elif mode == 'help': #Help page (1)
        #Make changes to the screen, create and draw buttons, update the display
        loginScreen.blit(helpImg,(0,0))
        backBtn = Button(100, 500, 'BACK', BLACK, 125, 50, loginScreen)
        backBtn.draw()  
        faqBtn = Button(337.5, 500, 'FAQ', BLACK, 125, 50, loginScreen)
        faqBtn.draw()
        helpBtnRight = Button(575, 500, 'NEXT', BLACK, 125, 50, loginScreen)
        helpBtnRight.draw()
        pygame.display.update()
        clock.tick(60)
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #If the user left clicks on a button, change the modes
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if backBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'welcome'
                elif faqBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    open_site()
                if helpBtnRight.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'help2'
    
    elif mode == 'help2': #Help page 2
        #Make changes to the screen, create and draw buttons, update the display
        loginScreen.blit(helpImg2,(0,0))
        backBtn = Button(100, 500, 'BACK', BLACK, 125, 50, loginScreen)
        backBtn.draw()
        faqBtn = Button(337.5, 500, 'FAQ', BLACK, 125, 50, loginScreen)
        faqBtn.draw()
        helpBtnRight = Button(575, 500, 'NEXT', BLACK, 125, 50, loginScreen)
        helpBtnRight.draw()
        pygame.display.update()
        clock.tick(60)
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #If the user left clicks on a button, change the mode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if backBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'help'
                elif faqBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    open_site()
                elif helpBtnRight.btn.collidepoint(event.pos):
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'help3'

    elif mode == 'help3': #Help page 3
        #Make changes to the screen, create and draw buttons, update the displays
        loginScreen.blit(helpImg3,(0,0))
        backBtn = Button(100, 500, 'BACK', BLACK, 125, 50, loginScreen)
        backBtn.draw()
        faqBtn = Button(337.5, 500, 'FAQ', BLACK, 125, 50, loginScreen)
        faqBtn.draw()
        pygame.display.update()
        clock.tick(60)
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #If the user left clicks a button, change the mode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if backBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'help2'
                elif faqBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    open_site()

    elif mode == 'play': #Play mode
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False #Disable loop
        menuMusic.stop() #Stop mode
        fade_out(loginWidth, loginHeight, loginScreen) #Fade into the arcade 
        mode = arcade.cutscene(True) #Call the arcade cutscene function
        menuMusic.play(-1) #Replay the music infinitely
        vol = getMusic() #Get the volume
        menuMusic.set_volume(vol) #Set the volume
    
    elif mode == 'stats': #Stats page mode
        #Make changes to the screen, create and draw buttons
        loginScreen.blit(statsBG,(0,0))
        backBtn = Button(337.5, 520, 'BACK', BLACK, 150, 50, loginScreen)
        resetStatsBtn = Button(537.5, 520, 'RESET STATS', BLACK, 200, 50, loginScreen)
        cutscene1Btn = Button(537.5, 320, 'CUTSCENE 1', BLACK, 200, 50, loginScreen)
        cutscene1Btn.draw()
        #Check if cutscene 2 is enabled
        cut_enabled = get_key('key_MSTR')
        if cut_enabled[1] == 1: #If met create the button and draw it
            cutscene2Btn = Button(537.5, 420, 'CUTSCENE 2', BLACK, 200, 50, loginScreen)
            cutscene2Btn.draw()
        #Draw buttons
        resetStatsBtn.draw()
        backBtn.draw()
        name_txt = get_username_sql() #Get the name of the user
        name = font2.render(name_txt, True, WHITE, None) #Render the name of the user
        loginScreen.blit(name, (460,200)) #Blit the name to the screen
        #Check if the user has unlocked these games
        show_km = display_text('ShowKM')
        show_shdw = display_text('ShowSHDW')
        show_lp = display_text('ShowLP')
        show_sitd =  display_text('ShowSITD')
        text_qstn = font2.render('???', True, BLUE)
        if show_km == 1:
            loginScreen.blit(statsKM, (0,0))
        else:
            loginScreen.blit(text_qstn, (35,200))
        if show_shdw == 1:
            loginScreen.blit(statsSB, (0,0))
        else:
            loginScreen.blit(text_qstn, (35,300))
        if show_lp == 1:
            loginScreen.blit(statsLP, (0,0))
        else:
            loginScreen.blit(text_qstn, (35,400))
        if show_sitd == 1:
            loginScreen.blit(statsSITD, (0,0))
        else:
            loginScreen.blit(text_qstn, (35,500))
        #Get the scores of the games and blit them
        km_score = get_score('KeyMatcher')
        shd_box_score = get_score('ShadowBoxing')
        l_pong_score = get_score('LightPong')
        sitd_score = get_score('ShotInTheDark')
        km = font2.render(str(km_score), True, RED)
        shd = font2.render(str(shd_box_score), True, RED)
        l_pong = font2.render(str(l_pong_score), True, RED)
        sitd = font2.render(str(sitd_score), True, RED)
        loginScreen.blit(km, (35,235))
        loginScreen.blit(shd, (35,335))
        loginScreen.blit(l_pong, (35,435))
        loginScreen.blit(sitd, (35,535))
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False #Disable the main game loop
            #If the user left clicks on a button, change the mode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if backBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'welcome'
                
                elif resetStatsBtn.btn.collidepoint(event.pos):
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'are_you_sure_reset_stats'
                elif cutscene1Btn.btn.collidepoint(event.pos):
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    pygame.mixer.fadeout(2000)
                    arcade.cutscene(False)
                    menuMusic.set_volume(0.3)
                    menuMusic.play(-1)
                #If cutscene2 is enabled display the button to play it
                if cut_enabled[1] == 1:
                    if cutscene2Btn.btn.collidepoint(event.pos):
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        pygame.mixer.fadeout(2000)
                        arcade.ending(loginScreen)
                        menuMusic.set_volume(0.3)
                        menuMusic.play(-1)
        #Update the screen and tick the clock 60 frames
        pygame.display.update()
        clock.tick(60)
    
    elif mode == 'options': #Options mode page
        #Make changes to the screen, Create and draw buttons     
        loginScreen.blit(bg,(0,0))
        loginScreen.blit(prismOptions,(0,0))
        backBtn = Button(337.5, 500, 'BACK', BLACK, 150, 50, loginScreen)
        soundFXBtn.draw()
        backBtn.draw()
        musicBtn.draw()
        resetGame = Button(537.5, 500, 'RESET GAME', BLACK, 200, 50, loginScreen)
        resetGame.draw()
        #Event checker 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #If the user left clicks a button, change the mode or settings
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if backBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'welcome'
                elif musicBtn.btn.collidepoint(event.pos):
                    
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    musicPlay(musicBtn)
                    vol = getMusic()
                    menuMusic.set_volume(vol)

                elif soundFXBtn.btn.collidepoint(event.pos):
                    playSound(soundFXBtn)
                    soundFX = getSound()
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                
                elif resetGame.btn.collidepoint(event.pos):
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    mode = 'are_you_sure_reset_game'
        #Update the display, tick the clock 60 frames
        pygame.display.update()
        clock.tick(60)
        
pygame.quit() #Quit pygame

################################################################################
