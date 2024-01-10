# import the pygame module, so you can use it
import pygame
import slidemodel as sm
import imagecreator as ic
import os, glob
from PIL import Image 
 
CANVAS_SIZE = 600
DEFAULT_SIZE = 4

def cleanTemps():
    files = glob.glob('tempfiles/*')
    for f in files:
        os.remove(f)

def saveToTemps(squares : dict):
    if not all([isinstance(x,Image.Image) for x in squares.values()]):
        raise RuntimeError("Squares are not all PIL images. Use imagecreator Split or Generate method to get squares")
    for key, image in squares.items():
        image.save(f"tempfiles/square{key}.jpg")
    return {i : f"tempfiles/square{i}.jpg" for i in squares.keys()}
        

def draw(screen : pygame.Surface, model : sm.Model, squares : dict):
    if not all([os.path.exists(x) for x in squares.values()]):
        raise RuntimeError("Squares are not all PIL images. Use imagecreator Split or Generate method to get squares")
    size = model.size
    for x in range(size):
        for y in range(size):
            value = model.value(x,y)
            squareSize = CANVAS_SIZE // model.size
            if value == -1:
                pygame.draw.rect(screen,(50,50,50),(x*squareSize,y*squareSize,squareSize,squareSize))
            else:
                image = pygame.image.load(squares[str(value)])
                screen.blit(image,(x * squareSize,y * squareSize))
    pygame.display.flip()
            

# define a main function
def main():
    
    cleanTemps()
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("files/slidelogo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    screen = pygame.display.set_mode((CANVAS_SIZE,CANVAS_SIZE + 100))

    model = sm.Model(DEFAULT_SIZE)
    model.generate()
    model.shuffle()

    squares = ic.generate(DEFAULT_SIZE)
    squares = saveToTemps(squares)
    draw(screen,model,squares)
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                cleanTemps()
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()