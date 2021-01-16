import pygame
import random
from Prism_Characters import Unit, Character, Goon, FightingBoss, Bullet, Healthpack
from pygame.locals import *
from Prism_Resources import fade_in
from Prism_sql import insert_score

pygame.init()

#Checks if unit collided with otherunit
def checkCollision(unit, otherUnit):
    
    #Hitbox collision based on unit's leftmost point being between otherunit's x values of its hitbox
    if otherUnit.hitbox[0] <= unit.hitbox[0] <= otherUnit.hitbox[0] + otherUnit.hitbox[2] or (otherUnit.hitbox[0] >= unit.hitbox[0] and otherUnit.hitbox[0] + otherUnit.hitbox[2] <= unit.hitbox[0] + unit.hitbox[2]):

        #Checks if the unit's topmost point is in between otherunit's y values of its hitbox
        if otherUnit.hitbox[1] <= unit.hitbox[1] <= otherUnit.hitbox[1] + otherUnit.hitbox[3]:
            return True

        #Checks if the unit's bottommost point is in between the otherunit's y values of its hitbox   
        elif otherUnit.hitbox[1] <= unit.hitbox[1] + unit.hitbox[3] <= otherUnit.hitbox[1] + otherUnit.hitbox[3]:
            return True
        
    #Hitbox collision based on unit's rightmost point beting between otherunit's x values of its hitbox
    elif otherUnit.hitbox[0] <= unit.hitbox[0] + unit.hitbox[2] <= otherUnit.hitbox[0] + otherUnit.hitbox[2] or (otherUnit.hitbox[0] + otherUnit.hitbox[2] <= unit.hitbox[0] + unit.hitbox[2]) and (unit.hitbox[0] <= otherUnit.hitbox[0] + otherUnit.hitbox[2]):

        #Checks if the unit's topmost point is in between the otherunit's y values of its hitbox
        if otherUnit.hitbox[1] <= unit.hitbox[1] <= otherUnit.hitbox[1] + otherUnit.hitbox[3] or (unit.hitbox[1] <= otherUnit.hitbox[1] and otherUnit.hitbox[1] + otherUnit.hitbox[3] <= unit.hitbox[1] + unit.hitbox[3]):
            return True
        
        #Checks if the unit's bottommost point is in between the otherunit's y values of its hitbox
        elif otherUnit.hitbox[1] <= unit.hitbox[1] + unit.hitbox[3] <= otherUnit.hitbox[1] + otherUnit.hitbox[3]:
            return True

#Checks if the player's fist's hitbox is touching any goons
def hitEnemies(me):
    
    for x in range(len(enemies)):
        
        #If Enemy is not invincible
        if enemies[x].IEFrames == 0:

            #Checks if the enemy's leftmost point is in between the x values of the punch
            if me.punch[0] <= enemies[x].hitbox[0] <= me.punch[0] + me.punch[2] or (me.punch[0] >= enemies[x].hitbox[0] and me.punch[0] + me.punch[2] <= enemies[x].hitbox[0] + enemies[x].hitbox[2]):

                #checks if the enemy's topmost point is in between the y values of the punch
                if me.punch[1] <= enemies[x].hitbox[1] <= me.punch[1] + me.punch[3]:
                    enemies[x].IEFrames = 1
                    enemies[x].health -= 1
                    
                #checks if the enemy's bottommost point is in between the y values of the punch
                elif me.punch[1] <= enemies[x].hitbox[1] + enemies[x].hitbox[3] <= me.punch[1] +me.punch[3]:
                    enemies[x].IEFrames = 1
                    enemies[x].health -= 1
                    
            #Checks if the enemiy's rightmost point is in between the x values of the punch
            if me.punch[0] <= enemies[x].hitbox[0] + enemies[x].hitbox[2] <= me.punch[0] + me.punch[2] or (me.punch[0] + me.punch[2] <= enemies[x].hitbox[0] + enemies[x].hitbox[2]) and (enemies[x].hitbox[0] <= me.punch[0] + me.punch[2]):

                #checks if the enemy's topmost point is in between the y values of the punch
                if me.punch[1] <= enemies[x].hitbox[1] <= me.punch[1] + me.punch[3] or (enemies[x].hitbox[1] <= me.punch[1] and me.punch[1] + me.punch[3] <= enemies[x].hitbox[1] + enemies[x].hitbox[3]):
                    enemies[x].IEFrames = 1
                    enemies[x].health -= 1
                    
                #checks if the enemy's bottommost point is in between the y values of the punch
                elif me.punch[1] <= enemies[x].hitbox[1] + enemies[x].hitbox[3] <= me.punch[1] +me.punch[3]:
                    enemies[x].IEFrames = 1
                    enemies[x].health -= 1

        #If the enemy is invincible, reduce their time invincible by 1 frame
        else:
            enemies[x].IEFrames -= 1

#Moves enemies away from the player after being hit
def moveEnemiesBack(me):
    for x in range(len(enemies)):
        if enemies[x].IEFrames != 0:
            if me.orientation == 'Up':
                enemies[x].ypos -= 30
                
            if me.orientation == 'UpRight':
                enemies[x].ypos -= 20
                enemies[x].xpos += 20
                
            if me.orientation == 'Right':
                enemies[x].xpos += 30
                
            if me.orientation == 'DownRight':
                enemies[x].ypos += 20
                enemies[x].xpos += 20
                
            if me.orientation == 'Down':
                enemies[x].ypos += 30
                
            if me.orientation == 'DownLeft':
                enemies[x].ypos += 20
                enemies[x].xpos -= 20
                
            if me.orientation == 'Left':
                enemies[x].xpos -= 30
                
            if me.orientation == 'UpLeft':
                enemies[x].ypos -= 20
                enemies[x].xpos -= 20

def killEnemies(points, surface):
    y = len(enemies)
    x = 0
    while x < y:
        if enemies[x].health <= 0:

            #Randomly drops a health pack if the enemy died
            healthpackDrop = random.randint(0,5)
            if healthpackDrop == 3:   
                pack = Healthpack(enemies[x].xpos, enemies[x].ypos, 21, 21, healthpackHalfHeart1, healthpackAnimation, surface)
                healthpacks.append(pack)

            enemies.pop(x)
            x -= 1
            y -= 1
            
            #increase pointcount
            points += 1000
            
        x += 1

    return points

def removeOutOfMapBullets(projectiles):
    y = len(projectiles)
    x = 0
    while x < y:
        #if bullets are outside the boundaries of the map
        if projectiles[x].xpos <= -20 or projectiles[x].xpos >= 820 or projectiles[x].ypos >= 600 or projectiles[x].ypos <= -20:
            projectiles.pop(x)
            x -= 1
            y -= 1
        x += 1

    return projectiles

#The map is a 1600x600 img. Therefore the map is blitted at different x values to swap between maps. This function blits the map based on the mapnumber passed into the function 
def updateMap(counter, surface):
    surface.blit(image, ((0 - counter * 800), (0)))

#Draws an entity
def drawEntity(entity, surface):
    image = 0

    #Move counter regulates which of the two moving animations of the entity will be blitted
    #If move counter > 100 it will reset to zero
    if entity.moveCounter > 100:
        entity.moveCounter = 0
        
    if entity.moveCounter > 50:
        image = 0

    elif entity.moveCounter <= 50:
        image = 1

    #Draws the attacking image
        
    if entity.attackTimer != 0:

        #Up
        if entity.orientation == 'Up' or entity.orientation == 'UpRight':
            surface.blit(entity.uPAnimation, (entity.xpos, entity.ypos))

        #Down
        elif entity.orientation == 'Down' or entity.orientation == 'DownLeft' or entity.orientation == 'DownRight':
            surface.blit(entity.dPAnimation, (entity.xpos, entity.ypos))

        #Left
        elif entity.orientation == 'Left' or entity.orientation == 'UpLeft':
            surface.blit(entity.lPAnimation, (entity.xpos, entity.ypos))

        #Right
        elif entity.orientation == ('Right'):
            surface.blit(entity.rPAnimation, (entity.xpos, entity.ypos))

    #Moving images

    #Up
    elif entity.orientation == 'Up':
        surface.blit(entity.uAnimation[image], (entity.xpos, entity.ypos))

    #Down
    elif entity.orientation == 'Down':
        surface.blit(entity.dAnimation[image], (entity.xpos, entity.ypos))

    #Left
    elif entity.orientation == 'Left' or entity.orientation == 'UpLeft' or entity.orientation == 'DownLeft':
        surface.blit(entity.lAnimation[image], (entity.xpos, entity.ypos))

    #Right
    elif entity.orientation == 'Right' or entity.orientation == 'UpRight' or entity.orientation == 'DownRight':
        surface.blit(entity.rAnimation[image], (entity.xpos, entity.ypos))

    entity.moveCounter += 2
    

#Draws heart images
def drawHearts(health, surface):
    if health == 6:
        surface.blit(fullHeart, (110, 10))
        surface.blit(fullHeart, (160, 10))
        surface.blit(fullHeart, (210, 10))

    if health == 5:
        surface.blit(halfHeart, (110,10))
        surface.blit(fullHeart, (160, 10))
        surface.blit(fullHeart, (210, 10))

    if health == 4:
        surface.blit(emptyHeart, (110,10))
        surface.blit(fullHeart, (160, 10))
        surface.blit(fullHeart, (210, 10))
    
    if health == 3:
        surface.blit(emptyHeart, (110,10))
        surface.blit(halfHeart, (160, 10))
        surface.blit(fullHeart, (210, 10))
    
    if health == 2:
        surface.blit(emptyHeart, (110,10))
        surface.blit(emptyHeart, (160, 10))
        surface.blit(fullHeart, (210, 10))
    
    if health == 1:
        heartX = random.randint(208, 212)
        heartY = random.randint(9, 11)
        surface.blit(emptyHeart, (110,10))
        surface.blit(emptyHeart, (160, 10))
        surface.blit(halfHeart, (heartX, heartY))

#Draws a healthbar above the entered entity
def drawHealthbar(entity, surface):
    pygame.draw.rect(surface, BLACK, (entity.xpos + 20,entity.ypos - 10,entity.hitbox[2],15), 2)    
    healthBarWid = (entity.hitbox[2] - 4) * (entity.health / entity.maxhealth) 
    pygame.draw.rect(surface, RED, (entity.xpos + 22, entity.ypos - 7, healthBarWid , 10))

#Displays controls to the user for a second and a half before the game starts
def displayPrompt(surface):
    
    promptCounter = 90
    prompt1 = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_ShdwBox_Prompt1.png')
    prompt1 = pygame.transform.scale(prompt1, (600,550))
    prompt2 = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_ShdwBox_Prompt2.png')
    prompt2 = pygame.transform.scale(prompt2, (600,550))

    #Blits different images based on the time to create an animation
    while promptCounter > 0:
        updateMap(mapnum, surface)
        if promptCounter < 30:
            surface.blit(prompt2, (100,0))
            
        elif promptCounter < 60:
            surface.blit(prompt1, (100,0))
            
        elif promptCounter < 90:
            surface.blit(prompt2, (100,0))

        promptCounter -= 1
        pygame.display.update()
        clock.tick(60)

#cutscene of 4 goons abuducting the player
def cutScene(me, surface):
    me.attackTimer = 0
    me.orientation = 'Down'
    #Moves player to the middle
    me.xpos = 350
    me.ypos = 250
    #surface.blit(me.sprite, (350, 250))
    updateMap(0, surface)
    drawEntity(me, surface)

    #Prints the text and leaves it for 2 seconds
    cutSceneText = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_ShdwBox_cutSceneText.png')
    cutSceneText = pygame.transform.scale(cutSceneText, (800,600))
    surface.blit(cutSceneText, (0,0))
    pygame.display.update()
    pygame.time.delay(2000)

    #Upmost Goon
    goon1Cords = [350, 0]

    #RightMost Goon
    goon2Cords = [550, 250]

    #Bottom Goon
    goon3Cords = [350, 500]

    #Right goon
    goon4Cords = [150, 250]
    
    movingCounter = 0
    seconds = 0

    #fade(800, 600)
    image = 0
    for seconds in range(0 ,180):
        updateMap(0, surface)
        drawEntity(me, surface)

        #Selects which moving image to print based on time
        if movingCounter >= 100:
            movingCounter = 0
            
        if movingCounter >= 0:
            image = 0

        if movingCounter >= 50:
            image = 1

        #Blits all for goons 
        surface.blit(goonMovingDown[image], (goon1Cords[0], goon1Cords[1]))
        surface.blit(goonMovingLeft[image], (goon2Cords[0], goon2Cords[1]))
        surface.blit(goonMovingUp[image], (goon3Cords[0], goon3Cords[1]))
        surface.blit(goonMovingRight[image], (goon4Cords[0], goon4Cords[1]))

        #moves the goons towards the player 
        movingCounter += 2
        goon1Cords[1] += 1.0
        goon2Cords[0] -= 1.0
        goon3Cords[1] -= 1.0
        goon4Cords[0] += 1.0

        clock.tick(60)
        pygame.display.update()

#Displays the victory or the defeat screen
def endScreen(screen, screenText, points, surface, defeat):
    x = 0
    surface.fill((15,15,15))
    font3 = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 60)
    pointsText = font3.render(str(points), True, GREEN, None)
    
    for seconds in range(0, 300):
        
        surface.blit(screen, (0,0))

        #Flashes text
        x += 1
        if x == 61:
            x = 0
            
        if x < 31:
            surface.blit(screenText, (0,0))

        #Blits the points, arcade machine and updates the screen
        if defeat == True:
            surface.blit(pointsText, (410, 250))
            
        else:
            surface.blit(pointsText, (350, 500))
        
        surface.blit(arcadeMachine, (0,0))
        pygame.display.update()

def getEnemyVariables(wave):
    enemyHealth = (wave ** 1.02)
            
    #randomize positions of the enemy's spawn
    patern = random.randint(1,3)

    #Anywhere along the left side of the screen
    if patern == 1:
        enemyX = random.randint(0, 100)
        enemyY = random.randint(0, 600)

    #Anywhere along the right side of the screen
    elif patern == 2:
        enemyX = random.randint(700, 800)
        enemyY = random.randint(0, 600)

    #Anywhere along the bottom of the screen
    elif patern == 3:
        enemyX = random.randint(0, 800)
        enemyY = random.randint(600, 700)

    return [enemyHealth, enemyX, enemyY]


#Defines a start screen function which swaps between two images and ends once the uder presses a key
def startScreen(surface):
    starting = True
    counter = 0
    while starting == True:
        if counter == 50:
            counter = 0
            
        #Img 1
        if counter < 25:
            surface.blit(startScreen1, (0,0))

        #Img 2
        else:
            surface.blit(startScreen2, (0,0))

        #Checks if user pressed a key or exited the game 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #User pressed a key
            if event.type == KEYDOWN:
                starting = False

        surface.blit(arcadeMachine, (0,0))
        counter += 1
        pygame.display.update()
        clock.tick(60)
        
def runGame(dylanInput):
    global mapnum, running, wave, boss, loss, wavenum, score, wavetime, healthpacks, enemies

    #Resets Variables 
    mapnum = 0
    running = True
    wave = True
    boss = False
    loss = False
    wavenum = 0
    score = 0
    wavetime = 0
    enemyCounter = 0
    healthpacks = []
    enemies =[] 

    #TEXT THINGS
    font = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf',32)
    font2 = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 46)
    #CREATES THE CHARACTER
    surface = pygame.display.set_mode((800,600))
    surface.fill((200,100,200))
    me = Character(100, 100, 100, 100, 'Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_Sprite.png', 4, playerMovingUp, playerMovingDown, playerMovingLeft, playerMovingRight, playerPunchUp, playerPunchDown, playerPunchLeft, playerPunchRight, surface)

    #Start screen & start music
    gameMusic.play(-1)
    startScreen(surface)
    
    #Display controlles
    displayPrompt(surface)
    
    while running == True and dylanInput == True:
        #Increments the wavenumber inbetween waves
        wavenum += 1
        enemyCounter = wavenum
        waveText = font.render('Wave: ' + str(wavenum), True, RED, None)

        wave = True

        #Midwave
        while wave == True and wavenum != 8 and dylanInput == True:
            #Updates and blits text
            scoreText = font.render('Score: ' + str(score), True, RED, None)
            surface.blit(waveText, (300,20))
            surface.blit(scoreText, (475,20))
            
            pygame.display.update()

            #Updates map/player/hearts
            updateMap(mapnum, surface)
            drawEntity(me, surface)
            drawHearts(me.health, surface)

            #Blits enemies and their healthbar
            for x in range(len(enemies)):
                enemies[x].moveToPlayer(me)
                drawEntity(enemies[x], surface)
                drawHealthbar(enemies[x], surface)

            #HEALTHPACKS
                
            amountOfHealthpacks = len(healthpacks)
            counter = 0
            while counter < amountOfHealthpacks:
                #BLITS HEALTHPACKS
                drawEntity(healthpacks[counter], surface)

                #CHECKS IF HEALTHPACK IS PICKED UP
                pickedUp = checkCollision(healthpacks[counter], me)

                #IF HEALTHPACK IS PICKEDUP HEAL PLAYER AND POP HEALTHPACK FROM HEALTHPACKS
                if pickedUp == True and me.health < 6:
                    healthpacks.pop(counter)
                    counter -= 1
                    amountOfHealthpacks -= 1
                    me.health += 1
                    healSound.play()
                    
                counter += 1

            #Blit arcademachine over all images on the screen
            surface.blit(arcadeMachine, (0,0))

            #If user clicked x on the window everything closes
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wave = False
                    running = False
                    loss = False
                    pygame.quit()

                #Gets userinput for movement
                me.getMovement(event)

                #Checks if the user punched
                if me.punch != (0, 0, 0, 0):
                    #checks if enemies collided with punch
                    hitEnemies(me)

                    #Moves collided enemies back
                    moveEnemiesBack(me)

                    #Updates score if enemies were killed
                    score = killEnemies(score, surface)

                    #Resets punch
                    me.punch = (0 ,0, 0, 0)

            #Moves the player
            me.move()

            #Checks if player collided with enemies if he is not invincible 
            if me.IEFrames == 0:
                for x in range(len(enemies)):
                    collided = checkCollision(me, enemies[x])
                    if collided == True:
                        playerHurtSound.play()
                        #Makes player faster momentarally if he is hurt in order to allow repositioning
                        me.health -= 1
                        me.IEFrames = 120
                        me.vel = 10
                        break

            #Gradually removes speed and invincibility
            else:
                me.IEFrames -= 1
                me.vel -= (7 / 120)
                
            wavetime += 1

            #Spawn an enemy evey 2 seconds
            if wavetime % 120 == 0 and enemyCounter - 1 >= 0 and me.health > 0:
                #Randomizes enemy's positions and derives their health based on the wavenumber 
                enemyVariables = getEnemyVariables(wavenum)

                #creates goon and appends it to the list
                enemy = Goon(enemyVariables[1], enemyVariables[2], 100, 100, 'Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_Sprite.png', 1.5, goonMovingUp, goonMovingDown, goonMovingLeft, goonMovingRight, enemyVariables[0], surface)
                enemies.append(enemy)
                enemyCounter -=1

            #If all enemies have been defeated you move on to the next round
            elif enemies == [] and wavetime > 120 and enemyCounter == 0:
                wave = False
                wavetime = 0

            #if you areo ut of health end the game
            if me.health <= 0:
                wave = False
                running = False
                loss = True
            
            clock.tick(60)

        #initializes variables to be used in the boss' fight
        if wavenum == 8:
            cutScene(me, surface)
            boss = True
            bullets = []
            shootingInterval = 60
            flameCounter = 0
            #creates boss
            bossman = FightingBoss(bossShooting, bossMovingLeft, surface)
            me.vel = 4
            
        #Boss round loop
        while boss == True and dylanInput == True:

            #Updates and displays text
            scoreText = font.render('Score: ' + str(score), True, RED, None)
            mapnum = 1
            surface.blit(waveText, (300,20))
            surface.blit(scoreText, (475,20))
            pygame.display.update()

            #blits map
            updateMap(mapnum, surface)
            
            #blits animated wall of flame
            if flameCounter >= 60:
                flameCounter = 0

            if flameCounter > 30:
                surface.blit(flameWall, (0,0))

            else:
                surface.blit(flameWall2, (0,0))
            flameCounter += 1

            #Draws player, boss, boss' healthbar and player's hearts
            drawEntity(me, surface)
            drawEntity(bossman, surface)
            drawHealthbar(bossman, surface)
            drawHearts(me.health, surface)

            #BULLETS

            
            if bullets != []:
                counter = 0
                bulletNum = len(bullets)
                while counter < bulletNum:
                    #Moves bullets
                    bullets[counter].fly()

                    #Checks if bullets were punched by the player 
                    score = bullets[counter].checkIfPunched(me.punch, me.orientation, score)

                    #Checks if player collided with bullets
                    playerWasShot = checkCollision(me, bullets[counter])

                    #If player is not invincible 
                    if me.IEFrames == 0:

                        #And if player was shot, take a heart away from the player and make him invincible
                        if playerWasShot == True:
                            playerHurtSound.play()
                            me.health -= 1
                            me.IEFrames = 30
                            
                    #If player is invincible, take away a frame of invincible
                    else:
                        me.IEFrames -=1

                    #Checks if the boss was shot
                    bossWasShot = checkCollision(bossman, bullets[counter])

                    #If the boss is not invincible
                    if bossman.IEFrames == 0:

                        #And if the boss was shot, take health from him and make him invincible for 25 frames
                        if bossWasShot == True:
                            gruntSound.play()
                            bossman.health -= 1
                            bossman.IEFrames = 25

                            #If the boss is down to half health (5) he enters a rage, screaming at the player then shoots faster
                            if bossman.health == 5:
                                #Decreases shooting interval from 60 to 30 frames
                                shootingInterval = 30
                                for x in range(len(bullets)):
                                    drawEntity(bullets[x], surface)

                                surface.blit(angryBossText, (0, 0))
                                
                                pygame.display.update()

                                #Pauses for a second to give the player time to read
                                pygame.time.delay(2500)

                    #Decreases the boss' time invincible           
                    else:
                        bossman.IEFrames -= 1
                        
                    if playerWasShot == True:
                        bullets.pop(counter)
                        counter -= 1
                        bulletNum -= 1

                    if bossWasShot == True:
                        bullets.pop(counter)
                        counter -= 1
                        bulletNum -= 1
                    
                    counter += 1

                #Draws all bullets     
                for x in range(len(bullets)):
                    drawEntity(bullets[x], surface)

                #Removes bullets outside the map
                bullets = removeOutOfMapBullets(bullets)
                
            surface.blit(arcadeMachine, (0,0))
            me.punch = (0 ,0, 0, 0)

            #Gets event
            for event in pygame.event.get():
                #Exits game if user clicked x on the window
                if event.type == pygame.QUIT:
                    wave = False
                    running = False
                    loss = False
                    pygame.quit()

                #gets the players movement
                me.getMovement(event)   

            #moves the player
            me.move()
            
            #prevents player from moving past the wall of flame
            if me.xpos > 440:
                me.xpos = 440

            #moves the boss
            bossman.move()
                
            wavetime += 1

            #Spawn a bullet during every set interval
            if wavetime % shootingInterval == 0 and me.health > 0:
                gunShotSound.play()
                shot = Bullet(bossman.xpos, bossman.ypos + 15, 3, bulletUpAnimation, bulletDownAnimation, bulletLeftAnimation, bulletRightAnimation, surface)
                bullets.append(shot)
                bossman.attackTimer = 10
                
            else:
                if bossman.attackTimer > 0:
                    bossman.attackTimer -= 1

            #If boss is dead, end the game
            if bossman.health <= 0:
                wave = False
                boss = False
                running = False

            #IF the player is dead, end the game
            if me.health <= 0:
                wave = False
                boss = False
                running = False
                loss = True
            
            clock.tick(60)

    #Player dies before round 7
    if loss == True and wavenum < 7:
        endScreen(lossScreen, lossScreenText, score, surface, loss)
        gameMusic.stop()
        insert_score('ShadowBoxing', score)
        dylanInput = False
        return False

    #player dies on round 7
    elif loss == True and wavenum == 7:
        endScreen(lossScreen, lossScreenText, score, surface, loss)
        gameMusic.stop()
        insert_score('ShadowBoxing', score)
        dylanInput = False
        return True

    #Player dies on boss round
    elif loss == True and wavenum == 8:
        endScreen(lossScreen, lossScreenText, score, surface, loss)
        gameMusic.stop()
        insert_score('ShadowBoxing', score)
        dylanInput = False
        return True

    #Player kills the boss
    elif loss == False:
        endScreen(winScreen, winScreenText, score, surface, loss)
        gameMusic.stop()
        insert_score('ShadowBoxing', score)
        dylanInput = False
        return True

loss = False

#Creates color variables
RED = (255,51,21)
BLACK = (0,0,0)
GREEN = (51, 255, 21)

    
#SOUNDS
gameMusic = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_ShadowBoxing_MenuMusic.ogg')
healSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_ShadowBoxing_Heal.ogg')
playerHurtSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_ShadowBoxing_PlayerHurt.ogg')
gunShotSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_ShadowBoxing_Gunshot.ogg')
gruntSound = pygame.mixer.Sound('Prism_assets/Prism_sounds/Prism_ShadowBoxing_Grunt.ogg')
gameMusic.set_volume(0.2)
playerHurtSound.set_volume(0.075)
gunShotSound.set_volume(0.05)

#MAP
image = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_Map.jpg')
image = pygame.transform.scale(image, (1600,600))
arcadeMachine = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_ShdwBoxBG.png')
flameWall = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_ShdwBox_wallOfFlame.png')
flameWall2 = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_ShdwBox_wallOfFlame2.png')

#HEART ICONS
fullHeart = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_Heart1.png')
fullHeart = pygame.transform.scale(fullHeart, (50, 50))
halfHeart = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_Heart2.png')
halfHeart = pygame.transform.scale(halfHeart, (50, 50))
emptyHeart = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_Heart3.png')
emptyHeart = pygame.transform.scale(emptyHeart, (50, 50))
healthpackHalfHeart1 = pygame.transform.scale(halfHeart, (20,20))
healthpackHalfHeart2 = pygame.transform.scale(halfHeart, (23,23))
healthpackAnimation =  [healthpackHalfHeart1, healthpackHalfHeart2]

#PLAYER MOVING ANIMATIONS
playerMovingRight = [ (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MR1.png')), (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MR2.png')) ]
playerMovingLeft = [ (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_ML1.png')), (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_ML2.png')) ]
playerMovingDown = [ (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MD1.png')), (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MD2.png')) ]
playerMovingUp = [ (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MU1.png')), (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MU2.png')) ]
movingAnimations = [playerMovingRight, playerMovingLeft, playerMovingDown, playerMovingUp]

#PLAYER PUNCHING ANIMATIONS
playerPunchUp = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MUP.png')
playerPunchUp = pygame.transform.scale(playerPunchUp, (100, 100))
playerPunchRight =  pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MRP.png')
playerPunchRight = pygame.transform.scale(playerPunchRight, (100, 100))
playerPunchDown =  pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MDP.png')
playerPunchDown = pygame.transform.scale(playerPunchDown, (100, 100))
playerPunchLeft =  pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_MLP.png')
playerPunchLeft = pygame.transform.scale(playerPunchLeft, (100, 100))

#Scale all the animation images properly
for counter in movingAnimations:
    for y in range(len(counter)):
        counter[y] = pygame.transform.scale(counter[y], (100, 100))

#GOON MOVING ANIMATIONS
goonMovingRight = [ (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_GoonR1.png')), (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_GoonR2.png')) ]
goonMovingLeft = [ (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_GoonL1.png')), (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_GoonL2.png')) ]
goonMovingDown = [ (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_GoonD1.png')), (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_GoonD2.png')) ]
goonMovingUp = [ (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_GoonU1.png')), (pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_GoonU2.png')) ]
goonMovingAnimations = [goonMovingRight, goonMovingLeft, goonMovingDown, goonMovingUp]

#Scale all the animation images for the goons properly
for counter in goonMovingAnimations:
    for y in range(len(counter)):
        counter[y] = pygame.transform.scale(counter[y], (100, 100))

#BOSS SHOOTING
bossShooting = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_BLP.png')
bossShooting = pygame.transform.scale(bossShooting, (100, 100))

#BOSS MOVING 
bossMovingLeft = [ pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_BL1.png') , pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_BL2.png') ]
bossMovingLeft[0] = pygame.transform.scale(bossMovingLeft[0], (100, 100))
bossMovingLeft[1] = pygame.transform.scale(bossMovingLeft[1], (100, 100))

#BULLET ASSETS
bulletUp = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_BulletUp.png')
bulletUp = pygame.transform.scale(bulletUp, (40,40))
bulletUpAnimation = [bulletUp, bulletUp]
bulletRight = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_BulletRight.png')
bulletRight = pygame.transform.scale(bulletRight, (40,40))
bulletRightAnimation = [bulletRight, bulletRight]
bulletDown = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_BulletDown.png')
bulletDown = pygame.transform.scale(bulletDown, (40,40))
bulletDownAnimation = [bulletDown, bulletDown]    
bulletLeft = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_BulletLeft.png')
bulletLeft = pygame.transform.scale(bulletLeft, (40,40))
bulletLeftAnimation = [bulletLeft, bulletLeft]
bulletAnimations = [bulletUpAnimation, bulletRightAnimation, bulletDownAnimation, bulletLeftAnimation]
        
#SECOND PHASE BOSS MINI-CUTSCENE TEXT
angryBossText =  pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_ShdwBox_cutSceneText2.png')

#VICTORY/DEFEAT SCREEN ASSETS
winScreen = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_WinScreen.jpg')
winScreenText = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_WinScreenText.png')
lossScreen = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_LoseScreen.jpg')
lossScreenText = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_LoseScreenText.png')

#START SCREEN
startScreen1 = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_StartScreen.png')
startScreen2 = pygame.image.load('Prism_assets/Prism_img/Prism_ShadowBoxing/Prism_SdwBox_StartScreen2.png')

#VARIABLES TO HOLD THE ENEMIES AND HEALTHPACK OBJECTS
enemies = []
healthpacks = []

#INITIALIZES THE CLOCK
clock = pygame.time.Clock()

#Variables
mapnum = 0
running = False
wave = False
boss = False
loss = False
wavenum = 0
score = 0
wavetime = 0