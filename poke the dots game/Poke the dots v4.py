# Poke The Dots Version 3
# This is a graphical game where two dots move around
# the screen, bouncing off the edges. The user tries 
# to prevent the dots from colliding by pressing and 
# releasing the mouse button to teleport the dots to 
# a random location. The score is the number of seconds 
# from the start of the game.

from uagame import Window
from random import randint
from pygame import QUIT, Color, MOUSEBUTTONUP
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

# User-defined functions

def main():
    game = Game() 
    game._play_game() 
    
                                     
class Game:
    # An object in this class represents a complete game.
    # - window
    # - frame_rate
    # - close_selected
    # - clock
    # - small_dot
    # - big_bot
    # - score
    def __init__(self):
        self.window = Window('Poke the Dots', 500, 400)
        self._adjust_window()
        self._frame_rate = 90  # larger is faster game
        self._close_selected = False
        self._clock = Clock()
        self.small_dot = Dot('red', [50,75], 30, [1,2], self.window)
        self.big_dot = Dot('blue', [200,100], 40, [2,1], self.window)
        self.small_dot._randomize_dot()
        self.big_dot._randomize_dot()
        self._score = 0        
               
    def _adjust_window(self):
        self.window.set_font_name('ariel')
        self.window.set_font_size(64)
        self.window.set_font_color('white')
        self.window.set_bg_color('black')
        
    def _handle_mouse_up(self):
        # Respond to the player releasing the mouse button by
        # taking appropriate actions.
        
        self.small_dot._randomize_dot()
        self.big_dot._randomize_dot()   
        
    def _handle_events(self):
        # Handle the current game events by changing the game
        # state appropriately.
        # - game is the Game whose events will be handled
        
        event_list = get_events()
        for event in event_list:
            #handle one event
            if event.type == QUIT:
                self._close_selected = True
            elif event.type == MOUSEBUTTONUP:
                self._handle_mouse_up()   
                
    def _play_game(self):
        # Play the game until the player presses the close icon.
        # - game is the Game to play
        self._adjust_window()
        while not self._close_selected:
            # play frame
            self._handle_events()
            self._draw_game()
            self._update_game()
        self.window.close()
               
                                    
    def _handle_mouse_up(self):
        # Respond to the player releasing the mouse button by
        # taking appropriate actions.
        # - game is the Game where the mouse up occured
        # - event is the Event object to handle
    
        self.small_dot._randomize_dot()
        self.big_dot._randomize_dot()
     
    def _draw_game(self):
        # Draw all game objects.
        # - game is the Game to draw for
        
        self.window.clear()
        self._draw_score()
        self.small_dot._draw()
        self.big_dot._draw()
        self.window.update()
    
    def _draw_score(self):
        # Draw the time since the game began as a score.
        # - game is the Game to draw for
        
        string = 'Score: ' + str(self._score)
        self.window.draw_string(string, 0, 0)
                        
    def _update_game(self):
        # Update all game objects with state changes
        # that are not due to user events.
        # - game is the Game to update
    
        self.small_dot._move_dot()
        self.big_dot._move_dot()
        self._clock.tick(self._frame_rate)
        self._score = get_ticks() // 1000     

class Dot:
    # An object in this class represents a colored circle
    # that can move.
    # - color
    # - center
    # - radius
    # - velocity
    # - window
    def __init__(self,color,center,radius,velocity, window):
        self._color = color
        self._radius = radius
        self._center = center
        self._velocity = velocity
        self._window = window
        
    def _draw(self):
        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius)      
        
    def _randomize_dot(self):
        # Change the dot so that its center is at a random
        # point on the surface. Ensure that no part of a dot
        # extends beyond the surface boundary.
        
        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            self._center[index] = randint(self._radius, size[index] - self._radius)    

    def _draw_dot(self):
        # Draw the dot on the window.
        # - dot is the Dot to draw
    
        surface = self.window.get_surface()
        color = Color(self.color)
        draw_circle(surface, color, self.center, self.radius)
    
    def _move_dot(self):
        # Change the location and the velocity of the Dot so it
        # remains on the surface by bouncing from its edges.
        # - dot is the Dot to move
    
        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            # update center at index
            self._center[index] = self._center[index] + self._velocity[index]
            # dot edge outside window?
            if (self._center[index] < self._radius) or (self._center[index] + self._radius > size[index]):
                # change direction
                self._velocity[index] = - self._velocity[index]            
        
main()