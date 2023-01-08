# Hacking Version 6
# This is a graphical password guessing game that displays a 
# list of potential computer passwords. The player is allowed 
# up to 4 attempts to guess the password. Each time the user 
# guesses incorrectly, the user is prompted to make a new guess. 
# The game indicates whether the player successfully guessed 
# the password or not.

from uagame import Window
from time import sleep

def main():
    location = [0,0]
    attemps = 4  
    window = create_window()
    display_header(window,location,attemps)
    password = display_password_list(window,location)
    guess = get_guesses(window,password,location,attemps)
    end_game(window,guess,password)
    
def create_window():
    # create window
    window = Window('Hacking', 600, 500)
    window.set_font_name('couriernew')
    window.set_font_size(18)
    window.set_font_color('green')
    window.set_bg_color('black')
    return window
    
def display_header(window, location, attempts_left):
# display header
    header = ['DEBUG MODE', str(attempts_left) + ' ATTEMPT(S) LEFT', '']
    for header_line in header:
        # display header line
        display_line(window,header_line,location) 

def display_password_list(window, location):
    #   create password list    
    password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE',  'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
    for password in password_list:
        display_line(window,password,location)
    return password_list[7]  
           
def get_guesses(window, password, location, attempts_left):
    # get guesses
    prompt = 'ENTER PASSWORD >'
    string_height = window.get_font_height()
    guess = prompt_user(window,prompt,location)
    
    attempts_left = attempts_left - 1
    
    while guess != password and attempts_left > 0:
        # get next guess
        #   display attempts left
        display_line(window,str(attempts_left), [location[0], string_height])
        
        #   check warning
        check_warning(window,attempts_left)
                
        #   prompt for guess
        guess = prompt_user(window,prompt,location)
    
        attempts_left = attempts_left - 1    
    return guess
    
def end_game(window, guess, password):
    # end game
    #   clear window
    window.clear()
    
    #   create outcome
    if guess == password:
        # create success
        outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
        prompt = 'PRESS ENTER TO CONTINUE'
    else:
        # create failure
        outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '','PLEASE CONTACT AN ADMINISTRATOR', '']
        prompt = 'PRESS ENTER TO EXIT'
            
    location = display_outcome(window,outcome)
    
    #   prompt for end
    line_x = (window.get_width() - window.get_string_width(prompt)) // 2
    prompt_user(window,prompt,[line_x,location])        
    
    #   close window
    window.close()  
    
def display_line(window,string,location):
    pause_time = 0.3
    string_height = window.get_font_height()
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(pause_time)
    location[1] = location[1] + string_height   
    
def prompt_user(window, prompt, location):
    #   prompt for guess
    string_height = window.get_font_height()
    guess = window.input_string(prompt, location[0], location[1])
    location[1] = location[1] + string_height    
    return guess

def check_warning(window, attempts_left):
    string_height = window.get_font_height()
    if attempts_left == 1:
        # display warning
        warning_string = '*** LOCKOUT WARNING ***'
        warning_x = window.get_width() - window.get_string_width(warning_string)
        warning_y = window.get_height() - string_height
        display_line(window,warning_string, [warning_x, warning_y])
        
def display_outcome(window, outcome):
    #   display outcome 
    #      compute y coordinate
    string_height = window.get_font_height()
    outcome_height = (len(outcome) + 1)*string_height
    y_space = window.get_height() - outcome_height
    line_y = y_space // 2
    
    for outcome_line in outcome:
        # display centered outcome line
        #    compute x coordinate
        x_space = window.get_width() - window.get_string_width(outcome_line)
        line_x = x_space // 2
        display_line(window,outcome_line,[ line_x, line_y])
        line_y = line_y + string_height
    return line_y

main()