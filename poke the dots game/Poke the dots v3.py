#Poke the dots version 3 

# This is a graphical game where two dots move around
# the screen, bouncing off the edges.
# A score is added, it is the time elapsed since the game started
# Dots are teleported when a click event occurs

from uagame import Window
from pygame import QUIT, Color,MOUSEBUTTONUP, KEYDOWN, K_q
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from random import randint

# User-defined functions

def main():
    window = create_window()
    game = create_game(window)
    play_game(game) 
    window.close()
    
def display_line(window, string, location):
    window.draw_string(string, location[0], location[1])


def create_window():
    # Create a window for the game, open it, and return it.

    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')
    window.set_font_size(50)
    window.set_font_color('white')    
    return window
                    
def create_game(window):
    # Create a Game object for Poke the Dots.
    # - window is the Window that the game is played in
    
    game = Game()
    game.window = window
    game.frame_rate = 90  # larger is faster game
    game.close_selected = False
    game.clock = Clock()
    game.is_clicked = False
    game.small_dot = create_dot('red', [50,75], 30, [1,2], window)
    game.big_dot = create_dot('blue', [200,100], 40, [2,1], window)
    return game

def create_dot(color, center, radius, speed, window):
    dot = Dot()
    dot.color = color
    dot.center = center
    dot.radius = radius
    dot.velocity = speed
    dot.window = window
    return dot
    
def play_game(game):
    
    while not game.close_selected:
        # play frame
        handle_events(game)
        draw_game(game)
        update_game(game)
           
def handle_events(game):
    
    event_list = get_events()
    for event in event_list:
        #handle one event
        if event.type == QUIT:
            game.close_selected = True
        elif event.type == MOUSEBUTTONUP:
            game.is_clicked = True
        elif event.type == KEYDOWN:
            if event.key == K_q:
                game.close_selected = True
                                
def draw_game(game):
    
    game.window.clear()
    # Compute a random center to redraw the dot
    if game.is_clicked==True:
        width = game.window.get_width()
        heigth = game.window.get_height()
        game.small_dot.center[0]= randint(game.small_dot.radius,width-game.small_dot.radius)
        game.small_dot.center[1]= randint(game.small_dot.radius,heigth-game.small_dot.radius)
        game.big_dot.center[0]= randint(game.big_dot.radius,width-game.big_dot.radius)
        game.big_dot.center[1]= randint(game.big_dot.radius,heigth-game.big_dot.radius)
        game.is_clicked=False
    
    draw_dot(game.small_dot)
    draw_dot(game.big_dot)
    game.window.update()
                    
def update_game(game):
    # Update all game objects with state changes
    # that are not due to user events.
    # - game is the Game to update

    move_dot(game.small_dot)
    move_dot(game.big_dot)
    game.clock.tick(game.frame_rate)

def draw_dot(dot):
    # Draw the dot on the window.
    # - dot is the Dot to draw
    
    score_string='SCORE: '+str((get_ticks()//1000))
    display_line(dot.window,score_string,[0,0])
    surface = dot.window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius)

def move_dot(dot):
    # Change the location and the velocity of the Dot so it
    # remains on the surface by bouncing from its edges.
    # - dot is the Dot to move

    size = (dot.window.get_width(), dot.window.get_height())
    for index in range(0, 2):
        # update center at index
        dot.center[index] = dot.center[index] + dot.velocity[index]
        # dot edge outside window?
        if (dot.center[index] < dot.radius) or (dot.center[index] + dot.radius > size[index]):
            # change direction
            dot.velocity[index] = - dot.velocity[index]
                 
class Game:
    # An object in this class represents a complete game.
    # - window
    # - frame_rate
    # - close_selected
    # - clock
    # - small_dot
    # - big_bot
    
    pass

class Dot:
    # An object in this class represents a colored circle
    # that can move.
    # - color
    # - center
    # - radius
    # - velocity
    # - window

    pass

main()