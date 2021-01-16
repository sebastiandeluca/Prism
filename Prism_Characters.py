import pygame
import random
from pygame.locals import*


#fighterGameImg = [pygame.image.load('Prism_assets/Prism_img/Prism_dylan/Prism_DylanIdle.png')] ##CHANGE TO FIGHTERCHAR

#Arcade
#-----------------------------------------------------------------------------------------------------------------------------------------

class ArcadeBoy(pygame.sprite.Sprite):
    def __init__(self,surface,image):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.image = image
        
    def spawn(self):
        self.surface.blit(self.image,(250,150))
#-----------------------------------------------------------------------------------------------------------------------------------------

# SHADOW BOXING
#-----------------------------------------------------------------------------------------------------------------------------------------

#Defines the parent class for most units in shadowboxing
class Unit():
        def __init__(self, x, y, l, w, sprite, vel, upAnimation, downAnimation, leftAnimation, rightAnimation, surface):
            self.xpos = x
            self.ypos = y
            self.len = l
            self.wid = w
            self.sprite = pygame.image.load(sprite)
            self.sprite = pygame.transform.scale(self.sprite, (self.len, self.wid))
            self.uAnimation = upAnimation
            self.dAnimation = downAnimation
            self.lAnimation = leftAnimation
            self.rAnimation = rightAnimation
            self.surface = surface
            self.vel = vel
            self.orientation = 'Down'
            self.health = 6
            self.maxhealth = 6
            self.IEFrames = 0
            self.attackTimer = 0
            self.moveCounter = 0
            self.hitbox = (self.xpos + 20, self.ypos, 55, 80)
            self.moveUp = False
            self.moveDown = False
            self.moveLeft = False
            self.moveRight = False

#Defines the class for the boss in shadowboxing
class FightingBoss():
    def __init__(self, shootingAnimation, leftAnimation, surface):
        self.xpos = 650
        self.ypos = 100
        self.len = 150
        self.wid = 150
        self.health = 10
        self.maxhealth = 10
        self.vel = 3
        self.hitbox = (self.xpos + 20, self.ypos, 55, 100)
        self.lPAnimation = shootingAnimation
        self.lAnimation = leftAnimation
        self.surface = surface
        self.IEFrames = 0
        self.moveCounter = 0
        self.orientation = 'Left'
        self.timeLeftMoving = 0
        self.attackTimer = 0
        self.movingUporDown = 'Up'
    
    #Defines the function which moves the boss randomly
    def move(self):
        #if the boss has moved the randomly generated time in a direction, generate a new time to move and change his direction
        if self.timeLeftMoving == 0:
            self.timeLeftMoving = random.randint(30, 60)
            if self.movingUporDown == 'Up':
                self.movingUporDown = 'Down'

            elif self.movingUporDown == 'Down':
                self.movingUporDown = 'Up'
        
        #Boss is moving up
        elif self.movingUporDown == 'Up':
            if self.ypos - self.vel >= 50:
                self.ypos -= self.vel

        #Boss is moving down
        elif self.movingUporDown == 'Down':
            if self.ypos + self.len + self.vel <= 600:
                self.ypos += self.vel

        self.timeLeftMoving -= 1
        #Adjust hitbox
        self.hitbox = (self.xpos + 20, self.ypos, 55, 100)

    #def shoot(self):

#Creates the class for bullets, bullets do not use the parent class as they are missing many characteristics of the parant 
class Bullet():
    def __init__(self, x, y, vel, upAnimation, downAnimation, leftAnimation, rightAnimation, surface):
        self.xpos = x
        self.ypos = y
        self.vel = vel
        self.health = 2
        self.uAnimation = upAnimation
        self.dAnimation = downAnimation
        self.lAnimation = leftAnimation
        self.rAnimation = rightAnimation
        self.surface = surface
        self.moveCounter = 0
        self.attackTimer = 0
        
        self.orientation = 'Left'
        self.hitbox = ((self.xpos + 10, self.ypos + 10, 20, 15))

    #Moves the bullet
    def fly(self):
        if self.orientation == 'Up':
            self.ypos -= self.vel
            
        elif self.orientation == 'UpRight':
            self.ypos -= self.vel
            self.xpos += self.vel
            
        elif self.orientation == 'Right':
            self.xpos += self.vel
            
        elif self.orientation == 'DownRight':
            self.ypos += self.vel
            self.xpos += self.vel
            
        elif self.orientation == 'Down':
            self.ypos += self.vel
            
        elif self.orientation == 'DownLeft':
            self.ypos += self.vel
            self.xpos -= self.vel
            
        elif self.orientation == 'Left':
            self.xpos -= self.vel
            
        elif self.orientation == 'UpLeft':
            self.ypos -= self.vel
            self.xpos -= self.vel

        self.hitbox = (self.xpos + 10, self.ypos + 10, 20, 15)

    #Checks if the player attacked the bullet
    def checkIfPunched(self, playerPunch, playerDirection, points):
        punchX = playerPunch[0]
        punchY = playerPunch[1]
        punchL = playerPunch[2]
        punchW = playerPunch[3]
            
        #COLLISION DETECTION (REFER TO Prism_ShadowBoxing.py and the checkCollision function for details on these lines)
        if punchX <= self.hitbox[0] <= punchX + punchL or (punchX >= self.hitbox[0] and punchX + punchL <= self.hitbox[0] + self.hitbox[2]):
            if punchY <= self.hitbox[1] <= punchY + punchW:
                #Calls on the redirect function
                self.redirect(playerDirection)
                points += 100

            elif punchY <= self.hitbox[1] + self.hitbox[3] <= punchY +punchW:
                #Calls on the redirect function
                self.redirect(playerDirection)
                points += 100
                
        elif punchX <= self.hitbox[0] + self.hitbox[2] <= punchX + punchL or (punchX + punchL <= self.hitbox[0] + self.hitbox[2]) and (self.hitbox[0] <= punchX + punchL):
            if punchY <= self.hitbox[1] <= punchY + punchW or (self.hitbox[1] <= punchY and punchY + punchW <= self.hitbox[1] + self.hitbox[3]):
                #Calls on the redirect function
                self.redirect(playerDirection)
                points += 100

            elif punchY <= self.hitbox[2] +self.hitbox[3] <= punchY +punchW:
                #Calls on the redirect function
                self.redirect(playerDirection)
                points += 100

        #Update points   
        return points
        
    #Changes the direction of the bullet based on the direction of the player
    def redirect(self, playerOrientation):
                
        if playerOrientation == 'Up':
            self.orientation = 'Up'

        elif playerOrientation == 'UpRight':
            self.orientation = 'UpRight'

        elif playerOrientation == 'Right':
            self.orientation = 'Right'

        elif playerOrientation == 'DownRight':
            self.orientation = 'DownRight'

        elif playerOrientation == 'Down':
            self.orientation = 'Down'

        elif playerOrientation == 'DownLeft':
            self.orientation = 'DownLeft'

        elif playerOrientation == 'Left':
            self.orientation = 'Left'

        elif playerOrientation == 'UpLeft':
            self.orientation = 'UpLeft'

#Defines the class for the goon
class Goon(Unit):
    def __init__(self, x, y, l, w, sprite, vel, upAnimation, downAnimation, leftAnimation, rightAnimation, health, surface):
        super().__init__(x, y, l, w, sprite, vel, upAnimation, downAnimation, leftAnimation, rightAnimation, surface)
        self.health = health
        self.maxhealth = health
        
    #Defines the class which automatically moves it to the player

    def moveToPlayer(self, player):
        #player to the left
        if player.xpos < self.xpos:
            self.xpos -= self.vel
            
            #Player above
            if player.ypos < self.ypos:
                self.ypos -=  self.vel
                
                #If the gap between the x values is greater than the
                #Y values the enemy's will face left
                #Other wise they face up
                if self.xpos - player.xpos > self.ypos - player.ypos:
                    self.orientation = 'Left'
                    
                else:
                    self.orientation = 'Up'
                    
            #player below
            elif player.ypos > self.ypos:
                self.ypos += self.vel

                #If the gap between the x values is greater than the
                #Y values the enemy's will face left
                #Other wise they face down
                if self.xpos - player.xpos > player.ypos - self.ypos:
                    self.orientation = 'Left'

                else:
                    self.orientation = 'Down'
                
        #player to the right
        elif player.xpos > self.xpos:
            self.xpos += self.vel
            
            #Player above
            if player.ypos < self.ypos:
                self.ypos -=  self.vel

                #If the gap between the x values is greater than the
                #Y values the enemy's will face Right
                #Other wise they Up down
                if player.xpos - self.xpos > self.ypos - player.ypos:
                    self.orientation = 'Right'
                    
                else:
                    self.orientation = 'Up'
                    
            #Player below
            elif player.ypos > self.ypos:
                self.ypos +=  self.vel
                
                #If the gap between the x values is greater than the
                #Y values the enemy's will face left
                #Other wise they face down
                if player.xpos - self.xpos > player.ypos - self.ypos:
                    self.orientation = 'Right'

                else:
                    self.orientation = 'Down'
                    
        #Player above
        elif player.ypos < self.ypos:
            self.ypos -= self.vel
            self.orientation = 'Up'
            
        #Player below
        elif player.ypos > self.ypos:
            self.ypos += self.vel
            self.orientation = 'Down'
            
        else:
            self.xpos += 0
            self.ypos += 0
 
        #Adjust hitbox
        self.hitbox = (self.xpos + 20, self.ypos, 55, 90)
    
#Defines the class for the player's character
class Character(Unit):
    def __init__(self, x, y, l, w, sprite, vel, upAnimation, downAnimation, leftAnimation, rightAnimation, upPunch, downPunch, leftPunch, rightPunch, surface):
        super().__init__(x, y, l, w, sprite, vel, upAnimation, downAnimation, leftAnimation, rightAnimation, surface)
        self.punch = (0, 0, 0, 0)

        #PUNCH ANIMATIONS
        self.uPAnimation = upPunch
        self.dPAnimation = downPunch
        self.rPAnimation = rightPunch
        self.lPAnimation = leftPunch
        
    def attack(self):
        if self.orientation == 'Up':
            #pygame.draw.rect(self.surface, (0, 255, 0), (self.xpos + 50, self.ypos - 40, 30, 50), 2)
            self.punch = (self.xpos + 50, self.ypos - 40, 30, 50)

        elif self.orientation == 'UpRight':
            #pygame.draw.rect(self.surface, (0, 255, 0), (self.xpos + 75, self.ypos - 15, 30, 30), 2)
            self.punch = (self.xpos + 75, self.ypos - 15, 30, 30)

            
        elif self.orientation == 'Right':
            #pygame.draw.rect(self.surface, (0, 255, 0), (self.xpos + 60, self.ypos + 20, 50, 30), 2)
            self.punch = (self.xpos + 60, self.ypos + 20, 50, 30)

            
        elif self.orientation == 'DownRight':
            #pygame.draw.rect(self.surface, (0, 255, 0), (self.xpos + 75, self.ypos + 85, 30, 30), 2)
            self.punch = (self.xpos + 75, self.ypos + 85, 30, 30)


        elif self.orientation == 'Down':
            #pygame.draw.rect(self.surface, (0, 255, 0), (self.xpos + 20, self.ypos + self.len, 30, 50), 2)
            self.punch = (self.xpos + 20, self.ypos + self.len, 30, 50)

        elif self.orientation == 'DownLeft':
            #pygame.draw.rect(self.surface, (0, 255, 0), (self.xpos - 10, self.ypos + 85, 30, 30), 2)
            self.punch = (self.xpos - 10, self.ypos + 85, 30, 30)

        elif self.orientation == 'Left':
            #pygame.draw.rect(self.surface, (0, 255, 0), (self.xpos - 10,  self.ypos + 20, 50, 30), 2)
            self.punch = (self.xpos - 10,  self.ypos + 20, 50, 30)

        elif self.orientation == 'UpLeft':
            #pygame.draw.rect(self.surface, (0, 255, 0), (self.xpos - 10 , self.ypos - 15, 30, 30), 2)
            self.punch = (self.xpos - 10 , self.ypos - 15, 30, 30)

        
        
    def getMovement(self, event):
        #Get movement
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                self.moveUp = True
                self.moveDown = False
                
            if event.key == K_s:
                self.moveDown = True
                self.moveUp = False
                
            if event.key == K_d:
                self.moveRight = True
                self.moveLeft = False

            if event.key == K_a:
                self.moveLeft = True
                self.moveRight = False

        #check if movment stopped 
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                self.moveUp = False
                
            if event.key == K_s:
                self.moveDown= False

            if event.key == K_a:
                self.moveLeft = False
                
            if event.key == K_d:
                self.moveRight = False

            if event.key == K_SPACE:
                self.attack()
                self.attackTimer = 1

        #CHANGE ORIENTATION
        if self.moveUp == True:
            if self.moveLeft == True:
                self.orientation = 'UpLeft'
                
            elif self.moveRight == True:
                self.orientation = 'UpRight'
                
            else:
                self.orientation = 'Up'

        elif self.moveDown == True:
            if self.moveLeft == True:
                self.orientation = 'DownLeft'
                
            elif self.moveRight == True:
                self.orientation = 'DownRight'
                
            else:
                self.orientation = 'Down'

        else:
            if self.moveLeft == True:
                self.orientation = 'Left'

            elif self.moveRight == True:
                self.orientation = 'Right'
        
    #Defines the function which actually moves the player 
    def move(self):
        #If player is not attacking
        if self.attackTimer == 0:
            if self.moveUp and (self.hitbox[1] - self.vel) > 50:
                self.ypos -= self.vel + .5
                self.ver = 'U'

            if self.moveDown and (self.hitbox[1] + self.hitbox[3] + self.vel) < 600:
                self.ypos += self.vel + .5
                self.ver = 'D'

            if self.moveLeft and (self.hitbox[0] - self.vel > 50):
                self.xpos -= self.vel

            if self.moveRight and (self.hitbox[0] + self.hitbox[2] + self.vel < 750):
                self.xpos += self.vel
    
        #Increment the timer for his attack. AKA do the attack animation
        elif self.attackTimer < 10:
            self.attackTimer += 1

        #Reset attack timer to zero / Stop the attack
        else:
            self.attackTimer = 0

        #Move the hitbox along with the player
        self.hitbox = (self.xpos + 20, self.ypos, 55, 100)

#Defines the class for the healthpacks
class Healthpack():
    def __init__(self, x, y, l, w, image, animations, surface):
        self.xpos = x
        self.ypos = y
        self.len = l
        self.wid = w
        self.sprite = image
        self.uAnimation = animations
        self.dAnimation = animations
        self.lAnimation = animations
        self.rAnimation = animations
        self.orientation = 'Down'
        self.attackTimer = 0
        self.moveCounter = 0
        self.hitbox = (x, y, 21, 21)
        self.surface = surface
#----------------------------------------------------------------------------------------------------------------------------------------