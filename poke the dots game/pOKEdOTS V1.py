#imports
from uagame import Window
from pygame import QUIT
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

# Main fucnction that makes the functionality
def main():
    # create the window 
    Window = create_window()
    # create the clock handler
    clock = Clock()
    # create game objects
    #biig dot
    big_dot_color ="blue"
    big_dot_radius =25
    big_dot_center =[200,100]
    big_dot_velosity =[2,1]
    
    #small dot
    small_dot_color ="red"
    small_dot_radius =23
    small_dot_center =[250,50]
    small_dot_velosity =[1,2]    
    
    #call the play_game fucntion
    play_game(Window,big_dot_color,big_dot_center,big_dot_radius,big_dot_velosity,clock,small_dot_color,small_dot_center,small_dot_radius,small_dot_velosity)
    Window.close()
    pass

# function to create and manage the window
def create_window():
    window=Window("Poke the dots",500,400)
    window.set_bg_color("black")
    return window

# function to play the game
def play_game(window,big_color,big_center,big_radius,big_velosity,clock,small_color,small_center,small_radius,small_velosity):
    close_selected=False
    while not close_selected:
        close_selected=handle_events()
        draw_game(window,big_color,big_center,big_radius,big_velosity,small_color,small_center,small_radius,small_velosity)
        update_game(window,big_center,big_radius,big_velosity,clock,small_center,small_radius,small_velosity)
    pass

#fucntion to update dot position on the window
def update_game(window,big_center,big_radius,big_velosity,clock,small_center,small_radius,small_velosity):
    frame_rate=90
    move_dot(window,big_center,big_radius,big_velosity)
    move_dot(window,small_center,small_radius,small_velosity)
    clock.tick(frame_rate)

#function to handle the user trgigerred  events 
def handle_events():
    closed = False
    events_list = get_events()
    for event in events_list:
        if event.type == QUIT:
            closed = True
    return closed
    pass

#function to draw game objects on time 
def draw_game(window,big_color,big_center,big_radius,big_velosity,small_color,small_center,small_radius,small_velosity):
    draw_dot(window,big_color,big_center,big_radius)
    draw_dot(window,small_color,small_center,small_radius)
    window.update()


# draw a dot on the screen
def draw_dot(window,color_string,center,radius):
    window.clear()
    surface = window.get_surface()
    draw_circle(surface,color_string,center,radius)
    

#move the dots
def move_dot(window, center, radius,velosity):
    size=[window.get_width(),window.get_height()]
    negative_size=[radius*2,radius*2]
    for index in range(0,2):
        center[index]=center[index]+velosity[index]
        if center[index]+radius >= size[index] or center[index]+radius < negative_size[index]:
            velosity[index]=-velosity[index]
    

main()