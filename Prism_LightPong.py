import pygame
import random
from pygame.locals import *
from Prism_sql import insert_score

pygame.init()
pygame.mixer.init()
class PongBall(): # Class for Ball
    def __init__(self,direction,x,y,image):
        self.yspeed = 0
        self.xspeed = 3 
        self.dir = direction
        self.x = x
        self.y = y
        self.image = image
        self.hit = False

    def dirCheck(self):
        if self.dir == 'R': # If the ball is moving right keep it moving right
            self.x += self.xspeed
        elif self.dir == 'L': # Ball is moving left
            self.x -= self.xspeed
        else:
            pass
        if self.yspeed < 0:
            self.y += self.yspeed
        elif self.yspeed > 0:
            self.y += self.yspeed
        else:
            self.y -= self.yspeed
    
    def pointCheck(self): #Check if the ball has passed the point where a player would score
        if self.x > 700: #If its greater, left side wins
            win = 'Left'
        elif self.x < 100: #If its less than, right side wins
            win = 'Right'
        else:
            win = 'None'
        return win

    def wallCheck(self):
        if self.y <= 16:
            self.yspeed *= -1
        elif self.y >= 584:
            self.yspeed *= -1
            #input()
            
class Character(pygame.sprite.Sprite): # Base Character Class
    def __init__(self, img, y, hit):
        self.image = img # Get sprite
        self.y_loc = y # Get y location of character. (X is unchanging, unnecessary)
        self.hitStrength = hit # A variable that will change dependent on in-game events
        
class Player(Character):
    def __init(self,facing):
        super(Player,self).__init__() # Retrieve vars. from Character init
        self.dir = 'L'
    def move(self, key):
        if key == K_w or key == K_UP and self.y_loc >= -10: # Move player upward
            direction = 'U'
            
        elif key == K_s or key == K_DOWN and self.y_loc < 500: # Move player downward
            direction = 'D'
        elif key == K_SPACE:
            direction = 'O'
        else:
            pass
        return direction

    def hitBall(self, ball,sound):
        if ball.x >625 and ball.x < 660:
            if (ball.y >= self.y_loc) and (ball.y <= (self.y_loc + 100)):
                ball.image = ballHit[0]
                pygame.display.update()
                if (self.y_loc + 50) < ball.y + 4:
                    ball.yspeed = (self.y_loc - ball.y) /20 * -1
                    
                elif (self.y_loc + 50) >= ball.y + 4:

                    ball.yspeed = (self.y_loc - ball.y) /20

                
                if self.hitStrength > 1:
                    ball.xspeed += self.hitStrength
                else:
                    pass
                sound.play()
                ball.dir = 'L' # The user has hit the ball. Switch Direction
                ball.image = ballHit[1]
                pygame.display.update()

            else:
                ball.dir = 'R' # User has missed the ball

class NPC(Character):
    def __init(self,facing): # Initialize NPC
        super(Player,self).__init__() # Retrieve vars. from Character init
        self.dir = 'R'
        
    def hitBall(self, ball,sound): # NPC HITS BALL
        if ball.x >90 and ball.x <140:
            if (ball.y >= self.y_loc) and (ball.y <= (self.y_loc + 100)):
                ball.image = ballHit[0]
                pygame.display.update()
                if self.y_loc < ball.y + 10:
                    ball.yspeed = (self.y_loc - ball.y) /20
                    
                elif self.y_loc < ball.y + 10:
                    ball.yspeed = ((self.y_loc - ball.y) /20) * -1
                    
                ball.dir = 'R' # The user has hit the ball. Switch Direction
                sound.play()
                ball.image = ballHit[1]
                pygame.display.update()
            else:
                ball.dir = 'L' # User has missed the ball
        ball.xspeed = 3
    def move(self, ball,sound): # MOVE NPC TOWARD THE BALL
        moveVal = random.uniform(2.0,4.0)
        if ball.y > self.y_loc and ball.y < (self.y_loc+ 50):
            self.hitBall(ball,sound)
        elif ball.y > (self.y_loc + 45) and (self.y_loc < 540):
            
            self.y_loc += moveVal
        elif ball.y <= (self.y_loc + 45) and (self.y_loc > 10):
            self.y_loc -= moveVal
        else:
            pass      


 #SOUNDS
#SOUND
hitSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_LP_HitBall.ogg')
hitSound.set_volume(0.3)
gameMusic = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_LP_GameMusic.ogg')
gameMusic.set_volume(0.1)

#IMG
ballHit = [pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LightPong_BallHit1.png'),pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LightPong_BallHit2.png')]
startImg = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_Start.jpg')
startText =pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_Begin.png')
screenBG = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LightPongBG.png')
winText = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_YouWin.png')
loseText = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_YouLose.png')
contText = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_Continue.png')
bG = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_BG.jpg')
yesNoImg = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_YN.png')

def startScreen(): # A starting screen for the user to begin playing at their time of choice
    global startImg, startText,screenBG,gameMusic
    gameMusic.play(-1)
    #CREATE THE SCREEN
    lightPongScreen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Prism')
    programIcon = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_Logo.png')
    pygame.display.set_icon(programIcon)

    #set up loop
    counter = 0
    run = True
    while run:
        counter += 1
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                ###PLAY SOUND
                run = False
        if counter == 201:
            counter = 0
        elif 0 <= counter <= 100:
            showText = True
        elif 101 <= counter <= 200:
            showText = False
        lightPongScreen.blit(startImg,(0,0))
        if showText == True:
            lightPongScreen.blit(startText,(0,0))
        else:
            pass
        lightPongScreen.blit(screenBG,(0,0))
        pygame.display.update()
    win = runGame(lightPongScreen)
    return win
    
def checkIfPlay(lightPongScreen):
    global bG, contText, yesNoImg,screenBG
    counter = 0
    show = True
    run = True
    while run:
        counter += 1
        lightPongScreen.blit(bG,(0,0))
        if counter == 101:
            counter = 0
        elif 0 <= counter <= 50:
            show = True
        elif 51 <= counter <= 100:
            show = False
        if show == True:
            lightPongScreen.blit(contText,(0,0))
        else:
            pass
        lightPongScreen.blit(yesNoImg,(0,0))
        lightPongScreen.blit(screenBG,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_y:
                    play = True
                    run = False
                elif event.key == K_n:
                    play = False
                    run = False
    return play

def runGame(lightPongScreen): # Function that encompasses the entire game to allow it to be played from Arcade.py
    #COLOUR CODES
    CYAN = (8,163,255)
    YELLOW =(208,232,7)
    RED = (255,51,21)
    BLUE = (12,67,235)
    GREEN = (105,255,8)
    BLACK = (0,0,0)
    D_GREEN = (48, 110, 3)
    WHITE = (255,255,255)

    #IMAGE LOADING
            #CHARACTERS
    right = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_RightChar.png')
    rightSideChar = pygame.transform.scale(right, (100,100))
    left = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_LeftChar.png')
    leftSideChar = pygame.transform.scale(left, (100,100))
    font = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf',32)
            #BALL
    ballImg = [pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LightPong_Ball1.png'),pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LightPong_Ball2.png'),pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LightPong_Ball3.png')]
    
            #MAP
    screenBG = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LightPongBG.png')
    pongTable = pygame.image.load('Prism_assets/Prism_img/Prism_LightPong/Prism_LP_Table.png')
    clock = pygame.time.Clock()
    #Object Creation
    userPlayer = Player(rightSideChar, 256, 1)
    npcPlayer = NPC(leftSideChar,256,1)
    ball = PongBall('R',384,256,ballImg[0])

    #VARIABLES
    gameRun = True # RUN THE GAME
    moveDir = 'O' # BASE FOR MOVEMENT DIRECTION
    userPts = 0
    npcPts = 0
    hitCount = 0
    userWins = 0
    userWon = False

    while gameRun == True:
    
        try:
            scoreCount = font.render(str(npcPts) + ' : ' + str(userPts), True, RED, None)
        except pygame.error:
            scoreCount = font.render('0 : 0', True, RED, None)
        val = random.randint(0,2)
        ball.image = ballImg[val] # Randomize ball image
        
        #BLIT EVERYTHING TO SCREEN
        lightPongScreen.fill((100,100,100))
        lightPongScreen.blit(pongTable,(0,0))
        lightPongScreen.blit(userPlayer.image, (660,userPlayer.y_loc))
        lightPongScreen.blit(npcPlayer.image, (35,npcPlayer.y_loc))
        lightPongScreen.blit(ball.image,(ball.x, ball.y))
        lightPongScreen.blit(screenBG, (0,0))
        lightPongScreen.blit(scoreCount, (368,550))
        npcPlayer.move(ball,hitSound) # NPC MOVES IN ACCORDANCE TO BALL LOCATION
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_w or event.key == K_UP:
                    moveDir = 'U' #Player is moving Upward
                    
                if  event.key == K_s or event.key == K_DOWN:
                    moveDir = 'D' # Player is moving down
                if event.key == K_SPACE:
                    if hitCount < 5:
                        userPlayer.hitStrength =3
                        userPlayer.hitBall(ball,hitSound)
                        hitCount += 1
                    elif hitCount == 5:
                        userPlayer.hitStrength = 5
                        hitCount = 0

            if event.type == pygame.KEYUP:
                if event.key == K_w or event.key == K_UP:
                    moveDir = 'O' #Player is not moving
                    
                if  event.key == K_s or event.key == K_DOWN:
                    moveDir = 'o' # Player is not moving 
        ball.wallCheck()
        pts = ball.pointCheck() # Check if someone has scored
        
        if pts == 'Left': # NPC has scored
            hitCount = 0

            npcPts += 1
            ball.x = 384
            ball.yspeed = 0
            ball.y = 256
            userPlayer.y_loc = 256
            npcPlayer.y_loc = 256
            restart = True
        elif pts == 'Right': # player has scored
            hitCount = 0
            userPts +=1 
            ball.x = 384
            ball.yspeed = 0
            ball.y = 256
            userPlayer.y_loc = 256
            npcPlayer.y_loc = 256
            restart = True
        else: # Nobody has scored
            restart = False

        if restart == True: # Change ball direction randomly when point is given
            direc = random.randint(1,2)
            if direc == 1:
                ball.dir = 'R'
            else:
                ball.dir = 'L'
        ball.dirCheck()
          
        #MOVEMENT
        if moveDir == 'U'and userPlayer.y_loc >= -40:
            userPlayer.y_loc -= 3
        elif moveDir == 'D' and userPlayer.y_loc <= 540:
            userPlayer.y_loc += 3

        if userPts >=5:
            userWins += 1
            userWon = True
            lightPongScreen.fill(WHITE)
            lightPongScreen.blit(bG,(0,0))
            lightPongScreen.blit(winText,(0,0))
            lightPongScreen.blit(screenBG,(0,0))
            pygame.display.update()
            pygame.time.delay(5000)
            yesNo = checkIfPlay(lightPongScreen) # CHECK IF THE USER WANTS TO CONTINUE
            if yesNo == False:
                gameMusic.stop()
                gameRun = False
            elif yesNo == True:
                npcPts = 0
                userPts = 0
                runGame(lightPongScreen)
            
        elif npcPts >= 5:
            if userWon == True:
                pass
            else:
                userWon = False
            lightPongScreen.fill(WHITE)
            lightPongScreen.blit(bG,(0,0))
            lightPongScreen.blit(loseText,(0,0))
            lightPongScreen.blit(screenBG,(0,0))
            pygame.display.update()
            #insert_score('LightPong', userPts)
            pygame.time.delay(5000)
            yesNo = checkIfPlay(lightPongScreen) # CHECK IF THE USER WANTS TO CONTINUE
            if yesNo == False:
                gameMusic.stop()
                gameRun = False
            elif yesNo == True:
                npcPts = 0
                userPts = 0
                runGame(lightPongScreen)
                
        insert_score('LightPong', userWins)
        pygame.display.update()
        clock.tick(60)
    return userWon
