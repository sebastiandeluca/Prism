import pygame
from pygame.locals import *
import pygame.locals as pl
import random
import os
pygame.font.init()
#COLOURS
WHITE = (255,255,255)
BLACK = (0,0,0)
CYAN = (8,163,255)
YELLOW =(208,232,7)
RED = (255,51,21)
BLUE = (12,67,235)
GREEN = (105,255,8)

#Creates a class for clickable buttons
class Button():
    def __init__(self, x_coord, y_coord, text, text_colour, x_size, y_size, screen):
        self.x_coord = x_coord # X-coordinate of button
        self.y_coord = y_coord # Y-coordinate of button
        self.text = text #Text to display
        self.text_colour = text_colour # Text colour
        self.x_size = x_size # X-size of the button
        self.y_size = y_size # Y-size of the button
        self.img = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_menu_button.png') #Load image 
        self.img2 = pygame.image.load('Prism_assets/Prism_img/Prism_Main_Menu/Prism_menu_hover.png') #Load Image
        self.screen = screen
        self.img = pygame.transform.scale(self.img, (x_size, y_size))
        self.img2 = pygame.transform.scale(self.img2, (x_size, y_size))

    def draw(self): #Draw function
        mouse = pygame.mouse.get_pos() #Get mouse position
        self.screen.blit(self.img,(self.x_coord,self.y_coord)) #Display image to the screen at x,y coords
        
        #Event check for hover
        if (self.x_coord+self.x_size) > mouse[0] > self.x_coord and (self.y_coord+self.y_size) > mouse[1] > self.y_coord:
            
            self.btn = self.screen.blit(self.img2,(self.x_coord,self.y_coord))
            
        else:
            self.btn = self.screen.blit(self.img,(self.x_coord,self.y_coord))
        

        #Font setup to print
        btnText = pygame.font.Font("Prism_assets/Prism_font/Pixellari.ttf", 20)
        textSurf, textRect = self.textObjects(self.text, btnText)
        textRect.center = ((self.x_coord+(self.x_size/2)), (self.y_coord+(self.y_size/2)) )
        self.screen.blit(textSurf, textRect)

    #Text objects function
    def textObjects(self, text, font):
        textSurface = font.render(self.text, True, self.text_colour)
        return textSurface, textSurface.get_rect()

#Creates the class of the keys used in the arcade
class Key():
    def genKey(self,keyBG,keyMatcher): # Generate the image of the key for the game
        regularFont = pygame.font.Font('Prism_assets/Prism_font/Pixellari.ttf', 32)
        self.x = 400 - 32
        self.y = 300 - 32
        self.key = chr(random.randint(97,122))
        self.keyUp = self.key.upper()
        self.letter = regularFont.render(self.keyUp,True,BLACK)
        self.letterRect = self.letter.get_rect()
        self.letterRect.center = (self.x,self.y)
        keyMatcher.blit(keyBG,(self.letterRect.center))
        keyMatcher.blit(self.letter,((self.x+20),(self.y+16)))
        pygame.display.update()
        return self.key

#Creates a function which makes a fade effect in the game
def fade_out(width,height,s):
    fadeS = pygame.Surface((width, height))
    fadeS.fill((0,0,0))
    for alpha in range(0,100):
        fadeS.set_alpha(alpha)
        s.blit(fadeS, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

#Creates a function which makes a fade effect in the game
def fade_in(width,height,s):
    fadeS = pygame.Surface((width, height))
    fadeS.fill((0,0,0))
    for alpha in range(100,0, -1):
        fadeS.set_alpha(alpha)
        s.blit(fadeS, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

class TextInput: #Text Box, snippet taken from an online source (https://github.com/Nearoo/pygame-text-input)
    """
    This class lets the user input a piece of text, e.g. a name or a message.
    This class let's the user input a short, one-lines piece of text at a blinking cursor
    that can be moved using the arrow-keys. Delete, home and end work as well.
    """
    def __init__(
            self,
            initial_string="",
            font_family="",
            font_size=35,
            antialias=True,
            text_color=(0, 0, 0),
            cursor_color=(255,255,255),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35,
            max_string_length=20):
        """
        :param initial_string: Initial text to be displayed
        :param font_family: name or list of names for font (see pygame.font.match_font for precise format)
        :param font_size:  Size of font in pixels
        :param antialias: Determines if antialias is applied to font (uses more processing power)
        :param text_color: Color of text (duh)
        :param cursor_color: Color of cursor
        :param repeat_keys_initial_ms: Time in ms before keys are repeated when held
        :param repeat_keys_interval_ms: Interval between key press repetition when held
        :param max_string_length: Allowed length of text
        """

        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.max_string_length = max_string_length
        self.input_string = initial_string  # Inputted text

        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)

        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {}  # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size / 20 + 1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500  # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()

    #updates the textbox
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True  # So the user sees where he writes

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]

                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                        self.input_string[:max(self.cursor_position - 1, 0)]
                        + self.input_string[self.cursor_position:]
                    )

                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + self.input_string[self.cursor_position + 1:]
                    )

                elif event.key == pl.K_RETURN:
                    return True

                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == pl.K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == pl.K_HOME:
                    self.cursor_position = 0

                elif len(self.input_string) < self.max_string_length or self.max_string_length == -1:
                    # If no special key is pressed, add unicode of key to input_string
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + event.unicode
                        + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]

        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                    self.keyrepeat_intial_interval_ms
                    - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False
    
    #Gets surface
    def get_surface(self):
        return self.surface

    #gets text
    def get_text(self):
        return self.input_string

    #gets the cursor position
    def get_cursor_position(self):
        return self.cursor_position

    #Sets the text color
    def set_text_color(self, color):
        self.text_color = color

    #Sets cursor color
    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    #Clears text
    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0
