from PIL import Image, ImageDraw, ImageFont

CANVAS_SIZE = 600

def split(image : Image.Image, size : int) -> list:
    resizedImage = image.resize((CANVAS_SIZE,CANVAS_SIZE))
    splits = []
    splitSize = (CANVAS_SIZE / size)
    for i in range(size):
        for j in range(size):
            x = j * splitSize
            y = i * splitSize
            splits.append(resizedImage.crop((x,y,x+splitSize,y+splitSize)))
    return splits

def generate(size : int) -> dict:
    squareSize = CANVAS_SIZE // size
    squares = {}
    for i in range(size):
        for j in range(size):
            position = size*i + j + 1
            canvas = Image.new("RGB",(squareSize,squareSize))
            canvasDraw = ImageDraw.ImageDraw(canvas)
            canvasDraw.rectangle((0,0,squareSize,squareSize),fill="grey")
            font = ImageFont.truetype('files/boldfont.ttf',70)
            canvasDraw.text((squareSize/2,squareSize/2),text = str(position), font=font, fill = "black", anchor="mm")
            squares[str(position)] = canvas
    return squares