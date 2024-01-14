# import the pygame module, so you can use it
import pygame
import slidemodel as sm
import imagecreator as ic
import os, glob
from PIL import Image 
 
CANVAS_SIZE = 600
DEFAULT_SIZE = 3

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

def newModel(size : int):
    model = sm.Model(size)
    model.generate()
    model.shuffle()
    return model
        
def handle(model : sm.Model, mouseX : int, mouseY : int, squares):
    if mouseY <= 600:
        if not model.isCorrect():
            squareSize = CANVAS_SIZE // model.size
            row = mouseY // squareSize
            column = mouseX // squareSize
            try:
                model.swap(column,row,model.currentX,model.currentY)
                model.currentX = column
                model.currentY = row
            except:
                pass
    else:
        newSize = mouseX // (CANVAS_SIZE // 3) + 3
        model = newModel(newSize)
        cleanTemps()
        squares = saveToTemps(ic.generate(newSize))
    return model, squares

def draw(screen : pygame.Surface, model : sm.Model, squares : dict):
    if not all([os.path.exists(x) for x in squares.values()]):
        raise RuntimeError("Squares are not all PIL images. Use imagecreator Split or Generate method to get squares")
    size = model.size

    # display squares
    for x in range(size):
        for y in range(size):
            value = model.value(x,y)
            squareSize = CANVAS_SIZE // model.size
            if value == -1:
                pygame.draw.rect(screen,(50,50,50),(x*squareSize,y*squareSize,squareSize,squareSize))
            else:
                image = pygame.image.load(squares[str(value)])
                screen.blit(image,(x * squareSize,y * squareSize))

    # display buttons
    for x in range(3,6):
        buttonWidth = CANVAS_SIZE / 3
        buttonHeight = 100
        buttonX = buttonWidth * (x - 3)
        buttonY = screen.get_height() - buttonHeight
        pygame.draw.rect(screen,(200,200,200,200),(buttonX,buttonY,buttonWidth,buttonHeight))
        dimFont = pygame.font.Font("files/boldfont.ttf",64)
        dimText : pygame.Surface = dimFont.render(str(x),False,(0,0,0,100))
        screen.blit(dimText,(buttonX + buttonWidth/2 - dimText.get_width()/2,buttonY + buttonHeight/2 + 10 - dimText.get_height()/2))
    
    # if correct, display won screen
    if model.isCorrect():
        pygame.draw.rect(screen,(100,100,100,100),(150,150,300,300))
        winFont = pygame.font.Font("files/boldfont.ttf",48)
        winText : pygame.Surface = winFont.render("You Won!",False,(0,0,0,100))
        screen.blit(winText,(CANVAS_SIZE/2 - winText.get_width()/2,CANVAS_SIZE/2 - winText.get_height()/2))
    pygame.display.flip()

# define a main function
def main():
    
    cleanTemps()
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("files/slidelogo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Slide Puzzles: Python Edition")
     
    screen = pygame.display.set_mode((CANVAS_SIZE,CANVAS_SIZE + 100))

    model = newModel(DEFAULT_SIZE)

    squares = ic.generate(DEFAULT_SIZE)
    squares = saveToTemps(squares)

    draw(screen,model,squares)
     
    # define a variable to control the main loop
    running = True
    mouseDown = False
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                cleanTemps()
                running = False
        
        mouseX, mouseY = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if not mouseDown:
                mouseDown = True
                model, squares = handle(model,mouseX,mouseY,squares)
                draw(screen,model,squares)
        else:
            mouseDown = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()