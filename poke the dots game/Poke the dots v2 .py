# Poke The Dots Version 1
# This is a graphical game where two dots move around
# the screen, bouncing off the edges.

from uagame import Window
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

def main():
    window = create_window()
    game = create_game(window)
    #play the game with the game object made
    play_game(game) 
    window.close()
    
def create_window():
    # Create a window for the game, open it, and return it.

    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')
    return window
                    
def create_game(window):
    #game attributes
    game = Game()
    game.window=window
    game.close_selected=False
    game.frame_rate=90
    game.clock=Clock()
    #dot attributes
    game.small_dot=create_dot('red',[50,75],30,[1,2])
    game.big_dot=create_dot('blue',[200,100],40,[2,1])
    
    return game
    

def create_dot(color,center,radius,speed):
    
    dot = Dot()
    dot.color = color
    dot.center=center
    dot.radius=radius
    dot.velocity=speed
    
    return dot
                    
def play_game(game):
    # Play the game until the player presses the close icon.
    #use the game object to play the game
    # -game is the game to play
    while not game.close_selected:
        # play frame
        handle_events(game)
        draw_game(game)
        update_game(game)
           
def handle_events(game):
    #this function changes the property closed_selected of the game object
    
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            game.close_selected=True

                
def draw_game(game):
    # Draw all game objects.
    # - game: game object will be used to draw the game into the 
    
    game.window.clear()
    draw_dot(game.window, game.small_dot)
    draw_dot(game.window, game.big_dot)
    game.window.update()
                    
def update_game(game):
    # Update all game objects with state changes
    # that are not due to user events usuing game object.
    # - game is the game object
    
    move_dot(game.window, game.small_dot)
    move_dot(game.window, game.big_dot)
    game.clock.tick(game.frame_rate)
                
def draw_dot(window, dot ):
    # Draw the dot on the window.
    # - window is the Window to draw in
    # - dot is the object containig the features of the dot

    surface = window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius)

def move_dot(window, dot ):
    # Change the location and the velocity of the dot so it
    # remains on the surface by bouncing from its edges.
    # - window is the Window to move in
    # - dot is the object that contain the features of the dot

    size = (window.get_width(), window.get_height())
    for index in range(0, 2):
        # update center at index
        dot.center[index] = dot.center[index] + dot.velocity[index]
        # dot edge outside window?
        if (dot.center[index] <= dot.radius) or (dot.center[index] + dot.radius >= size[index]):
            # change direction
            dot.velocity[index] = - dot.velocity[index]

class Game:
    pass

class Dot:
    pass

main()