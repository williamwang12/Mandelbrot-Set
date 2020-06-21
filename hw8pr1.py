# hw8pr1.py
# Lab 8
#
# Name: William Wang
#

# keep this import line...
from cs5png3 import *


#
# a test function...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300,200)  # creates an image of width=300, height = 200

    # Nested loops!
    for r in range(200):  # loops over the rows with runner-variable r
        for c in range(300):  # loops over the cols with c
            if  c == r:   
                im.plotPoint( c, r, (255,0,0))
            #else:
            #    im.plotPoint( c, r, (255,0,0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#


def mult(c, n):
    """Mult uses only a loop and addition
       to multiply c by the positive integer n
    """
    result = 0 # Set the result to 0.
    for i in range(n): # Add a value of c to result, n times.
        result = result + c
    return result

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    result = 0 
    for i in range(n): 
        result = result**2 + c
    return result

def inMSet(c, n):
    """inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
       Then, it returns
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    result = 0
    for i in range(n):
        result = result**2 + c
        if (abs(result) > 2):
            return False

    return True  

def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0  and  row % 10 == 0:
        return True
    else:
        return False

def test():
    # I think that the image will have half the pixels as the original if we change the line. 
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file

    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    """scale accepts
           pix, the CURRENT pixel column (or row)
           pixMax, the total # of pixel columns
           floatMin, the min floating-point value
           floatMax, the max floating-point value
       scale returns the floating-point value that
           corresponds to pix
    """
    scalar = pix / pixMax
    difference = scalar * (floatMax - floatMin)
    return (floatMin + difference)

def mset():
    """Creates a 300x200 image of the Mandelbrot set
    """
    NUMITER = 25
    XMIN = -1.2
    XMAX = -.6
    YMIN = -.5
    YMAX = -.1
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            # Use scale twice:
            #   once to create the real part of c (x)
            x = scale(col,300,XMIN,XMAX)
            #   once to create the imaginary part of c (y)
            y = scale(row,200,YMIN,YMAX)
            # THEN, create c, choose n, and test:
            c = x + y*1j
            if inMSet(c, NUMITER):
                image.plotPoint(col, row, (255, 175, 0))
            else:
                image.plotPoint(col,row, (0, 0, 0))
    # we looped through every image pixel; we now write the file
    image.saveFile()

def example():
    """Shows how to access the pixels of an image.
       inputPixels is a list of rows, each of which is a list of columns,
           each of which is a list [r,g,b]
    """

    inputPixels = getRGB("./pngs/alien.png")
    inputPixels = inputPixels[::-1] # the rows are reversed

    height = len(inputPixels)
    width = len(inputPixels[0])
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            if col%10 < 5 and row%10 < 5: # only plot some of the pixels
                image.plotPoint(col, row, inputPixels[row][col])

    image.saveFile()