#my hacking version 2
#esta es una version basada en el juego hacking del cursos de python coursera

from uagame import Window

# Create a window
window = Window("Hacking",600,600)

#calculate distances

#display header
print("DEBUG MODE")
print("1ATTEMPT(S) LEFT")

print("""
PROVIDE
SETTING
CANTINA
CUTTING
HUNTERS
SURVIVE
HEARING
HUNTING
REALIZE
NOTHING
OVERLAP
FINDING
PUTTING
""")
password=input("Enter password >")
print("""LOGIN FAILURE - TERMINAL LOCKED

PLEASE CONTACT AN ADMINISTRATOR""")
try: 
    input("PRESS ENTER TO EXIT")
except SyntaxError: 
    pass
    
# Close window

window.close