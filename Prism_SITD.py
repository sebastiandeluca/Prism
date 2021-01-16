import pygame
from pygame.locals import *
import random
from Prism_sql import insert_score

#initialize pygame
pygame.init()
pygame.mixer.init()


dudeTransition = [pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_WhiteChar.png'), pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_TransChar1.png'), pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_TransChar2.png'), pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_TransChar3.png'), pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_DarkChar.png')]
dudeTransitionImg = [] #list with scaled up pictures
for img in dudeTransition:
    img = pygame.transform.scale(img,(100,100))
    dudeTransitionImg.append(img)

#COLOUR
#Define all the basic tuples for Colors.
CYAN = (8,163,255)
YELLOW =(208,232,7)
RED = (255,51,21)
BLUE = (12,67,235)
GREEN = (105,255,8)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (127, 127, 127)

#load and transform the white and black tokens to be used in Shot in the Dark
tokenWhite = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_TokenWhite.png')
tokenBlack = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_TokenBlack.png')
tokenWhite = pygame.transform.scale(tokenWhite, (50, 50))
tokenBlack = pygame.transform.scale(tokenBlack, (50, 50))

#load and transform the base characters that the user can transform into
dropperChar = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_WhiteChar.png')
dropperChar = pygame.transform.scale(dropperChar, (100,100))


#load and transform the background image for the game
dropperBg = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_BG.png')
dropperBg = pygame.transform.scale(dropperBg, (5120, 10240))


#load the top of the arcade machine to show that the game is being played in an arcade machine.
dropperTop = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_Overlay.png')

#boolean for completing the nessessary requirements to move on the game.
complete = False

#load up the background music for the game
SITD_Background = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_SITD_GameMusic.ogg')

#load in the startup screens
startScreen1 = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_StartScreen.jpg')
startScreen2 = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_StartScreenText.png')



def gameScreen(dropperScreen): # Show the start menu of the game
    SITD = dropperScreen # 
    SITD_Background.set_volume(0.3)
    SITD_Background.play(-1) #set and play music
    run = True
    counter = 0
    while run: # Loop the game
        counter += 1
        if counter == 201:
            counter = 0
        elif  0 <= counter <= 100:
            dropperScreen.blit(startScreen1,(0,0))
            dropperScreen.blit(dropperTop, (0, 0))
        elif 101 <= counter <= 200:
            dropperScreen.blit(startScreen2,(0,0))
            pygame.display.update()


        for event in pygame.event.get():
            if event.type == KEYDOWN: # If the user presses a key, stop the loop
                
                if event.key == K_ESCAPE:
                    run = False
                    
                else:
                    run = False

def endScreen(dropperScreen, score,font): #show the lose screen of the game once the user dies.

    #load up images
    loseScreen1 = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_LoseScreen.jpg')
    loseScreenText = pygame.image.load('Prism_assets/Prism_img/Prism_SITD/Prism_SITD_LoseScreenText.png')

    #declare initial variables
    run = True
    viewcount = 0
    counter = 0
    #render the final score into a string viewable on the screen
    finalScore = font.render(str(score) + ' TOKENS', True, WHITE, None)
    while run:
        counter += 1
        viewcount += 1
        if counter == 201:
            counter = 0
        elif 0 <= counter <= 100:
            showText = True
        elif 101 <= counter <= 200:
            showText = False
        dropperScreen.blit(loseScreen1,(0,0))
        dropperScreen.blit(finalScore,(348,300))
        if showText == True:
            dropperScreen.blit(loseScreenText,(0,0)) 
        else:
            pass
        dropperScreen.blit(dropperTop,(0,0)) #blit the top of the arcade machine
        pygame.display.update()
        if viewcount == 300:
            run = False
    
    SITD_Background.stop() #stop the background music
                    
def randomVals():
    s = 1 # speed of game
    c = random.randint(1,2) #color
    x = random.randint(0,800) #x coord
    y = random.randint(0, 600) #y coord
    w = random.randint(50,150)# width
    h = 30 #height, constant
    t = random.randint(1,3) #token spawnability

    #randomize the color
    if c == 1:
        c = BLACK
    elif c == 2:
        c = WHITE
    listVal = []
    listVal.extend((s,c,x,y,w,h,t))
    return listVal


#create the initial class for the three Obstacles used in-game.
class Obstacle():
    def __init__(self,surface, speed, colour, x, y, width, height):
        self.surface = surface
        self.speed = speed
        self.colour = colour
        self.x = x
        self.y = 600
        self.width = width
        self.height = height
        

    def draw(self): #function for the class to draw out the obstacle
        
        for n in range(self.speed):
            self.y -= 5 #move the obstacle upward
            yaxisRandomizer = random.randint(1,2)
            if yaxisRandomizer == 1:
                
                if self.y <= 0:
                    self.y = 650 #This is done to randomize spacing between platforms.
                    self.x = random.randint(100, 650)
                    self.width = random.randint(50, 150)
                    randomColor = random.randint(1,2)
                    if randomColor == 1:
                        self.colour = BLACK
                    elif randomColor == 2:
                        self.colour = WHITE
                    
            elif yaxisRandomizer == 2:
                if self.y <= 0:
                    self.y = 900 #This is done to randomize spacing between platforms
                    
                    self.x = random.randint(100, 650)
                    self.width = random.randint(50, 150)
                    randomColor = random.randint(1,2)
                    if randomColor == 1:
                        self.colour = BLACK
                    elif randomColor == 2:
                        self.colour = WHITE
                    
                        
            
            if self.colour == BLACK:
                #create a gray outline to the black platform if the color is indeed black.
                pygame.draw.rect(self.surface, GRAY, [(self.x - 2), (self.y - 2), (self.width + 4), (self.height + 4)])
                pygame.draw.rect(self.surface, self.colour, [self.x,self.y,self.width,self.height])
            else:
                #outline not needed for white platform, so it blits just by itself.
                pygame.draw.rect(self.surface, self.colour, [self.x,self.y,self.width,self.height])

class ColorChanger():
    #color changer class for the Gray bar, third obstacle.
    def __init__(self, surface):
        self.x = 0
        self.y = 600
        self.width = 800
        self.height = 10
        self.surface = surface

    def draw(self):

        self.y -= 5 
        if self.y < 0:
            self.y = 1800
        #does not change color, therefore stays constant and only checks if the y is out of the scope of the game.

        #draw the gray bar.
        pygame.draw.rect(self.surface, GRAY, [self.x, self.y, self.width, self.height])


#actual game definition
def dropper(imagelist,dropperScreen):
    
    #define font and caption of game
    font = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf',32)
    pygame.display.set_caption('Prism')
    
    #DECLARING OF INITIAL VARIABLES
    x_loc = 400
    y_loc = 100
    img_x = 0
    img_y = 0
    imagecounter = 0
    whiteDude = True
    darkDude = False

    #Clock
    clock = pygame.time.Clock()
    runDropper = True
    mode = 'dropper'
    moveLeft = False
    moveRight = False
    moveDown = True
    obsType = randomVals()
    changecount = 0
    initial = True
    imageChange = False
    tcontact1 = False
    tcontact2 = False

    #define initial obstacles and their properties
    obstacle1 = Obstacle(dropperScreen, obsType[0], obsType[1], obsType[2], obsType[3], obsType[4], obsType[5])
    obstacle2 = Obstacle(dropperScreen, obsType[0], obsType[1], obsType[2], obsType[3], obsType[4], obsType[5])
    obstacle3 = ColorChanger(dropperScreen)
    scoreincreaser = False
    #load the music
    pygame.mixer.music.load('Prism_assets/Prism_sounds/Prism_Pickup.wav')

    #initial variables, extended for tokens and score
    token1x = 0
    token1y = 0

    token2x = 0
    token2y = 0


    blitToken1 = True
    blitToken2 = True

    tokenCount = 0
    score = 0
    
    while runDropper:
        if mode == 'dropper':
            #obtain initial random values
            obsType = randomVals()

            #blit the background
            dropperScreen.blit(dropperBg, (img_x, img_y))

            #render and blit the player's score
            playerScore = font.render(str(score), True, WHITE, None)
            playerScoreIdentity = font.render(('TOKENS:'), True, WHITE, None)

            dropperScreen.blit(playerScore, (450, 50))
            dropperScreen.blit(playerScoreIdentity, (320, 50))
            

            if changecount == 0 and imageChange == True:
                for x in range (0,5): #change the color through a swift animation
                    dropperScreen.blit(imagelist[x], (x_loc, y_loc))
                    pygame.time.delay(20) #delay briefly to show the user the color transition
                    dropperScreen.blit(dropperTop,(0,0)) 
                    pygame.display.update()
                    #draw obstacles
                    obstacle1.draw()
                    obstacle2.draw()
                    obstacle3.draw()
                     #update screens
                imageChange = False #stop  the image change

                
            elif changecount == 1 and imageChange == True:
                for x in range (4,-1, -1): #change the color through a swift animation
                    dropperScreen.blit(imagelist[x], (x_loc, y_loc))
                    pygame.time.delay(20) #delay briefly to show the user the color transition
                    dropperScreen.blit(dropperTop,(0,0)) 
                    pygame.display.update()
                    #draw the obstacles
                    obstacle1.draw()
                    obstacle2.draw()
                    obstacle3.draw()
                    
                imageChange = False #stop the image change
            else:
                if changecount == 1:
                    dropperScreen.blit(imagelist[0], (x_loc, y_loc)) #show the white image on startup after transition
                elif changecount == 0:
                    dropperScreen.blit(imagelist[4], (x_loc, y_loc)) #show the black image on startup after transition
            
            #loop for each time an event is given
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runDropper = False

                #detection if statements for when a key is pressed
                if event.type == pygame.KEYDOWN:
                    #move the character left if the key is pressed
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        moveLeft = True
                        moveRight = False
                        
                    #move the character right if the key is pressed
                    if event.type == pygame.K_RIGHT or event.key == pygame.K_d:
                        moveRight = True
                        moveLeft = False

                    if event.key == pygame.K_SPACE: #space = controls for color swap
                        if whiteDude == True: #changes the player's colors to black
                            changecount = 1 #one means changing to black
                            darkDude = True
                            whiteDude = False
                            imageChange = True
                            
                        elif darkDude == True: #changes the player's color to white
                            changecount = 0 #zero means back to white
                            darkDude = False
                            whiteDude = True
                            imageChange = True
                            
                        

                        
                            

                if event.type == pygame.KEYUP: #make the user stop moving if the key is released

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        moveLeft = False

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        moveRight = False

                        
            if moveLeft == True: #move the player left if the left key is pressed.
                if x_loc < 35 and x_loc < 635:
                    x_loc += 0 #boundary check if not in window
                else:
                    x_loc -= 5
                    
            if moveRight == True: #move the player right if the right key is pressed.
                if x_loc > 635 and x_loc > 35:
                    x_loc -= 0 #boundary check if not in window
                else:
                    x_loc += 5

                
            
            if moveDown == True: #set options for game when the player is falling
                img_y -= 10 
                imagecounter -= 10 #duplicate variable for stopping purposes
                if img_y <= -5000:
                    img_y = 0 #looping the image when the picture gets far enough
                    imagecounter = 0





                    
            elif moveDown == False:
                img_y = imagecounter  #stop the background
                obstacle1.y += 5 
                obstacle2.y += 5 #contradict the upward movement of the platform, making the platforms stop
                if platform1 == True: #if the first platform is landed on
                    if obstacle1.colour == BLACK and darkDude == True:
                        #stop the game if the user is the incorrect color
                        runDropper = False
                        
                    elif obstacle1.colour == WHITE and whiteDude == True:
                        #stop the game if the user is the incorrect color
                        runDropper = False
                        
                    else:
                        pass
                elif platform2 == True: #if the second platform is landed on
                    if obstacle2.colour == BLACK and darkDude == True:
                        #stop the game if the user is the incorrect color
                       runDropper = False
                        
                    elif obstacle2.colour == WHITE and whiteDude == True:
                        #stop the game if the user is the incorrect color
                        runDropper = False
                        
                    



                
            
            
                
                





            '''
            Checking if the platforms' Y value is close to each other.
            If this occurs, set one of the platforms' Y values to be BELOW the other.
            '''
            
            obstacle1yspawncheck = obstacle1.y + 100
            obstacle2yspawncheck = obstacle2.y + 100


            if obstacle2.y >= obstacle1.y and obstacle2.y <= obstacle1yspawncheck:
                obstacle2.y = 1000
                
            if obstacle1.y >= obstacle2.y and obstacle1.y <= obstacle2yspawncheck:
                obstacle1.y = 1000
            
            
            



                




            boundary1left = obstacle1.x - (obstacle1.width / 2) #set the leftward boundary for the first platform
            boundary1right = obstacle1.x + (obstacle1.width / 2)#set the rightward boundary for the first platform

            boundary2left = obstacle2.x - (obstacle2.width / 2) #set the leftward boundary for the second platform
            boundary2right = obstacle2.x + (obstacle2.width / 2)#set the rightward boundary for the second platform

            if x_loc >= boundary1left and x_loc <= boundary1right and obstacle1.y <= 200 and obstacle1.y >= 195:
                #recognize if the player lands on the first platform
                moveDown = False
                platform1 = True
                platform2 = False
                
                
                
                
            
            
                

            elif x_loc >= boundary2left and x_loc <= boundary2right and obstacle2.y == 200:
                #recognize if the player lands on the second platform
                moveDown = False
                platform2 = True
                platform1 = False

                
            elif x_loc < boundary2left or x_loc > boundary2right and obstacle2.y <= 200 and obstacle2.y >= 195:
                #detection if out of range of the platform
                moveDown = True
                

            elif x_loc <  boundary1left or x_loc > boundary1right and obstacle1.y <= 200 and obstacle1.y >= 195:
                #detection if out of range of the platform
                moveDown = True
                
            

            #draw the obstacles
            obstacle1.draw()
            obstacle2.draw()
            obstacle3.draw()

            if obstacle3.y == 150: #if the player passes through the gray obstacle
                
                if whiteDude == True: #changes the player's colors to black
                    changecount = 1 #one means changing to black
                    darkDude = True
                    whiteDude = False
                    imageChange = True
                            
                elif darkDude == True: #changes the player's color to white
                    changecount = 0 #zero means back to white
                    darkDude = False
                    whiteDude = True
                    imageChange = True





            '''
            The Following lines of code focus on tokens and the scoring system
            '''

            #set the boundaries for each token's position

            #first token
            token1x = obstacle1.x + (obstacle1.width / 2) - 25
            token1y = (obstacle1.y - 50)
            
            #second token      
            token2x = obstacle2.x + (obstacle2.width / 2) - 25
            token2y = obstacle2.y - 50


            


            #token hitbox boundaries

            token1xboundaryleft = token1x - 100
            token1xboundaryright = token1x + 25

            token2xboundaryleft = token2x - 100
            token2xboundaryright = token2x + 25





            #check if the token associated with the first platform is showing or not
            if blitToken1 == True:
                if darkDude == False:
                    dropperScreen.blit(tokenBlack, (token1x, token1y))
                elif whiteDude == False:

                    dropperScreen.blit(tokenWhite, (token1x, token1y))

                if x_loc >= token1xboundaryleft and x_loc <= token1xboundaryright and token1y <= 195 and token1y >= 150:
                    #detection that the user is making contact with the token
                    tcontact1 = True





            #check if the token associated with the second platform is showing or not
            if blitToken2 == True:
                if darkDude == False:
                        
                    dropperScreen.blit(tokenBlack, (token2x, token2y))
                elif whiteDude == False:
                        
                    dropperScreen.blit(tokenWhite, (token2x, token2y))

                if x_loc >= token2xboundaryleft and x_loc <= token2xboundaryright and token2y <= 195 and token2y >= 150:
                    tcontact2 = True

            #token contact for first token
            if tcontact1 == True:
                tcontact1 = False
                tcontact2 = False
                blitToken1 = False
        
            #token contact for second token
            if tcontact2 == True:
                tcontact1 = False
                tcontact2 = False
                blitToken2 = False


            #checking if second token has been picked up
            if blitToken2 == False:
                scoreincreaser = True
                if obstacle2.y < 15:
                    blitToken2 = True
            elif blitToken2 == True:
                if darkDude == False: #blit the tokens if it has not been picked up 
                    dropperScreen.blit(tokenBlack, (token2x, token2y))
                elif whiteDude == False:
                        
                    dropperScreen.blit(tokenWhite, (token2x, token2y))


            #checking if first token has been picked up
            if blitToken1 == False:
                scoreincreaser = True
                if obstacle1.y < 15:
                    blitToken1 = True
                    
            elif blitToken1 == True:
                if darkDude == False:
                    dropperScreen.blit(tokenBlack, (token1x, token1y))
                elif whiteDude == False:

                    dropperScreen.blit(tokenWhite, (token1x, token1y))




            
            #increase the score for the player
            if scoreincreaser == True and token1y == 150 and x_loc >= token1xboundaryleft and x_loc <= token1xboundaryright:
                score += 1
                scoreincreaser = False #score no longer increases
                pygame.mixer.music.play() #play the sound effect for picking up tokens


            elif scoreincreaser == True and token2y == 150 and x_loc >= token2xboundaryleft and x_loc <= token2xboundaryright:
                score += 1
                scoreincreaser = False #the score no longer increases
                pygame.mixer.music.play()#play the sound effect for picking up tokens

            dropperScreen.blit(dropperTop,(0,0)) 
            pygame.display.update() #update screen after drawings
            clock.tick(60) #frames per second of game
            

    
    endScreen(dropperScreen, score,font)

    if score >= 25:
        complete = True #return a true variable for the story to advance
    
    else:
        complete = False
    insert_score('ShotInTheDark', score)
    return complete

    #return 'welcome'

def run(dylanInput): #put everything into one function for the game to run in another program
    global dudeTransitionImg
    if dylanInput == True:     
        dropperHeight = 600
        dropperWidth = 800
        dropperScreen = pygame.display.set_mode((dropperWidth, dropperHeight))
        gameScreen(dropperScreen)
        win = dropper(dudeTransitionImg,dropperScreen)
        dylanInput = False
    else:
        win = False
        
    return win #return the win condition

pygame.quit()  #quit program






