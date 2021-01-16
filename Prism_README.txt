******************************************************************************
						  
                ██████╗ ██████╗ ██╗███████╗███╗   ███╗
                ██╔══██╗██╔══██╗██║██╔════╝████╗ ████║
                ██████╔╝██████╔╝██║███████╗██╔████╔██║
                ██╔═══╝ ██╔══██╗██║╚════██║██║╚██╔╝██║
                ██║     ██║  ██║██║███████║██║ ╚═╝ ██║
                ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝
                           LET THE LIGHT IN.
                           
******************************************************************************

Author -  Adam Grabowski, Alden DeMello, Maged Armanios, Sebastian Deluca

******************************************************************************

Class / Section - ICS4U1

******************************************************************************

Date - 04/14/2020

******************************************************************************

Version - V 1.0

*****************************************************************************

Unit / Question # - Unit 2: Software Development

******************************************************************************

Programming Language - Python 3.7.x

******************************************************************************

Problem Description – Create an original video game using Pygame and Python in
a student-managed project. The game needs to be made with direct relation to
the theme of the project. The theme selected was Light and Darkness. We must 
also simulate the software development process effectively, through all its 
stages.

******************************************************************************

Program Assumptions - For this program to run the user can use a choice of
		      Windows or MacOS running Python 3.x.x or higher.

******************************************************************************

Features of Program

INTRODCUTION:

    - There is a loading screen which simulates many popular games 
    introductions. 

    - The user is prompted to save a username.  

MAIN MENU: 

    - On the main menu screen, there is a help menu to provide more detail 
    about the game. 

    - Also present is a stats page which displays real-time and saved 
    highscores as well as finding easter eggs it even has the ability to 
    reset your stats. 

    - Lastly, an options page which allows the user to have saved 
    options for music and sounds while also being able to reset the whole 
    game. 

    - Music and Button Sounds are also present.

------------------------------------------------------------------------------

ARCADE:

 - Added Ambience:
    Though a one in 10,000 chance, occasionally, the user will hear the sound
    of thunder, which will consequently short out the lights in the arcade
    temporarily and the only light will be from the lightning nearby. This 
    serves the purpose of more fully immersing the user into Prism's world.

- 'Original' Music:
    The arcade, and all subsequent games, feature either original music or
    music created from samples found on the Internet.

- Original SFX:
    All sound effects, minus the Thunder sound effect, are unique to Prism--
    as they were created for the game by the sound designer.

- 2.5D Perspective / Dynamic Visibility:
    Prism adopts a unique camera-angle in-game with a 2.5D Perspective, rather
    than a Simple  2D. In-turn, Dylan's visibility typically responds to how
    he would be visible in a real-life perspective. He will occasionally go
    under walls to adhere to this approach for the map.
    
- Dynamic Map:
    The further you progress in Prism's story, the more the map changes.
    More lights turn on, doors open, etc.
    
- Cutscenes:
    Prism utilizes for loops and pygame's syntax to create cutscenes to begin
    and end Prism's story.

- Collision:
    Due to Prism's unique perspective-- we had to manually code in collision 
    for every area of the map.

- Exception Handling:
    Prism uses lists, and such, we check the lists. This requires exception 
    Handling because lists are prone to crashing programs.

- Game Saving / Settings Saving:
    Prism utilizes databases to dynamically save the player's progress in the 
    story as well as their settings preference. For example, if the user turns 
    off Music, that setting will be saved.

- Keys:
    A unique vessel to further the story-- Dylan collects the keys to turn on 
    the arcade machines. This makes sure that the player plays the games in a 
    specific order, as each game corresponds to a specific area of the Map
     lighting up again.

------------------------------------------------------------------------------

KEYMATCHER:
- Starting Screen:
    After activating the Arcade Machine, the starting screen gives the user a
    chance to prepare for the game ahead. 

- How-To-Play Screen:
    This screen follows the starting screen and shows the controls to the
    user before the game starts.


------------------------------------------------------------------------------

SHADOWBOXING:
- 2.5D perspective

- Start screen, an anmimated prompt, and a cutscene

- Increasing difficulty:
    As the player progresses trough the game, the enemies become harder to 
    attack

- Includes basic enemies and a boss battle:
    Boss battle occurs at wave 8, the final wave

- Multiple Maps
    Map changes once the boss battle begins 

- Unique sound effects:
    sound effects trigger upon...
        Taking damage
        Picking up a healthpack 
        Hitting the boss

- Randomized enemy spawn positions

- Randomly generated healthpack drops 

- Can Attack in 8 Directions 
    Bullets shot by the boss can also be redirected in all 8 directions 

------------------------------------------------------------------------------

LIGHT PONG:
- Starting Screen:
    After activating the Arcade Machine, the starting screen gives the user a
    chance to prepare for the game ahead. 

- Continue Playing Option:
    After a Light Pong Match finishes, the game prompts the user to either
    continue playing, or return to the Arcade.

- Dynamic Movespeed:
    The NPC you play against has the ability to travel at a speed that is in
    a range between 2.0 and 4.0, to add difficulty to the game.
------------------------------------------------------------------------------
SHOT IN THE DARK:

- Unique start screen in an arcade style

- 2D perspective

- Special effect that makes the character seem like he/she is falling.

- Collision detection on both sides of the machine and platforms rising
toward the player

- Point increasing system where the user collects tokens

- Color shifting functionallity where the user can press space to swap
colors from white to black. 

- The game progresses when the user lands on a platform that matches
the color of the user's current character sprite.

- a swift animation plays that switches the user's color to black or white
upon pressing the space key.

- If the user connects with a platform with a different color than the 
user's sprite color, it would be considered a game over. 

- The objective of the game is to get as many tokens as possible. Once the
user achieves 25 tokens, the rest of Prism can be played! This is the
minimum requirement for the score to be able to move on. 

- "original" music is being played throughout the game. Alongside such,
sound effects are played every time a token is picked up. 

- Tokens change color based on the user's color.

- A gray bar constantly loops on the screen, moving upward despite the user
stopping on platforms. If the user passes through the middle of this gray
bar, the user automatically switches colors from the opposite one it is 
currently held at. If the user is on a platform at the time the gray bar
passes, the user will die due to the color change, so the user is 
encouraged to move quick and think fast during these situations.


******************************************************************************

Restrictions – The entire game must be held within a 10 mb zip file.

******************************************************************************

~~ Known Errors ~~

SHOT IN THE DARK

- Known bug that allows the user to phase through platforms occasionally if 
the user presses space right before landing on a platform. 
- Occasionally, Tokens do not spawn on a platform (which is intended at first)
however upon landing on said platform, the point counter still goes up one.

ARCADE

- 

******************************************************************************

Implementation Details / How to build the program - For the user to run
                                                    the program they must
    1. have Python 3.x.x installed or they can find it here
        (https://www.python.org/downloads/)

    2. Go to Python's File Location (Appdata/Local/Programs/python/)

    3. Right-click, and open a Windows Powershell.

    4. Type in: 'pip3 install pygame'

    5. After being installed the user must open Python IDLE.

    6. After that the user must go to File > Open > (select Prism_main.py )
        to open.

    7. Then the user must Hit f5 on their keyboard or Run > Run Module.

******************************************************************************

~~ Additional Files ~~

Prism_Arcade.py
Prism_Characters.py
Prism_database.db
Prism_KeyMatch.py
Prism_LightPong.py
Prism_main.py
Prism_Resources.py
Prism_ShadowBoxing.py
Prism_SITD.py
Prism_sql.py
Pixellari.ttf


hitbox.png
Prism_Arcade_DOOR.png
Prism_Arcade_MapBot.png
Prism_Arcade_MapBot2.png
Prism_Arcade_MapBot3.png
Prism_Arcade_MapBot4.png
Prism_Arcade_MapBot5.png
Prism_Arcade_MapBot6.png
Prism_Arcade_MapLightning.png
Prism_Arcade_MapLightning_NO.png
Prism_Arcade_MapLit.png
Prism_Arcade_MapTop.png
Prism_Arcade_MapTop2.png
Prism_Arcade_MapTop3.png
Prism_Arcade_MapTop4.png
Prism_Arcade_MapTop5.png
Prism_BG.png

Prism_CS_AH.png
Prism_CS_ANYONE.png
Prism_CS_BG.png
Prism_CS_DylSCREAM.png
Prism_CS_Eyes.jpg
Prism_CS_LookUpDyl.png
Prism_CS_Mom.png
Prism_CS_whatgoing.png
Prism_CS_where.png

Prism_CS2_1.jpg
Prism_CS2_2.jpg
Prism_CS2_2Text.png
Prism_CS2_2Text2.png
Prism_CS2_ThankYou.jpg

Prism_callForMom.png
Prism_callForSomeone.png
Prism_confused.png
Prism_DONTneedKey.png
Prism_DylanIdle.png
Prism_DylanIdleBack.png
Prism_DylanIdleSideR.png
Prism_DylanWalkBack1.png
Prism_DylanWalkBack2.png
Prism_DylanWalkF1.png
Prism_DylanWalkF2.png
Prism_DylanWalkSideR1.png
Prism_DylanWalkSideR2.png
Prism_FoundFrontKey.png
Prism_FoundKey.png
Prism_LightsOn.png
Prism_LoseGame.png
Prism_needFrontKey.png
Prism_needKey.png
Prism_sigh.png
Prism_turnedOff.png
Prism_TurnedOnTheLights.png

Prism_KeyMatcherBG.png
Prism_KeyMatcherkeyBG.jpg
Prism_KeyMatcher_GO.jpg
Prism_KeyMatcher_HowToPlay.jpg
Prism_KeyMatcher_LoseScreen.jpg
Prism_KeyMatcher_StartScreen.jpg
Prism_KeyMatcher_StartScreen1.jpg
Prism_KeyMatcher_WAIT.jpg
Prism_NewKeymatch_GetReady.png

Prism_LightPongBG.png
Prism_LightPong_Ball1.png
Prism_LightPong_Ball2.png
Prism_LightPong_Ball3.png
Prism_LightPong_BallHit1.png
Prism_LightPong_BallHit2.png
Prism_LP_Begin.png
Prism_LP_BG.jpg
Prism_LP_Continue.png
Prism_LP_LeftChar.png
Prism_LP_RightChar.png
Prism_LP_Start.jpg
Prism_LP_Table.png
Prism_LP_YN.png
Prism_LP_YouLose.png
Prism_LP_YouWin.png
Prism_SITD_BG.png

Prism_BG.jpg
Prism_FooLogo.png
Prism_HelpBG.png
Prism_HelpBG2.png
Prism_Logo.png
Prism_Logo2.png
Prism_Main_Credit.jpg
Prism_Main_Username.jpg
Prism_menu_button.png
Prism_menu_hover.png
Prism_Options.png
Prism_PygamePowered.png
Prism_Quit.png

Prism_SdwBox_BL1.png
Prism_SdwBox_BL2.png
Prism_SdwBox_BLP.png
Prism_SdwBox_BulletDown.png
Prism_SdwBox_BulletLeft.png
Prism_SdwBox_BulletRight.png
Prism_SdwBox_BulletUp.png
Prism_SdwBox_GoonD1.png
Prism_SdwBox_GoonD2.png
Prism_SdwBox_GoonL1.png
Prism_SdwBox_GoonL2.png
Prism_SdwBox_GoonR1.png
Prism_SdwBox_GoonR2.png
Prism_SdwBox_GoonU1.png
Prism_SdwBox_GoonU2.png
Prism_SdwBox_Heart1.png
Prism_SdwBox_Heart2.png
Prism_SdwBox_Heart3.png
Prism_SdwBox_LoseScreen.jpg
Prism_SdwBox_LoseScreenText.png
Prism_SdwBox_Map.jpg
Prism_SdwBox_MD1.png
Prism_SdwBox_MD2.png
Prism_SdwBox_MDP.png
Prism_SdwBox_ML1.png
Prism_SdwBox_ML2.png
Prism_SdwBox_MLP.png
Prism_SdwBox_MR1.png
Prism_SdwBox_MR2.png
Prism_SdwBox_MRP.png
Prism_SdwBox_MU1.png
Prism_SdwBox_MU2.png
Prism_SdwBox_MUP.png
Prism_SdwBox_SHADOWMAN.png
Prism_SdwBox_Sprite.png
Prism_SdwBox_StartScreen.png
Prism_SdwBox_StartScreen2.png
Prism_SdwBox_WinScreen.jpg
Prism_SdwBox_WinScreenText.png
Prism_ShdwBoxBG.png
Prism_ShdwBox_cutSceneText.png
Prism_ShdwBox_cutSceneText2.png
Prism_ShdwBox_Prompt1.png
Prism_ShdwBox_Prompt2.png
Prism_ShdwBox_wallOfFlame.png
Prism_ShdwBox_wallOfFlame2.png

Prism_SITD_BG.png
Prism_SITD_DarkChar.png
Prism_SITD_Overlay.png
Prism_SITD_StartScreen.jpg
Prism_SITD_StartScreenText.png
Prism_SITD_TokenBlack.png
Prism_SITD_TokenWhite.png
Prism_SITD_TransChar1.png
Prism_SITD_TransChar2.png
Prism_SITD_TransChar3.png
Prism_SITD_WhiteChar.png

Prism_SITD.png
Prism_Stats.jpg
Prism_STATS_KM.png
Prism_STATS_LP.png
Prism_STATS_SB.png

Prism_button.wav
Prism_ArcadeMusic.ogg
Prism_KeyMatcher_correctKeySound.wav
Prism_KeyMatcher_inGame.ogg
Prism_KeyMatcher_loseSound.wav
Prism_KeyMatcher_MainMusic.ogg
Prism_LP_GameMusic.ogg
Prism_LP_HitBall.ogg
Prism_MenuMusic.ogg
Prism_Pickup.wav
Prism_Reunited.ogg
Prism_ShadowBoxing_Grunt.ogg
Prism_ShadowBoxing_Gunshot.ogg
Prism_ShadowBoxing_Heal.ogg
Prism_ShadowBoxing_MenuMusic (1).ogg
Prism_ShadowBoxing_MenuMusic.ogg
Prism_ShadowBoxing_PlayerHurt.ogg
Prism_SITD_GameMusic.ogg
Prism_Speak.wav
Prism_Thunder.ogg
Prism_Reset.png

Prism_Restart.png




******************************************************************************