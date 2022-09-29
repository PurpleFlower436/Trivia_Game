import pygame, sys
from pygame_widgets.button import Button
import pygame_widgets
from pygame_widgets.textbox import TextBox
print("hello") #delete later

# variables for pygame
winWidth = 600
winHeight = 600
# variables for commonly used colours
BLUE = (0, 0, 255)
font_match = pygame.font.match_font('calibri')

# initialise pygame settings and create game window
pygame.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Trivia Game")
WHITE = (255, 255, 255)
Black = (0,0,0)



# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()


#this function will write the text to the screen
def textRender(surface, text,size,x,y):
    font_match = pygame.font.match_font('calibri')
    font = pygame.font.Font(font_match,size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)





def TextInputScreen():
  
    textbox = TextBox(window, 100, 300, 400, 80, fontSize=50,
                  borderColour=(255, 0, 0), textColour=(0, 200, 0),
                  radius=10, borderThickness=5)

    while True:
        events = pygame.event.get()
        window.fill(Black)
        textRender(window,str("Please enter your name to get started!"),30, winWidth/2,60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit()
        pygame_widgets.update(events)
        pygame.display.update()


"""
def ChooseRandomTriviaCategory():
    while True:
        window.fill(Black)
"""








#this is a button that is created using the python widgets module. This button is the start button
# and once you click it, it will lead you to the input screen where the user will type in their name 

button = Button(window, 250, 450, 100, 50, text='Start',
        fontSize=50, margin=20,
        inactiveColour=(WHITE),pressedColor=(WHITE),
        radius=20,
        onClick=lambda: TextInputScreen()
     )

  



# create game loop
while True:
    mouse_position = pygame.mouse.get_pos()
    # 'processing' inputs (events)
    
    events = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit()
        
        
            
            
            
    #'updating' the game
    # 'rendering' to the window
    window.fill(Black)
    textRender(window,str("Welcome to our trivia game!"),30, winWidth/2,60)
    
    button.draw()
    pygame_widgets.update(events)
    pygame.display.update()
    #'flip' display - always after drawing...
    pygame.display.flip()

    
   
