import sqlite3 #Import the sqlite3 module

conn = sqlite3.connect('Prism_database.db') #Connect to the Prism database

c = conn.cursor() #Create a cursor from the connection object

#Create the databases if they do not exist

c.execute('''CREATE TABLE IF NOT EXISTS `HighScores` (
    `Game` TEXT NOT NULL UNIQUE,
    `Score` INTEGER  NOT NULL
); ''')

c.execute('''CREATE TABLE IF NOT EXISTS `Settings` (
    `Name` TEXT NOT NULL UNIQUE,
    `Option` INTEGER NOT NULL
); ''')

c.execute('''CREATE TABLE IF NOT EXISTS `SaveGame` (
    `Name` TEXT NOT NULL UNIQUE,
    `Value1` INTEGER NOT NULL,
    `Value2` INTEGER NOT NULL
); ''')

c.execute('''CREATE TABLE IF NOT EXISTS `User` (
    `Name` TEXT NOT NULL UNIQUE,
    `UserName` TEXT NOT NULL,
    `Value` INTEGER NOT NULL
); ''')


#Function to insert the highscores into the database
def insert_score(game, score):
    score_row = c.execute("SELECT Score from HighScores where Game=(?)", [game]).fetchone()
    if not score_row or score > score_row[0]: #If score is greater than the one in the db
        c.execute("REPLACE INTO HighScores VALUES (?, ?)", [game, score])
    else:
        x = 5 #Testing purposes
    conn.commit() #Commit the changes to the database


#Function to get the score of the games
def get_score(game):
    score_row = c.execute("SELECT Score from HighScores where Game=(?)", [game]).fetchone()
    conn.commit()
    return score_row[0] #Return the score
    

#Function to change the saved setting of the game
def change_setting(s_type, val): #Type of setting, #Value
    #Change the associated values
    if s_type == 'KM': 
        s_type = 'ShowKM'
    elif s_type == 'SB':
        s_type = 'ShowSHDW'
    elif s_type == 'LP':
        s_type = 'ShowLP'
    elif s_type == 'SITD':
        s_type = 'ShowSITD'
    else:
        pass
    c.execute("REPLACE INTO Settings VALUES (?, ?)", [s_type, val]) #Execute SQL 
    conn.commit() #Commit changes to database

#Function to get the saved setting values
def get_setting(s_name_type): 
    #Change the associated values
    if s_name_type == 'KM':
        s_name_type = 'ShowKM'
    elif s_name_type == 'SB':
        s_name_type = 'ShowSHDW'
    elif s_name_type == 'LP':
        s_name_type = 'ShowLP'
    elif s_name_type == 'SITD':
        s_name_type = 'ShowSITD'
    else:
        pass
    s_name_type = c.execute("SELECT Option from Settings where Name=(?)", [s_name_type]).fetchone() #Execute SQL
    if not s_name_type:
        return 0 #Return 0 if false
    return s_name_type[0] #Return the value

#Function to display text
def display_text(game):
    game_text = c.execute("SELECT Option from Settings where Name=(?)", [game]).fetchone()
    if not game_text:
        return 0 
    return game_text[0] #Return the value
    conn.commit() #Commit changes to the database

#Function to save coordinates when the user exits the game
def save_coords(x, y):
    name = 'coords'  
    c.execute("REPLACE INTO SaveGame VALUES (?,?,?)", [name, x, y]) #Execute SQL
    conn.commit() #Commit changes to the database

#Function to get the coordinates from the last save
def get_coords():
    c_coords = []
    s_coord_x = c.execute("SELECT Value1 from SaveGame where Name='coords'").fetchone() #Execute SQL
    s_coord_y = c.execute("SELECT Value2 from SaveGame where Name='coords'").fetchone()
    c_coords.append(s_coord_x[0])
    c_coords.append(s_coord_y[0])
    return c_coords #Return the list

#Function to save the keys    
def save_key(game, key_num, has_key): # Save the keys from the game
    s_key_name = c.execute("SELECT Name from SaveGame where Name=(?)", [game]).fetchone() # KEY NAME
    s_key_num = c.execute("SELECT Value1 from SaveGame where Name=(?)", [game]).fetchone() # HAS KEY
    s_key_has = c.execute("SELECT Value2 from SaveGame where Name=(?)", [game]).fetchone() # # BEATEN GAME 

    c.execute("REPLACE INTO SaveGame VALUES (?,?,?)", [game, key_num, has_key]) #Execute SQL
    conn.commit() #Commit changes to the database

#Function to get the values from the keys in the database
def get_key(game): 
    s = [] #Create an empty list
    s_key_num = c.execute("SELECT Value1 from SaveGame where Name=(?)", [game]).fetchone() #Has Key
    s_key_has = c.execute("SELECT Value2 from SaveGame where Name=(?)", [game]).fetchone() #Beaten game

    s.append(s_key_num[0])
    s.append(s_key_has[0])
    return s #Return the list

#Function to save the username/name of the user to the database
def save_username(u_name, val):
    name = 'User1'
    c.execute("REPLACE INTO User VALUES (?,?,?)", [name, u_name, val]) #EXecute SQL
    conn.commit() #Commit changes to the database

#Function to get the username from the database
def get_username_sql():
    user1 = c.execute("SELECT UserName from User where Name='User1'").fetchone() #EXecute SQL
    return user1[0]#Return the value
#Set the username/name function in the database
def username_set():
    user = c.execute("SELECT Value from User where Name='User1'").fetchone() #EXecute SQL
    if not user:
        return 0
    return user[0] #Return value

#Function to reset the scores of the game
def reset_scores():
    games = ['KeyMatcher', 'ShadowBoxing', 'LightPong', 'ShotInTheDark'] #Create a list with all the games
    for game in games:
        c.execute("REPLACE INTO HighScores VALUES (?, ?)", [game, 0]) #Execute SQL
    conn.commit() #Commit changes to the database

#Function to reset the whole game 
def reset_game():
    coord = 'coords'
    coordinates = (-400,-300) #Default coordinates
    games = ['KeyMatcher', 'ShadowBoxing', 'LightPong', 'ShotInTheDark'] #List for games
    save_game = ['key_LP', 'key_MSTR', 'key_SB', 'key_SITD', 'key_KM'] #List for keys
    settings = ['ShowKM', 'ShowSITD', 'ShowSHDW', 'ShowLP', 'Sounds', 'Music', 'cutscene'] #List for SaveGame
    user_setting = ['user'] #Default value for the username
    name = 'User1'

    #Loop through games,settings,user and replace all the values to the default settings

    for game in games:
        c.execute("REPLACE INTO HighScores VALUES (?, ?)", [game, 0])
    
    for save in save_game:
        c.execute("REPLACE INTO SaveGame VALUES (?, ?, ?)", [save, 0, 0])
    
    for sett in settings:
        c.execute("REPLACE INTO Settings VALUES (?, ?)", [sett, 0])
    
    for u in user_setting:
        c.execute("REPLACE INTO User VALUES (?,?,?)", [name, u, 0])

    c.execute("REPLACE INTO SaveGame VALUES (?, ?, ?)", [coord, coordinates[0], coordinates[1]])

    conn.commit() #Commit the changes 
    return False #Return False
