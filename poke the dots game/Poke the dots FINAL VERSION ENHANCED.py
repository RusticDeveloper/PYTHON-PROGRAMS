# Poke The Dots Version 4
# This is a graphical game where two dots move around
# the screen, bouncing off the edges. The user tries 
# to prevent the dots from colliding by pressing and 
# releasing the mouse button to teleport the dots to 
# a random location. The score is the number of seconds 
# from the start of the game.

#This enhanced version implements the following improvements

 #-> add a key press event handler 
 
    #- Each time a 'T/t' key is pressed the dots are teleported
    #- When 'Q/q' key is pressed the game quits
    #- When 'Enter' is pressed and the game is over the game restarts
    
 
 #-> add new features
    #- Adds a preview window
      #The preview screen has:
       #* A score board
       #* A play game button
       #* A instructions screen
         #> keys and mouse events
         #> Dinamic/ instrutions
         #> Achivements
    #- Each time a click is done outside of a dot, the game doubles the speed

from uagame import Window
from random import randint
from pygame import QUIT, Color, MOUSEBUTTONUP,MOUSEBUTTONDOWN, Rect, mouse, K_RETURN,K_PAUSE,K_ESCAPE,K_KP_ENTER, KEYDOWN, K_q, K_t
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle, rect as draw_rectangle
from math import sqrt

# User-defined functions

def main():
    game = Game()
    #game.draw_start_screen(1)
    #print(game._option_list)
    game.play()
    
# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self):
        # Initialize a Game.
        # - self is the Game to initialize
        
        self._window = Window('Poke the Dots', 900, 600)
        self._adjust_window()
        self._frame_rate = 90  # larger is faster game
        self._close_selected = False
        self._clock = Clock()
        self._small_dot_speed = [1,2]
        self._big_dot_speed = [2,1]
        self._small_dot = Dot('red', [50,75], 50, self._small_dot_speed, self._window)
        self._big_dot = Dot('blue', [200,100], 70, self._big_dot_speed, self._window)
        self._small_dot.randomize()
        self._big_dot.randomize()
        self._score = 0
        self._continue_game = True
        #my defined class properties
        self._option_selected = 0
        self._option_hovering = 0
        self._welcome_color = Color('white')
        self._welcome_font_color = Color('aquamarine3')
        self._start_screen_rectangle = Rect(50,50,800,500)
        self._best_three = [0,0,0]
        self._option_list = []
        #time variables to get score just when the player start/restart the game
        self._game_started_at = 0
        self._game_started = False
        
    
    def _adjust_window(self):
        # Adjust the window for the game.
        # - self is the Game to adjust the window for
        
        self._window.set_font_name('ariel')
        self._window.set_font_size(64)
        self._window.set_font_color('white')
        self._window.set_bg_color('black')
        
    def draw_start_screen(self,coloring = 0): 
        self._window.clear()
        # draw the rectangle to contain the options 
        draw_rectangle(self._window.get_surface(),self._welcome_color,self._start_screen_rectangle,5)
        
        # each string is represented by a rectangle that can be tracked to check the clicks and hovering
        play_option = self._window.draw_string('PLAY GAME', self._start_screen_rectangle.left +(self._start_screen_rectangle.w//3.5), self._start_screen_rectangle.top*2, self._welcome_font_color if self._option_hovering == 1 else 'white')
        score_option = self._window.draw_string('SCORE',self._start_screen_rectangle.left +(self._start_screen_rectangle.w//3.5), self._start_screen_rectangle.top*5,self._welcome_font_color if self._option_hovering == 2 else 'white')
        how_option = self._window.draw_string('HOW TO PLAY', self._start_screen_rectangle.left +(self._start_screen_rectangle.w//3.5), self._start_screen_rectangle.top*8,self._welcome_font_color if self._option_hovering == 3 else 'white')
        #mouse_position  = mouse.get_pos()
        #print(play_option.collidepoint(mouse_position))         
        # fills the option list with the rectangles correspondint o the options
        self._option_list = [play_option,score_option,how_option]
        #update th screen 
        self._window.update()
        
    def handle_option_selection(self):
        #varibles to use in the screen drawing
        mouse_position = mouse.get_pos()
        #print(play_option.collidepoint(mouse_position)) 
        for index, value in enumerate(self._option_list):
            if value.collidepoint(mouse_position):
                self._option_selected = index+1
                if self._option_selected == 1:
                    self.set_default_values()
                
                
    def handle_option_hovering(self):
        #varibles to use in the screen drawing
        mouse_position = (x_pos,y_pos) = mouse.get_pos() 
        for index, value in enumerate(self._option_list):            
            if value.collidepoint(mouse_position):
                self._option_hovering = index+1
    
    def draw_score_screen(self):
        self._window.clear()
        y_position = self._start_screen_rectangle.top
        for index,score in enumerate(self._best_three):
            text =  str(index+1)+') '+str(score)
            self._window.draw_string(text, self._start_screen_rectangle.left +(self._start_screen_rectangle.w//3.5),y_position , 'cadetblue3')
            y_position += self._window.get_font_height()+self._start_screen_rectangle.top
        self._window.draw_string('PRESS ESC TO RETURN',0,self._window.get_height()-self._window.get_font_height() , 'cadetblue3')                 
        self._window.update()        
    
    def draw_how_to_screen(self):
        self._window.clear()
        text = "Instructions /n When playing must click inside a dot to make both dots teleport and the ESC key to return to the start screen, also Q key closes the game,finally if the game is over it could be replayed if the RETURN/ENTER key is pressed. /n The SCORE option in the start screen lets u see the three best scores obtained since the game started"
        self._window.draw_string(text,0,self._window.get_font_height() , 'cadetblue3')
        self._window.update()        
        
    def set_default_values(self):
        self._continue_game = True
        self._game_started = True
        self._small_dot._velocity = self._small_dot_speed
        self._big_dot._velocity = self._big_dot_speed        
        self.handle_mouse_up()        
    
    def set_best_score(self):
        self._best_three.append(self._score)
        self._best_three.sort(reverse=True)
        self._best_three.pop()
    
    def play(self):
        # Play the game until the player presses the close icon
        # and then close the window.
        # - self is the Game to play

        while not self._close_selected:
            
            # play frames depending the screen
            self.handle_events()
            if self._option_selected == 0:
                self.handle_option_hovering()
                self.draw_start_screen()
            elif self._option_selected == 1:
                self.draw()
                self.update()                
            elif self._option_selected == 2:
                self.draw_score_screen()
            elif self._option_selected == 3:
                self.draw_how_to_screen()
        self._window.close()
           
    def handle_events(self):
        # Handle the current game events by changing the game
        # state appropriately.
        # - self is the Game whose events will be handled

        event_list = get_events()
        for event in event_list:
            self.handle_one_event(event)
            
    def handle_one_event(self, event):
        # Handle one event by changing the game state
        # appropriately.
        # - self is the Game whose event will be handled
        # - event is the Event object to handle
        if event.type == KEYDOWN:
            print('key pressed')
            if event.key == K_q:
                self._close_selected = True
            elif  self._continue_game and self._option_selected == 1 and event.key == K_t:
                self.handle_mouse_up()
            elif self._option_selected == 1 and not self._continue_game and event.key == K_RETURN:
                self.set_default_values()
                print ('TODO: restart game')
            elif self._option_selected != 0 and event.key == K_ESCAPE:
                self._option_selected = 0        
        
        if event.type == QUIT:
            self._close_selected = True
        elif self._option_selected == 0 and event.type == MOUSEBUTTONDOWN:
            self.handle_option_selection()
        elif self._continue_game and self._option_selected == 1 and event.type == MOUSEBUTTONDOWN:
            print(self._big_dot.check_click() , self._small_dot.check_click())
            if self._big_dot.check_click() or self._small_dot.check_click():
                self.handle_mouse_up()
            else:
                self._big_dot._velocity = list(map(lambda item: item * 2, self._big_dot._velocity))
                self._small_dot._velocity = list(map(lambda item: item * 2, self._small_dot._velocity))             
         #   self.handle_mouse_up()
            
                        
                
    def handle_mouse_up(self):
        # Respond to the player releasing the mouse button by
        # taking appropriate actions.
        # - self is the Game where the mouse up occurred
        # - event is the Event object to handle

        self._small_dot.randomize()
        self._big_dot.randomize()
 
    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        
        self._window.clear()
        self.draw_score()
        self._small_dot.draw()
        self._big_dot.draw()
        if not self._continue_game :
            self.draw_game_over()   
        self._window.update()
                        
    def update(self):
        # Update all game objects with state changes
        # that are not due to user events.
        # - self is the Game to update
        if self._continue_game == True:   
            self._small_dot.move()
            self._big_dot.move()
            if self._game_started:
                self._game_started_at = get_ticks() // 1000
                self._game_started = False
            self._score = (get_ticks() // 1000)-self._game_started_at
            self._clock.tick(self._frame_rate)
            
                                       
        
        if self._small_dot.intersects(self._big_dot):
            self._continue_game = False 
            if self._score not in self._best_three:
                self.set_best_score()
        
        
    def draw_score(self):
        # Draw the time since the game began as a score.
        # - self is the Game to draw for
        
        string = 'Score: ' + str(self._score)
        self._window.draw_string(string, 0, 0)
        
    def draw_game_over(self):
        string = 'GAME OVER'
        font_color = self._small_dot.get_color()
        bg_color = self._big_dot.get_color()
        original_font_color = self._window.get_font_color()
        original_bg_color = self._window.get_bg_color()
        self._window.set_font_color(font_color)
        self._window.set_bg_color(bg_color)
        height = self._window.get_height() - self._window.get_font_height()
        self._window.draw_string(string, 0, height)
        self._window.set_font_color(original_font_color)
        self._window.set_bg_color(original_bg_color)        
        # draw the game over text to show the game has finished
              
    

class Dot:
    # An object in this class represents a colored circle
    # that can move.

    def __init__(self, color, center, radius, velocity, window):
        # Initialize a Dot.
        # - self is the Dot to initialize
        # - color is the str color of the dot
        # - center is a list containing the x and y int
        # coords of the center of the dot
        # - radius is the int pixel radius of the dot
        # - velocity is a list containing the x and y components
        # - window is the game's Window

        self._color = color
        self._center = center
        self._radius = radius
        self._velocity = velocity
        self._window = window

    def move(self):
        # Change the location and the velocity of the Dot so it
        # remains on the surface by bouncing from its edges.
        # - self is the Dot

        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            # update center at index
            self._center[index] = self._center[index] + self._velocity[index]
            # dot perimeter outside window?
            if (self._center[index] < self._radius) or (self._center[index] + self._radius > size[index]):
                # change direction
                self._velocity[index] = - self._velocity[index]

    def draw(self):
        # Draw the dot on the surface.
        # - self is the Dot

        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius)
    
    def randomize(self):
        # Change the dot so that its center is at a random
        # point on the surface. Ensure that no part of a dot
        # extends beyond the surface boundary.
        # - self is the Dot

        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            self._center[index] = randint(self._radius, size[index] - self._radius)
            
    def intersects(self,dot):  
        distance = sqrt((self._center[0] - dot._center[0])**2 + (self._center[1] - dot._center[1])**2)
        return distance <= self._radius + dot._radius
    
    def check_click(self):
        
                x,y = mouse.get_pos()
                sqx = (x - self._center[0])**2
                sqy = (y - self._center[1])**2
                
                if sqrt(sqx + sqy) < self._radius:
                    print ('inside')
                    return True
                else:
                    print('outside')  
                    return False
    
    def get_color(self):
        return self._color

main()