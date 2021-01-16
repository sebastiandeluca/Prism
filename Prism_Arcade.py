import pygame
from pygame.locals import *
from Prism_Resources import Button, fade_in, fade_out
from Prism_Characters import *
import Prism_KeyMatch as keyMatch
import Prism_ShadowBoxing as SdwBox
import Prism_LightPong as LightPong
import Prism_SITD as SITD
import time
from Prism_sql import *
import random
pygame.init()

#COLOUR
 
CYAN = (8,163,255)
YELLOW =(208,232,7)
RED = (255,51,21)
BLUE = (12,67,235)
GREEN = (105,255,8)
BLACK = (0,0,0)
D_GREEN = (48, 110, 3)
 
#MUSIC / SOUNDS
arcadeMusic = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_ArcadeMusic.ogg')
    
btnSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/button.wav')
dylanSpeak = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_Speak.wav')
pickUpSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_Pickup.wav')
thunderSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_Thunder.ogg')
#TEXT
font = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf',55)
logo = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Logo2.png')
logo = pygame.transform.scale(logo, (210,210))
pauseScreenText = font.render('PAUSED', True, RED, None)

#IMAGE LOADING
arcade_map = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapBot.png')

topImg1 = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapTop.png')
topImg1 = pygame.transform.scale(topImg1,(2835,1875))

topImg2 = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapTop2.png')
topImg2 = pygame.transform.scale(topImg2,(2835,1875))

topImg3 = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapTop3.png')
topImg3 = pygame.transform.scale(topImg3,(2835,1875))

topImg4 = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapTop4.png')
topImg4 = pygame.transform.scale(topImg4,(2835,1875))

topImg5 = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapTop5.png')
topImg5 = pygame.transform.scale(topImg5,(2835,1875))

topImg6 = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapLit.png')
topImg6 = pygame.transform.scale(topImg6,(2835,1875))

topImg7 = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapLightning.png')
topImg7 = pygame.transform.scale(topImg7,(2835,1875))

topImg8 = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapLightning_NO.png')
topImg8 = pygame.transform.scale(topImg8,(2835,1875))

grass = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_BG.png')
grass = pygame.transform.scale(grass,(2835,1875))
arcade_mapTop = [topImg1,topImg2,topImg3,topImg4,topImg5,topImg6,topImg7,topImg8]
arcade_map = pygame.transform.scale(arcade_map,(2835,1875))
arcadeDoor = pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_DOOR.png')
arcadeDoor = pygame.transform.scale(arcadeDoor,(2835,1875))

helpImg = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_HelpBG.png')
helpImg2 = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_HelpBG2.png')
helpImg3 = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Main_Credit.jpg')
prismBG = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_BG.jpg')
prismOptions = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Options.png')

endMusic = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_Reunited.ogg')
endMusic.set_volume(0.2)

img_x = 100
img_y = 0
cutscenePlayed = False ###CHANGE TO FALSE
cut_scene_checker = get_setting('cutscene')
if cut_scene_checker == 0:
    cutscenePlayed = False ###CHANGE TO FALSE
elif cut_scene_checker == 1:
    cutscenePlayed = True 

#IMAGERY LISTS
cutsceneImgs = [pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_Eyes.jpg'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_BG.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_LookUpDyl.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_DylSCREAM.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_Mom.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_ANYONE.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_whatgoing.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_where.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene/Prism_CS_AH.png')]
programIcon = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Logo.png')
#MAP FILES
maps = [pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapBot.png'),pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapBot2.png'),pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapBot3.png'),pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapBot4.png'),pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapBot5.png'),pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapBot6.png'),pygame.image.load('Prism_assets/Prism_img/Prism_arcade/Prism_Arcade_MapBotFIX.jpg')]
arcade_maps = []
for img in maps: #Rescale Images
    img = pygame.transform.scale(img,(2835,1875))
    arcade_maps.append(img)
 
dylanText = [pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_callForMom.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_callForSomeone.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_confused.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_sigh.png')]
dylanOptions = [pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_needKey.png'), pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_turnedOff.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_FoundKey.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_LightsOn.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_LoseGame.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DONTneedKey.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_FoundFrontKey.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_TurnedOnTheLights.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_needFrontKey.png')]
 
            #RESCALE CHAR MODEL IMGS
dylanForward = [pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanIdle.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanWalkF1.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanWalkF2.png')]
dylanForwardImg = []
for img in dylanForward: #Rescale Images
    img = pygame.transform.scale(img,(64,64))
    dylanForwardImg.append(img)
 
dylanBack = [pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanIdleBack.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanWalkBack1.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanWalkBack2.png')]
dylanBackImg = []
for img in dylanBack:#Rescale Images
    img = pygame.transform.scale(img,(64,64))
    dylanBackImg.append(img)
 
dylanRSide = [pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanIdleSideR.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanWalkSideR1.png'),pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanWalkSideR2.png')]
dylanRSideImg = []
for img in dylanRSide:#Rescale Images
    img = pygame.transform.scale(img,(64,64))
    dylanRSideImg.append(img)
 
dylanLSideImg = []
 
for img in dylanRSideImg:#Rescale Images
    leftImg = pygame.transform.flip(img, True, False)
    dylanLSideImg.append(leftImg)

#IMAGERY OF DYLAN'S ****SPOILER*****

cutsceneImg = [pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene_2/Prism_CS2_1.jpg'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene_2/Prism_CS2_2.jpg'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene_2/Prism_CS2_2Text.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene_2/Prism_CS2_2Text2.png'),pygame.image.load('Prism_assets/Prism_img/Prism_Cutscene_2/Prism_CS2_ThankYou.jpg')]
walkCount = 0 # Set a constant for walkcount

def pickUpKey(img_x,img_y,dylanKeys): #Allow Dylan to pick up keys to further story if he is in the right area
    if dylanKeys == []: # Make sure dylan can only pick up the Keymatcher key
        if (-1200 <= img_x <= -1160) and (-845 <= img_y <= -730) and 'KM' not in dylanKeys:
            dylanKeys.append('KM') # Append KeyMatcher Key
    elif dylanKeys != []: # Make sure dylan can no longer repeat 'I don't need that key'
        if (-2200 <= img_x <= -2150) and (138 >= img_y >= 90) and 'SB' not in dylanKeys and dylanKeys[-1] == 'KM':
            dylanKeys.append('SB') # Append Shadowboxing Key
        elif (-1810 <= img_x <= -1780) and (-320 <= img_y <= -285) and 'LP' not in dylanKeys and dylanKeys[-1] == 'SB':
            dylanKeys.append('LP') # Append Light Pong key
        elif (-730 <= img_x <= -690) and (40<= img_y <= 110) and 'SITD' not in dylanKeys and dylanKeys[-1] == 'LP':
            dylanKeys.append('SITD') # Append Shot In The Dark key
        elif (-410 <= img_x <= -350) and (-652 <= img_y <= -610) and 'MSTR' not in dylanKeys and dylanKeys[-1] == 'SITD':
            dylanKeys.append('MSTR') # Append master key
        elif (-460 <= img_x <= -410) and (-652 <= img_y <= -610) and 'ON' not in dylanKeys and dylanKeys[-1] == 'MSTR':
            dylanKeys.append('ON') # Append that lights are on
         
    return dylanKeys # Return Dylan's keys to the main game
 
#Function to change music buttons
def musicPlay(musicBtn): # Allow the user to disable music in the pause menu
    playMusic = get_setting('Music')
    if playMusic == 0:
        change_setting('Music', 1)
        musicBtn.text = 'OFF'
        musicBtn.text_colour = RED
    elif playMusic == 1:
        change_setting('Music', 0)
        musicBtn.text = 'ON'
        musicBtn.text_colour = D_GREEN

#Function to change sound buttons
def playSound(soundFXBtn):  # Allow the user to disable sound in the pause menu
    soundFX = get_setting('Sounds')
    if soundFX == 0:
        change_setting('Sounds', 1)
        soundFXBtn.text = 'OFF'
        soundFXBtn.text_colour = RED
    elif soundFX == 1:
        change_setting('Sounds', 0)
        soundFXBtn.text = 'ON'
        soundFXBtn.text_colour = D_GREEN

#Function to get the sound from the database and return some value
def getSound(): # Retrieve whether the user has turned off sound or not
    sound = get_setting('Sounds')
    if sound == 0:
        return True
    elif sound == 1:
        return False

#Function to get the music from the database and return some value
def getMusic(): # Retrieve whether the user has turned off music or not
    music_vol = get_setting('Music')
    if music_vol == 0:
        return 0.3
    elif music_vol == 1:
        return 0

def cutscene(val): # The cutscene that starts the game
    
    global cutsceneImgs,cutscenePlayed, arcadeScreen, musicBtn, soundFXBtn
    #W/H OF SCREEN
    arcadeHeight = 600
    arcadeWidth = 800
    #CREATE SCREEN
    arcadeScreen = pygame.display.set_mode((arcadeWidth, arcadeHeight))
    pygame.display.set_caption('Prism')
    pygame.display.set_icon(programIcon)
    bg = pygame.transform.scale(cutsceneImgs[1],(4500,2000))
    #Create Buttons
    musicBtn = Button(215, 300, 'ON', D_GREEN, 150, 50, arcadeScreen)
    soundFXBtn = Button(435, 300, 'ON', D_GREEN, 150, 50, arcadeScreen)
    arcadeMusic.play(-1) # Play the background music infinitely
    soundText = getSound() #Call the get sound function
    
    if soundText == True: # Switch
        soundFXBtn.text = 'ON'
        soundFXBtn.text_colour = D_GREEN
    elif soundText == False: #WAS TRUE --------------------
        soundFXBtn.text = 'OFF'
        soundFXBtn.text_colour = RED
    musicPlayBack = getMusic()
    if musicPlayBack == 0.3:
        musicBtn.text = 'ON'
        musicBtn.text_colour = D_GREEN
    elif musicPlayBack == 0:
        musicBtn.text = 'OFF'
        musicBtn.text_colour = RED
    vol = getMusic()
    arcadeMusic.set_volume(vol)
    if val == False:
        cutscenePlayed = False
    if cutscenePlayed == False:
        ##################################################################
        #This entire block of code is the cutscene.
        arcadeScreen.fill((0,0,0))
        pygame.display.update()
        pygame.time.delay(1000)
        for event in pygame.event.get(): # Prevent Crashes
            if event.type == KEYDOWN:
                pass
        arcadeScreen.blit(cutsceneImgs[0],(0,0))
        pygame.display.update()
        pygame.time.delay(1000)
        for event in pygame.event.get(): # Prevent Crashes
            if event.type == KEYDOWN:
                pass
        arcadeScreen.blit(cutsceneImgs[4], (0,0))
        dylanSpeak.play()
        pygame.display.update()
        pygame.time.delay(1000)
        for event in pygame.event.get(): # Prevent Crashes
            if event.type == KEYDOWN:
                pass
        arcadeScreen.blit(cutsceneImgs[0],(0,0))
        arcadeScreen.blit(cutsceneImgs[5], (0,0))
        dylanSpeak.play()
        pygame.display.update()
        pygame.time.delay(1000)
        for event in pygame.event.get(): # Prevent Crashes
            if event.type == KEYDOWN:
                pass
        arcadeScreen.blit(bg,(-100,-300))
        arcadeScreen.blit(cutsceneImgs[2],(100,0))
        pygame.display.update()
        pygame.time.delay(500)
        for event in pygame.event.get(): # Prevent Crashes
            if event.type == KEYDOWN:
                pass
        arcadeScreen.blit(bg,(-100,-300))
        arcadeScreen.blit(cutsceneImgs[3],(100,0))
        arcadeScreen.blit(cutsceneImgs[8],(100,0))
        dylanSpeak.play()
        pygame.display.update()
        pygame.time.delay(500)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
        base = 0
        for i in range(0, 850): # Create a pan effect
            base += 1
            arcadeScreen.blit(bg,(-100 + (i * -2) * 2,-1*base + (-300)))
            arcadeScreen.blit(cutsceneImgs[3],(100+(i * -2) * 2,-1*base))
            arcadeScreen.blit(cutsceneImgs[8],(100+(i * -2) * 2,-1*base))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    pass
            pygame.display.update()
        dylanSpeak.play()
        arcadeScreen.blit(cutsceneImgs[7],(0,0))
        pygame.display.update() # Update the screen
        pygame.time.delay(2000)
        for event in pygame.event.get():
            pass
        change_setting('cutscene', 1) # Save whether the user has played the cutscene before so they don't have to rewatch it when re-entering
        cutscenePlay = get_setting('cutscene')
        if cutscenePlay == 0: #If you user hasn't watched the cutscene
            cutscenePlayed = False
        elif cutscenePlay == 1: # If the user has
            if val == True: # If the user is viewing the cutscene from in-game
                cutscenePlayed = True
                
            elif val == False: # If the user is viewing the cutscene from main.py's menu
                cutscenePlayed = False
                arcadeMusic.stop()
    else:
        pass
        
    get_vals = get_coords()
    get_x = get_vals[0]
    get_y = get_vals[1]
    if val == True:
        game = lobby(get_x,get_y,0,arcadeScreen) # Spawn Dylan at the last saved coordinates
    else:
        game = '0' # Prevent crashing
    return game
    

def ending(arcadeScreen): # The cutscene that ends the game
    global cutsceneImg,dylanSpeak,endMusic
    endMusic.play(-1) # Play music indefinitely
    
    #######PLAY THE CUTSCENE#######
    fade_in(800,600,arcadeScreen) # Fade In the Cutscene
    arcadeScreen.blit(cutsceneImg[0],(0,0))
    pygame.display.update()
    pygame.time.delay(3000)
    for event in pygame.event.get(): # Prevent crashing
        if event.type == KEYDOWN:
            pass
    arcadeScreen.blit(cutsceneImg[1],(0,0))
    pygame.display.update()
    pygame.time.delay(1000)
    for event in pygame.event.get():# Prevent crashing
        if event.type == KEYDOWN:
            pass
    dylanSpeak.play()
    arcadeScreen.blit(cutsceneImg[2],(0,0))
    pygame.display.update()
    pygame.time.delay(1000)
    for event in pygame.event.get():# Prevent crashing
        if event.type == KEYDOWN:
            pass
    dylanSpeak.play()
    arcadeScreen.blit(cutsceneImg[1],(0,0))
    arcadeScreen.blit(cutsceneImg[3],(0,0))
    pygame.display.update()
    pygame.time.delay(3000)
    for event in pygame.event.get():# Prevent crashing
        if event.type == KEYDOWN:
            pass
    pygame.mixer.fadeout(2000)
    pygame.time.delay(500)
    for event in pygame.event.get():# Prevent crashing
        if event.type == KEYDOWN:
            pass
    fade_out(800,600,arcadeScreen)
    
    fade_in(800,600,arcadeScreen)
    arcadeScreen.blit(cutsceneImg[4],(0,0))
    pygame.display.update()
    pygame.time.delay(3000)
    for event in pygame.event.get():# Prevent crashing
        if event.type == KEYDOWN:
            pass
    fade_out(800,600,arcadeScreen) # Fade out the screen

    lobby.runArcade = False # Return user to the main menu

def checkSave(key): # Check the database for if the user has keys / beaten games
    checkList = [] # Create an empty list
    
    check = get_key(key) # Check data in database for if user has a key and has beaten the subsequent game
    if check[0] == 0:
        checkList.append(False)
    elif check[0] == 1:
        checkList.append(True)
    if check[1] == 0:
        checkList.append(False)
    elif check[1] == 1:
        checkList.append(True)
    return checkList # Return the values

def lobby(img_x,img_y,walkCount,screen): # Build the arcade
    font = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf',55)#####REMOVE
    global dylanForwardImg,dylanRSideImg,dylanLSideImg, arcade_mapTop,dylanOptions, arcade_map,programIcon
    arcadeScreen = screen
    #DYLAN-SPECIFIC VARIABLES
    moving = False
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False
    x_loc = 368 # Dylan's X-Coordinate on Map
    y_loc = 268 # Dylan's Y-Coordinate on Map
    
    #BUTTONS
    musicBtn = Button(215, 300, 'ON', D_GREEN, 150, 50, arcadeScreen)
    soundFXBtn = Button(435, 300, 'ON', D_GREEN, 150, 50, arcadeScreen)
    
    #CHECK SOUND / MUSIC SETTINGS
    soundFX = getSound()
    if soundFX == True:
        soundFXBtn.text = 'ON'
        soundFXBtn.text_colour = D_GREEN
    elif soundFX == False:
        soundFXBtn.text = 'OFF'
        soundFXBtn.text_colour = RED
    musicPlayBack = getMusic()
    if musicPlayBack == 0.3:
        musicBtn.text = 'ON'
        musicBtn.text_colour = D_GREEN
    elif musicPlayBack == 0:
        musicBtn.text = 'OFF'
        musicBtn.text_colour = RED
    imgCounter2 = 0 # imgCounter for 2nd set of dylan speech

    dylanKeys = [] # Set the list for the keys Dylan has
    keyCount = 0 # Set KeyCount to 0
    
    #Utilize the SQL to allow the user to continue where they left off
    keyOne = checkSave('key_KM')
    pickedUpKM = keyOne[0]
    beatKM = keyOne[1]
    if pickedUpKM == True:
        dylanKeys.append('KM')
        keyCount +=1
    else:
        pass

    keyTwo = checkSave('key_SB')
    pickedUpSB = keyTwo[0]
    beatSB = keyTwo[1]
    
    if pickedUpSB == True:
        dylanKeys.append('SB')
        keyCount +=1
    else:
        pass

    keyThree = checkSave('key_LP')
    pickedUpLP = keyThree[0]
    beatLP = keyThree[1]
    
    if pickedUpLP == True:
        dylanKeys.append('LP')
        keyCount +=1
    else:
        pass

    keyFour = checkSave('key_SITD')
    pickedUpSITD = keyFour[0]
    beatSITD = keyFour[1]
    
    if pickedUpSITD == True:
        dylanKeys.append('SITD')
        keyCount +=1
    else:
        pass

    masterKey = checkSave('key_MSTR')
    pickedUpMasterKey = masterKey[0]
    turnedOnLights = masterKey[1]
    if pickedUpMasterKey == True:
        dylanKeys.append('MSTR')
        keyCount +=1
        if turnedOnLights == True:
            dylanKeys.append('ON')
            keyCount +=1
        else:
            pass
    else:
        pass
    
    # Set program icon and initialize what's left of requirements for game
    pygame.display.set_icon(programIcon)
    arcadeScreen.fill((255,255,255))
   
    #Clock
    clock = pygame.time.Clock()
    arcadeScreen.blit(arcade_map,(300,600))
    dylan = spawnBoy(arcadeScreen)
   
    #Game Variables
    lobby.mode = 'arcade'
    lobby.runArcade = True
    arcadeLockoutTimer = 0
    imgCounter = 0
    weatherCount = 0
    sCount = 2
    topMap = arcade_mapTop[0] # Set top layer of map to Beginning of game
    weather = False # Create BOOL for Weather playing or not
 
    #More Buttons
    backBtn = Button(300, 500, 'BACK', BLACK, 150, 50, arcadeScreen)
    backBtn2 = Button(300, 500, 'BACK', BLACK, 150, 50, arcadeScreen)    
    nextBtn = Button(500, 500, 'NEXT', BLACK, 150, 50, arcadeScreen)
    
    

    
    while lobby.runArcade: #Main Arcade Loop
        if arcadeLockoutTimer > 0: # Prevent user from entering a 'loop' of the arcade games
            arcadeLockoutTimer -= 1

        if pickedUpKM == False: # CHECK IF DYLAN HAS KEYS
            arcade_map = arcade_maps[0]
        elif pickedUpKM == True and pickedUpSB == False:
            arcade_map = arcade_maps[1]
        elif pickedUpSB == True and pickedUpLP == False:
            arcade_map = arcade_maps[2]

        elif pickedUpLP == True and pickedUpSITD == False:
            arcade_map = arcade_maps[3]
        
        elif pickedUpSITD == True and beatSITD == True and pickedUpMasterKey == False:
            arcade_map = arcade_maps[4]
        elif pickedUpSITD == True and pickedUpMasterKey == False:
            arcade_map = arcade_maps[6]

        elif pickedUpMasterKey == True and turnedOnLights == False or pickedUpMasterKey == True and turnedOnLights == True :
            arcade_map = arcade_maps[5]
        elif turnedOnLights == True:
            topMap = arcade_mapTop[5]
        
        #Blit the map and Dylan
        arcadeScreen.blit(grass, (img_x+300,img_y - 300))
        arcadeScreen.blit(arcade_map,(img_x,img_y))
        arcadeScreen.blit(dylan.image, (x_loc,y_loc))
        
        #Generate a random weather variable and then play weather if conditions are met
        weatherVar = random.randint(0,10000)
        if weatherVar == 100:
            weather = True  
        if weather == True and  0 <= weatherCount <= 100: # Weather conditions are met
            if weatherCount == 1:
                soundFX = getSound()
                if soundFX == True:
                    thunderSound.play()
            else:
                pass
            if beatSITD == False:
                topMap = arcade_mapTop[7]
            else:
                topMap = arcade_mapTop[6]
            weatherCount += 1

        else: # Weather conditions are not met-- keep map in current state.
            weather = False
            weatherCount = 0
            if 'ON' in dylanKeys:
                topMap = arcade_mapTop[5]
            elif beatSITD == True:
                topMap = arcade_mapTop[4]
            elif beatLP == True:
                topMap = arcade_mapTop[3]
            elif beatSB == True:
                topMap = arcade_mapTop[2]
            elif beatKM == True:
                topMap = arcade_mapTop[1]
            else:
                topMap = arcade_mapTop[0]

        #Blit the darkness, lightbulbs, and the illuminated front door
        arcadeScreen.blit(topMap, (img_x,img_y))
        arcadeScreen.blit(arcadeDoor,(img_x,img_y))

        if lobby.mode == 'arcade': # If the player is playing arcade mode
            if imgCounter > 0: # THINKING TEXT
                arcadeScreen.blit(speak,(x_loc+50,y_loc))
                imgCounter -= 1
           
            if imgCounter2 > 0: # SPEAKING TEXT
                arcadeScreen.blit(speak2,(0,0))
                imgCounter2 -= 1
           
            if moving == True: # PROCESS WALK ANIM.
                if walkCount > 30:
                        walkCount = 0
                else:
                    walkCount += 1
            else:
                walkCount = 0
                pygame.display.update()
 
            for event in pygame.event.get(): # Check user events
                if event.type == pygame.QUIT: #Check if the user hits the red X
                    lobby.mode = 'quit' #Set lobby mode to quit
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #If left mouse click
                    soundFX = getSound() #Call getSound function
                    if soundFX == True: #If true play dylan's sound
                        dylanSpeak.play()
                    imgCounter = 120 # Start loop for Dylan's speaking
                    pic = random.randint(0,3) #Randomly choose one of dylan's possible voice lines
                    speak = dylanText[pic] 
                   
                if event.type == pygame.KEYDOWN: #User Presses a Button
                    if event.key == K_ESCAPE: # Activate pause mode upon user pressing escape
                        lobby.mode = 'pause'
                        moveUp = False
                        moveDown = False
                        moveLeft = False
                        moveRight = False
                    else: # User hasn't pressed ESCAPE
                        moving = True

                           
                    if event.key == K_w or event.key == K_UP: # If user is moving upward
                        moveUp = True
                       
                        moveDown = False
                    if event.key == K_s or event.key == K_DOWN: # If user is moving downward
                        moveDown = True
         
                        moveUp = False
                    if event.key == K_d or event.key == K_RIGHT: # If user if moving right
                        moveRight = True
                     
                        moveLeft = False
                    if event.key == K_a or event.key == K_LEFT: # If user is moving left
                        moveLeft = True
             
                        moveRight = False
                    
                       
               
                if event.type == pygame.KEYUP: # User releases a button
                   
                    if event.key == K_w or event.key == K_UP: # User is no longer moving up
                        moveUp = False
                       
                    if event.key == K_s or event.key == K_DOWN: # User is no longer moving down
                        moveDown= False
                        dylan.image = dylanForwardImg[0]
                    if event.key == K_a or event.key == K_LEFT:# User is no longer moving left
                        moveLeft = False
                        dylan.image = dylanLSideImg[0]
                    if event.key == K_d or event.key == K_RIGHT:# User is no longer moving right
                        moveRight = False
                        dylan.image = dylanRSideImg[0]
                    if event.key == K_SPACE: # If the user attempts to interact with anything in the map
                        
                        ###IF CONDITIONS ARE MET-- ALLOW DYLAN TO PICK UP KEYS
                        if len(dylanKeys) == 0: # Allow user to pick up KeyMatcher key
                            dylanKeys = pickUpKey(img_x,img_y,dylanKeys)
                           
                        elif len(dylanKeys) == 1 and beatKM == True:# Allow user to pick up ShadowBoxing key
                            dylanKeys = pickUpKey(img_x,img_y,dylanKeys)

                        elif len(dylanKeys) == 2 and beatSB == True:# Allow user to pick up LightPong key
                            dylanKeys = pickUpKey(img_x,img_y,dylanKeys)

                        elif len(dylanKeys) == 3 and beatLP == True:# Allow user to pick up Shot in The Dark key
                            dylanKeys = pickUpKey(img_x,img_y,dylanKeys)

                        
                        elif len(dylanKeys) == 4 and beatSITD == True: # Allow user to pick up Master key
                            
                            dylanKeys = pickUpKey(img_x,img_y,dylanKeys)
                        elif len(dylanKeys) == 5 and 'MSTR' in dylanKeys: # Allow user to pick up Master key
                            
                            dylanKeys = pickUpKey(img_x,img_y,dylanKeys)

                        else:
                            pass
                           
                        try: # Exception handling to prevent index errors
                            
                            # Check if Dylan has collected the key-- if he does, save it and play a sound.
                            needKey = dylanKeys[-1]
                            if needKey == 'KM' and keyCount == 0: 
                                keyCount +=1
                                save_key('key_KM', 1, 0)
                                pickedUpKM = True
                                pickUpSound.play()
                                speak2 = dylanOptions[2]
                                imgCounter2 = 120  
                            elif needKey == 'SB'and keyCount == 1 and beatKM == True:
                                keyCount +=1
                                save_key('key_SB', 1, 0)
                                pickedUpSB = True
                                pickUpSound.play()
                                speak2 = dylanOptions[2]
                                imgCounter2 = 120  
                            elif needKey == 'LP'and keyCount == 2 and beatSB == True:
                                keyCount +=1
                                save_key('key_LP', 1, 0)
                                pickedUpLP = True
                                pickUpSound.play()
                                speak2 = dylanOptions[2]
                                imgCounter2 = 120  
                            elif needKey == 'SITD'and keyCount == 3 and beatLP == True:
                                keyCount +=1
                                save_key('key_SITD', 1, 0)
                                pickedUpSITD = True
                                pickUpSound.play()
                                speak2 = dylanOptions[2]
                                imgCounter2 = 120
                            elif needKey == 'MSTR'and keyCount == 4 and beatSITD == True:
                                keyCount +=1
                                save_key('key_MSTR', 1, 0)
                                pickedUpMasterKey = True
                                pickUpSound.play()
                                speak2 = dylanOptions[6]
                                imgCounter2 = 120
                            elif needKey == 'ON' and keyCount == 5 and pickedUpMasterKey == True:
                                keyCount += 1
                                save_key('key_MSTR', 1, 1)
                                #turnedOnLights = True
                                topMap = arcade_mapTop[5]
                                pickUpSound.play()
                                speak2 = dylanOptions[7]
                                imgCounter2 = 120
                            else:
                                if (-2200 <= img_x <= -2150) and (135 >= img_y >= 90) and beatKM == False:
                                    speak2 = dylanOptions[5]
                                    imgCounter2 = 120  
                                elif (-1810 <= img_x <= -1780) and (-320 <= img_y <= -285) and beatSB == False:
                                    speak2 = dylanOptions[5]
                                    imgCounter2 = 120  
                                elif (-730 <= img_x <= -690) and (40<= img_y <= 110) and beatLP == False:
                                    speak2 = dylanOptions[5]
                                    imgCounter2 = 120
                        except IndexError:
                            pass
 
                        if (img_x <= -1680 and img_x >= -1720) and (img_y <= -610 and img_y >= -640): #If Dylan is at keymatch
                            machine = 'KM' # Dylan is at the keymatcher Machine
                            hasKey = keyCheck(machine,dylanKeys)
                            if hasKey == True and arcadeLockoutTimer == 0: # If Dylan has the key and is not locked out of the machine
                                pickedUpKM = True # Acknowledge that Dylan has the key
                                arcadeMusic.stop() # Stop the arcade music
                                win = keyMatch.run() # Run keymatcher and retrieve whether Dylan has won or not
                                arcadeMusic.play(-1) # Play the music indefinitely
                                vol = getMusic() # Check if the user has music enabled
                                arcadeMusic.set_volume(vol)
                                
                                if win == True: # If the user won the game
                                    save_key('key_KM', 1, 1) # Save that Dylan has the key in the database
                                    beatKM = True # Save that Dylan has beaten the game
                                    speak2 = dylanOptions[3] # Dylan speak
                                    imgCounter2 = 120  # Activate speech loop
                                    topMap = arcade_mapTop[1] # Change lighting of map
                                    arcadeScreen.blit(topMap, (img_x,img_y)) #Blit new map
                                    pygame.display.update()
                                else:
                                    if beatKM == True: # If Dylan has already beaten the game, pass
                                        pass
                                    else: # If Dylan has lost, hint the user that a higher score will give a result
                                        speak2 = dylanOptions[4]
                                        imgCounter2 = 120

                                arcadeLockoutTimer = 30 # Begin lockout timer
                                
                            elif arcadeLockoutTimer != 0: # Continue lockout timer
                                pass
                            
                            else: # if the user doesnt have the key
                                imgCounter2 = 120
                                speak2 = dylanOptions[0]

                        elif (img_x <= -1870 and img_x >= -1900) and (img_y <=-610 and img_y >= -640): #If Dylan is at shadowboxing
                            machine = 'SB' # Dylan is at the ShadowBoxing Machine
                            hasKey = keyCheck(machine,dylanKeys) # Check if dylan has the key
                            if hasKey == True and arcadeLockoutTimer == 0: # If Dylan has the key and is not locked out of the machine
                                pickedUpSB = True # Dylan has the key
                                arcadeMusic.stop() # Stop the music
                                win = SdwBox.runGame(True) # Start game
                                arcadeMusic.play(-1) # Play music indefinitely
                                vol = getMusic() # Check if user has the music enabled
                                arcadeMusic.set_volume(vol)
                                if win == True: # If Dylan wins, save the key and say that more lights have turned on
                                    save_key('key_SB', 1, 1)
                                    beatSB = True
                                    speak2 = dylanOptions[3]
                                    imgCounter2 = 120  
                                    topMap = arcade_mapTop[2] # Update Map
                                    arcadeScreen.blit(topMap, (img_x,img_y)) # Update Map
                                    pygame.display.update()
                                else:
                                    if beatSB == True: # If Dylan has already beaten ShadowBoxing
                                        pass
                                    else: # If Dylan has lost, hint the user that a higher score will give results
                                        speak2 = dylanOptions[4] 
                                        imgCounter2 = 120  

                                arcadeLockoutTimer = 30 # Start lockout
                            elif arcadeLockoutTimer != 0: # Continue lockout
                                pass
                            else: # If the user doesn't have the key
                                imgCounter2 = 120
                                speak2 = dylanOptions[0]
                        
                        elif (img_x <= -1870 and img_x >= -1900) and (img_y <=-800 and img_y >= -840): #If Dylan is at LightPong
                            machine = 'LP' # Dylan is at the LightPong Machine
                            hasKey = keyCheck(machine,dylanKeys) # Check if Dylan has the key
                            if hasKey == True and arcadeLockoutTimer == 0:
                                pickedUpLP = True # Dylan has the key
                                arcadeMusic.stop() # Stop music
                                win = LightPong.startScreen() # Start Game
                                arcadeMusic.play(-1) # Play music indefinitely
                                vol = getMusic() # Check if user has music enabled
                                arcadeMusic.set_volume(vol)
                                if win == True: # If Dylan wins LightPong
                                    save_key('key_LP', 1, 1) # Save Kry
                                    beatLP = True # Save win
                                    speak2 = dylanOptions[3] # Dylan voice line
                                    imgCounter2 = 120  
                                    topMap = arcade_mapTop[3]
                                    arcadeScreen.blit(topMap, (img_x,img_y)) # Update map
                                    pygame.display.update()
                                else:
                                    if beatLP == True: # If Dylan has already won before
                                        pass
                                    else:
                                        speak2 = dylanOptions[4] # Dylan has lost-- hint user that higher score will give results
                                        imgCounter2 = 120  

                                arcadeLockoutTimer = 30 # Activate lockout
                            
                            elif arcadeLockoutTimer != 0: # Continue lockout
                                pass
                            
                            else: # Dylan doesn't have the key
                                imgCounter2 = 120
                                speak2 = dylanOptions[0]
                        
                        elif (img_x <= -1680 and img_x >= -1720) and (img_y <=-800 and img_y >= -840): #If Dylan is at SITD
                            machine = 'SITD' # Dylan is at the SITD Machine
                            hasKey = keyCheck(machine,dylanKeys) # Check if Dylan has the key
                            if hasKey == True and arcadeLockoutTimer == 0: # If Dylan has the key and is not locked out of the machine
                                pickedUpSITD = True #
                                arcadeMusic.stop() #Stop music
                                win = SITD.run(True) # Run Shot In The Dark
                                arcadeMusic.play(-1) # Play music indefinitely
                                vol = getMusic() # Check if the user has music enabled
                                arcadeMusic.set_volume(vol)
                                if win == True: # If Dylan wins
                                    save_key('key_SITD', 1, 1) # Save the win
                                    beatSITD = True
                                    speak2 = dylanOptions[3] # Dylan speaks
                                    imgCounter2 = 120  
                                    topMap = arcade_mapTop[4]
                                    arcadeScreen.blit(topMap, (img_x,img_y)) # Update the map
                                    pygame.display.update()
                                else: # If Dylan already won
                                    if beatSITD == True:
                                        pass
                                    else: # Dylan lost-- hint that higher score will give results
                                        speak2 = dylanOptions[4]
                                        imgCounter2 = 120   
                                
                                arcadeLockoutTimer = 30 # begin lockout
                            elif arcadeLockoutTimer != 0: # Continue Lockout
                                pass  
                            else: # Dylan does not have the key
                                imgCounter2 = 120
                                speak2 = dylanOptions[0]
                        
                        elif (-960 < img_x < -890) and (-930 <= img_y <= -900): #Dylan is at the front door
                            machine = 'ON'
                            hasKey = keyCheck(machine,dylanKeys) # Check if Dylan has turned on the lights
                            if hasKey == True:
                                arcadeMusic.fadeout(1000) # Begin the cutscene if dylan has turned on the lights and then end the game
                                fade_out(800,600,arcadeScreen)
                                ending(arcadeScreen)
                            
                            else: # If Dylan hasn't turned the lights on
                                speak2 = dylanOptions[1]
                                imgCounter2 = 120  
            ####### DYLAN CHAR WALK ANIMATION DEPENDENT ON STEPS
            if moveUp: #Collision Detection for move up.
                ##COLLISION DET.
                if img_y >= 135:
                    pass
 
                ##SPAWNROOM
                elif (img_x <= -535 and img_x >= -609) and (img_y >= -290 and img_y <= -291):
                    pass
                elif (img_x <= -280 and img_x >= -609) and (img_y == -290):
                    pass
                elif (img_x <= -540 and img_x >= -653) and (img_y <= -325 and img_y >= -431):
                    pass
                elif (img_x <= -535 and img_x >= -608) and (img_y == -704):
                    pass
                
                #Collision for concession stand
                elif (img_x >= -1306 and img_x <= -1014) and (-800 <= img_y <= -797): 
                    pass
                #EATING AREA -- TOP TABLES
                elif ((-1073 <= img_x <= -771) or (-1453 <= img_x <= -1151)) and ((-51 <= img_y <= 99) or (-241 <= img_y <= -91)):
                    pass

                #ARCADE AREA WALL
                elif (-2230 <= img_x <= -1618) and (img_y == -570):
                   pass
                
                #ARCADE MACHINES
                elif (-2023 <= img_x <= -1666) and (img_y == -620):
                    pass

                #PINBALL MACHINE
                elif (-2213 <= img_x <= -2137) and (img_y == -620):
                    pass
                #HOCKEY TABLEs
                elif (-2230 <= img_x <= -2139) and (-820 <= img_y <= -682):
                    pass

                #BOTTOM ARCADE MACHINES
                elif (-2023 <= img_x <= -1667) and (-800 <= img_y <= -692):
                    pass
                
                ####KITCHEN AREA
                    #DOOR
                elif (-1690 < img_x < -1573) and (-100 < img_y < 0):
                    pass
                    #ISLAND
                elif (-1965< img_x< -1650) and (-285 < img_y <-112):
                    pass
                    #CRATE
                elif ( -1922< img_x<-1690) and (-114 < img_y <-92):
                    pass
                    #KITCHEN ENTRYWAY
                elif (-1690 <= img_x <= -1620) and ( img_y >= 45):
                    pass
                    #CUPBOARD LEFT
                elif (-1760 <= img_x <= -1692) and (img_y >= 90):
                    pass
                elif (-2072 <= img_x <= -1760) and (img_y == 40):
                    pass
                    #FRIDGE
                elif (-2165 <= img_x <= -2072) and (img_y == 90):
                    pass
                #TOP WALL STORAGE ROOM
                elif (-2118 < img_x < -1912)and(-284 <= img_y <-139):
                    pass
                #KITCHEN LOCKERS
                elif (-2235 <= img_x <= -2205) and (-95 <= img_y <= 97):
                    pass
                ###STORAGE ROOM
                    #CRATE 1
                elif ( -1878 <= img_x <=-1812) and (-330 <= img_y <= -110):
                    pass
                    #CRATE 2 AND 3
                elif (-1788 < img_x <=-1619) and (-330 <= img_y <= -110):
                    pass
                    ##ENCLOSING WALLS
                #STORAGE ROOM ENTRY WAY
                elif (-2235 < img_x < -2186) and (-330 <= img_y <-100):
                    pass
                ####OFFICE
                elif (img_x <= -270 and img_x >= -535) and (-610<= img_y <= -468):
                    pass
                #office table
                elif (-417 <= img_x <=-341)and(-840 <= img_y <= -654):
                    pass
                ####COLLISIONS FOR OPEN DOORS ONCE SITD IS BEATEN
                elif ((img_x <= -540 and img_x > -654) and ((img_y == -704) or (img_y == -844))) and beatSITD == True:
                    pass
                else: # If Dylan is not colliding with any of the above statements, allow him to move.
                    if walkCount >= 0 and walkCount <= 10:
 
                        dylan.image = dylanBackImg[0]
                    elif walkCount > 10 and walkCount <= 20:
 
                        dylan.image = dylanBackImg[1]
                    elif walkCount > 20 and walkCount <= 30:

                        dylan.image = dylanBackImg[2]
                    img_y += 2
                    
            if moveDown: #Collision detection for move down.
                if img_y <= -930: #Down-most wall
                    pass
                ##SPAWNROOM
                elif (img_x <= -270 and img_x >= -533) and (-610< img_y <= -465):
                    pass
                elif (img_x <= -535 and img_x > -654) and (img_y <= -324 and img_y >= -400):
                    pass
                elif (img_x <= -535 and img_x >= -608) and (img_y == -746):
                    pass
                #Collision for concession stand
                elif (img_x >= -1305 and img_x <= -1014) and (img_y == -750): 
                    pass
                #EATING AREA -- TOP TABLES
                elif ((-1073 <= img_x <= -771) or (-1453 <= img_x <= -1151)) and ((-49 <= img_y <= 101) or (-238 <= img_y <= -90)):
                    pass
                # ARCADE AREA WALL
                elif (-2230 <= img_x <= -1618) and (img_y == -569):
                    pass

                #ARCADE MACHINES
                elif (-2023 <= img_x <= -1666) and (img_y == -619):
                    pass

                #PINBALL MACHINE
                elif (-2213 <= img_x <= -2137) and (-619 <= img_y <= -569):
                    pass
                
                #HOCKEY TABLE
                elif (-2231 <= img_x <= -2139) and (-819 <= img_y <= -680):
                    pass

                #BOTTOM ARCADE MACHINES
                elif (-2023 <= img_x <= -1667) and (-798 <= img_y <= -690):
                    pass
                ####KITCHEN AREA
                    #DOOR
                elif (-1690 < img_x < -1573) and (-98 < img_y < 4):
                    pass
                #ISLAND DOWN TO NEXT ROOM WALL
                elif ((-1972< img_x< -1690 ) or (-2066 <= img_x < -2000)) and (-284 < img_y <-110):
                    pass
                elif ( -1922< img_x<-1660) and (-109 < img_y <-90):
                    pass
                    #KITCHEN ENTRYWAY
                elif (-1690 <= img_x <= -1620) and ( img_y == 47):
                    pass
                    #CUPBOARD LEFT
                elif (-1760 <= img_x <= -1692) and (img_y == 92):
                    pass
                    #STOVECOUNTER
                elif (-2072 <= img_x <= -1758) and (img_y == 136):
                    pass
                #BACK WALL OF KITCHEN
                elif ((-2118 < img_x <= -1690) or (-2240 < img_x < -2186)) and (-252 < img_y < -136):
                    pass
                 #KITCHEN LOCKERS
                elif (-2235 <= img_x <= -2205) and (-94 <= img_y <= 98):
                    pass
                ###STORAGE ROOM
                    #CRATE 1
                elif (-1878 <= img_x <= -1812) and (-328 <= img_y <= -110):
                    pass
                elif (-2235 <= img_x <= -1654) and (-445 <= img_y <= -418):
                    pass
                elif (-2235 < img_x < -2186) and (-400 <= img_y <=-392):
                    pass
                #LAST CRATE
                elif (-1834 < img_x < -1764) and (-420 <= img_y <= -392):
                    pass
                #office table
                elif (-417 <= img_x <=-341)and(-838 <= img_y <= -652):
                    pass
                ####DOORS FOR WHEN SITD IS BEATEN
                elif ((img_x <= -540 and img_x > -654) and ((img_y == -606) or (img_y == -746))) and beatSITD == True:
                    pass
                else: #If none of the above statements are met, allow Dylan to move.
                    if walkCount >= 0 and walkCount <= 10:
                        dylan.image = dylanForwardImg[0]
                    elif walkCount > 10 and walkCount <= 20:
                        dylan.image = dylanForwardImg[1]
                    elif walkCount > 20 and walkCount <= 30:
                        dylan.image = dylanForwardImg[2]
                    img_y -= 2
 
            if moveLeft: #Collision detection for move left.
                if img_x >= -280: #Leftmost wall
                    pass
                ##SPAWNROOM
                elif (img_x <= -540 and img_x >= -610) and (img_y <= 136 and img_y >= -275):
                    pass
                elif (img_x <= -535 and img_x >= -610) and (-930 <= img_y <= -748):
                    pass
                elif (img_x <= -535 and img_x >= -610) and (-703 <= img_y <= -325):
                    pass
                elif (img_x <= -540 and img_x >= -655) and (img_y <= -325 and img_y >= -429):
                    pass
                
                #Collision for concession stand
                elif (img_x == -1306) and (img_y <= -754 and img_y >= -795): 
                    pass
                #EATING AREA -- TOP TABLES
                elif ((-1074 <= img_x <= -771) or (-1455 <= img_x <= -1151)) and ((-48 <= img_y <= 99) or (-238 <= img_y <= -91)):
                    pass

                #ARCADE MACHINES
                elif (-2025 <= img_x <= -1667) and (-619 <= img_y <= -569):
                    pass
                #PINBALL MACHINE
                elif (-2214 <= img_x <= -2137) and (-619 <= img_y <= -569):
                    pass
                
                #BOTTOM ARCADE MACHINES 
                elif (-2025 <= img_x <= -1667) and ( -798 <= img_y <= -692):
                    pass
                ####KITCHEN AREA
                    #DOOR
                elif (-1692 < img_x < -1630) and (-94 < img_y < 0):
                    pass
                #ISLAND
                elif (-1924 < img_x < -1690) and (-115 < img_y < -92):
                    pass

                elif (-1925<= img_x<= -1690) and (-284 < img_y <=-112):
                    pass

                #BOX
                elif ((-1976 <= img_x <= -1974) or (-2070 <= img_x <= -2068 )) and (-138 <= img_y <= -112):
                    pass
                    #CUPBOARD LEFT
                elif (img_x == -1692) and (46 <= img_y <= 90):
                    pass
                    #STOVECOUNTER
                elif (-2072 <= img_x <= -1760) and (42 <= img_y <= 136):
                    pass
                    #FRIDGE
                elif (-2165 <= img_x <= -2072) and (92 <= img_y <= 136):
                    pass
                #STORAGE ROOM ENTRY WAY
                elif (-2120 < img_x < -2000) and (-282 <= img_y <-138):
                    pass
                 #KITCHEN LOCKERS
                elif (-2235 <= img_x <= -2205) and (-94 < img_y < 97):
                    pass
                ###STORAGE ROOM
                    #CRATE 1
                elif (-1880 <= img_x <= -1812) and (-328 <= img_y <= -110):
                    pass
                #CRATE 2 AND 3
                elif (-1788 <= img_x <=-1620) and (-328 <= img_y <= -110):
                    pass
                      ###inner wall
                elif (-1694 <= img_x <= -1660) and (-430 <= img_y <= -328):
                    pass
                elif (-1834 <= img_x <= -1800) and (-420 <= img_y <= -394):
                    pass
                    #OFFICE TABLE
                elif (-418 <= img_x < -340) and (-838 <= img_y <= -654):
                    pass
                ######IF USER HAS UNLOCKED THE GAME, ALLOW THEM TO PASS THROUGH THE DOOR
                elif ((img_x == -610 and (-748 <= img_y <= -702))) and beatSITD == False:
                    pass
                elif ((img_x <= -540 and img_x >= -655) and ((-702 <= img_y <= -608) or (-748 >= img_y >= -842))) and beatSITD == True:
                    pass
                else: #If none of the above statements are met allow Dylan to move.
                    if walkCount >= 0 and walkCount <= 10:
 
                        dylan.image = dylanLSideImg[0]
                    elif walkCount > 10 and walkCount <= 20:
 
                        dylan.image = dylanLSideImg[1]
                    elif walkCount > 20 and walkCount <= 30:
 
                        dylan.image = dylanLSideImg[2]
                    
                    img_x += 2

            if moveRight: #Collision detection for move right.
                if img_x <= -2230: #Right-most wall
                    pass
                elif (img_x <= -530 and img_x >= -608) and (img_y <= 136 and img_y >= -275):
                    pass
                elif (img_x <= -532 and img_x > -610) and (-703 <= img_y <= -325):
                    pass
                elif (img_x <= -540 and img_x > -654) and (img_y <= -325 and img_y >= -429):
                    pass
                
                #Collision for concession stand
                elif (img_x == -1014) and (img_y <= -752 and img_y >= -792): 
                    pass
                #KITCHEN
                elif (img_x == -1618) and (img_y <= 136 and img_y >= 50):
                   pass
                #EATING AREA -- TOP TABLES
                elif ((-1073 <= img_x <= -770) or (-1453 <= img_x <= -1150)) and ((-48 <= img_y <= 99) or (-238 <= img_y <= -91)):
                    pass
                #ARCADE MACHINES
                elif (-2023 <= img_x <= -1665) and (-619 <= img_y <= -569):
                    pass
                #PINBALL
                elif (-2213 <= img_x <= -2135) and (-618 <= img_y <= -569):
                    pass

                #HOCKEY TABLE
                elif (-2230 <= img_x <= -2137) and (-819 <= img_y <= -682):
                    pass
                #BOTTOM ARCADE MACHINES 
                elif (-2023 <= img_x <= -1665) and (-798 <= img_y <= -692):
                    pass
                ####KITCHEN AREA
                    #WALLS
                elif ( -1630 < img_x <-1570) and (-98 < img_y < 0):
                    pass
                elif (-1760 < img_x < -1688) and (91 < img_y < 0):
                    pass
                elif ( -1922< img_x<-1690) and (-109 < img_y <-92):
                    pass
                    #CUPBOARD LEFT
                elif (-1760 == img_x) and (42 <= img_y <= 90):
                    pass
                    #STOVECOUNTER
                elif (-2072 <= img_x <= -1760) and (img_y == 42):
                    pass
                #BOX2
                elif (-2065 <= img_x <= -2000 ) and (-138 <= img_y < -112):
                    pass
                #BACK WALL OF KITCHEN
                elif(-2230 < img_x < -2184) and (-328 <= img_y < -138):
                    pass
                #STORAGE ROOM ENTRY WAY
                elif (-2117 < img_x < -2000) and (-282 <= img_y <-138):
                    pass
                #KITCHEN LOCKERS
                elif (-2235 <= img_x <= -2202) and (-94 < img_y < 97):
                    pass
                ###STORAGE ROOM
                    #CRATE 1
                elif (-1878 <= img_x <= -1810) and (-328 <= img_y <= -110):
                    pass
                    #LONGWALL
                elif (-1690 <= img_x <= -1618) and (-570 <= img_y <=-98):
                    pass
                elif(-2235 <= img_x <= -2186) and (-420 <= img_y <= -394):
                    pass
                #LAST CRATE
                elif (-1800 <= img_x <= -1760) and (-420 <= img_y <= -394):
                    pass
                    #OFFICE TABLE
                elif (-416 <= img_x <= -338) and (-838 <= img_y <= -654):
                    pass
                #OFFICE BOTTOM WALL
                elif (-570 <= img_x <= -532) and (-746 > img_y >= -930):
                    pass
                else: #If none of the above values are met allow Dylan to move
                    if walkCount >= 0 and walkCount <= 10:
                        dylan.image = dylanRSideImg[0]
                    elif walkCount > 10 and walkCount <= 20:
                        dylan.image = dylanRSideImg[1]
                    elif walkCount > 20 and walkCount <= 30:
                        dylan.image = dylanRSideImg[2]
                    pygame.display.update()
                    img_x -= 2
       
            pygame.display.update() # Update the display
            clock.tick(60) # Tick the clock 60 frames
 
        elif lobby.mode == 'pause': #Pause screen
            lobby.mode = pauseMenu(arcadeScreen) #Call pauseMenu function
 
        elif lobby.mode == 'quit': #Quit mode
            arcadeMusic.stop() #Stop music
            save_coords(img_x, img_y) #Save coordinates
            lobby.runArcade = False #Disable loop
 
        elif lobby.mode == 'options': #Options page
           #Make changes to the screen
            arcadeScreen.blit(prismBG,(0,0))
            arcadeScreen.blit(prismOptions,(0,0))
            soundFXBtn.draw()
            backBtn.draw()
            musicBtn.draw()
            pygame.display.update()
            #Event checker
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    lobby.mode = 'quit'
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        lobby.mode = 'arcade'
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if backBtn.btn.collidepoint(event.pos):
                        soundFX = getSound()
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        lobby.mode = 'pause'
                    elif musicBtn.btn.collidepoint(event.pos):
                        soundFX = getSound()
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        musicPlay(musicBtn)
                        vol = getMusic()
                        arcadeMusic.set_volume(vol)

                    elif soundFXBtn.btn.collidepoint(event.pos):
                        playSound(soundFXBtn)
                        soundFX = getSound()
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
            pygame.display.update() #Update the display
            
        elif lobby.mode == 'help': #Help screen 1
            #Make changes to the screen
            arcadeScreen.blit(helpImg, (0,0))
            backBtn.draw()
            nextBtn.draw()
            #Event checker
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    lobby.mode = 'quit'
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        lobby.mode = 'arcade'
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if backBtn.btn.collidepoint(event.pos):
                        soundFX = getSound()
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        lobby.mode = 'pause'
                    elif nextBtn.btn.collidepoint(event.pos):
                        soundFX = getSound()
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        lobby.mode = 'help2'
            pygame.display.update() # Update the display
        
        elif lobby.mode == 'help2': #Help page #2
            #Make changes to the screen
            arcadeScreen.blit(helpImg2, (0,0))
            backBtn.draw()
            nextBtn.draw()
            #Event checker
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    lobby.mode = 'quit'
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        lobby.mode = 'arcade'
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if backBtn.btn.collidepoint(event.pos):
                        soundFX = getSound()
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        lobby.mode = 'help'
                    elif nextBtn.btn.collidepoint(event.pos):
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        lobby.mode = 'help3'
                
            pygame.display.update() #Update the display    

        elif lobby.mode == 'help3': #Help page #3 (Contains credits)
            #Make changes to the screen
            arcadeScreen.blit(helpImg3,(0,0))
            backBtn = Button(100, 500, 'BACK', BLACK, 125, 50, arcadeScreen)
            backBtn.draw()
            pygame.display.update()
            clock.tick(60)
            #Event checker
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    lobby.mode = 'quit'
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if backBtn.btn.collidepoint(event.pos):
                        if soundFX == True:
                            pygame.mixer.Sound.play(btnSound)
                        lobby.mode = 'help2'
               
    return 'welcome' #Return welcome to the Prism_main file to continue the main menu
 
def pauseMenu(arcadeScreen): #Create a Pause Menu
    global pauseScreenText
    rect = pygame.Surface((800,600), pygame.SRCALPHA) #Create a rectangular surface
    arcadeScreen.blit(pauseScreenText, (300, 300))
    #Create the buttons
    optionsBtn = Button(300, 375, 'OPTIONS', BLACK, 220, 50, arcadeScreen)
    quitBtn = Button(300, 505, 'QUIT', BLACK, 220, 50, arcadeScreen)
    helpBtn = Button(300, 440, 'HELP', BLACK, 220, 50, arcadeScreen)
    arcadeScreen.blit(logo, (310,50))
    pygame.display.update()
    a = True # Create a never-ending loop
    while a: #While true
        #Make changes to the screen
        rect.fill((12,67,235,1))
        arcadeScreen.blit(rect, (0,0))
        pygame.display.update()
        arcadeScreen.blit(logo, (310,50))
        arcadeScreen.blit(pauseScreenText, (300, 300))
        #Draw buttons
        optionsBtn.draw()
        quitBtn.draw()
        helpBtn.draw()
        #Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Left click mouse
                if optionsBtn.btn.collidepoint(event.pos):
                    soundFX = getSound()
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    return 'options'
                elif quitBtn.btn.collidepoint(event.pos):
                    soundFX = getSound()
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    return 'quit'
                elif helpBtn.btn.collidepoint(event.pos):
                    soundFX = getSound()
                    if soundFX == True:
                        pygame.mixer.Sound.play(btnSound)
                    return 'help'
            if event.type == KEYDOWN: #Key is pressed down.
                if event.key == K_ESCAPE:
                    a = False
                    pygame.display.update()
                    return 'arcade'
           
    pygame.display.update() #Update the display
 
def keyCheck(machine, keys): #Function to check whether dylan has a key and update it into the database.
    valid = False 
    for key in keys:
        if key == machine:
            valid = True # Dylan has the key
            change_setting(key, 1)
            break
        else:
            pass
    return valid
 
def spawnBoy(screen): #Spawn dylan onto the map
    dylan = ArcadeBoy(screen,dylanForwardImg[0])
    dylan.spawn()
    return dylan

pygame.quit() #Quit pygame