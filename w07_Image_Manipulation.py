"""
File: w07_Image_Manipulation.py
Author: Leah Tajon

Project: Image Manipulation in Python
"""
# DONE downloading the images for this assignment, unzip them, and save them to
# a location on my computer.

# INSTALLED the image library and import it in a Python program without errors.
from PIL import Image

# Load an image in Python and have it shown on the screen.
beach_img = Image.open("beach.jpg")
beach_img.show()

# Print out the size and format type of the image
print(beach_img.size) # The size is 800 x 600 
print(beach_img.format) # The format is JPEG

# Retrieve and print out the numbers corresponding to the pixel RGB values for 5 different pixels.
pixels_beach = beach_img.load() # The load() function retrieves the pixels(RGB) of an image

print(pixels_beach[200, 100]) # (160, 178, 214) 
print(pixels_beach[200, 101]) # (159, 179, 214) 
print(pixels_beach[200, 102]) # (159, 179, 216) 
print(pixels_beach[200, 103]) # (156, 178, 215) 
print(pixels_beach[200, 104]) # (158, 178, 213)

# Set a new color value for 5 different pixels.
pixels_beach[200, 100] = (255, 0, 0)    # FROM (160, 178, 214) TO (255, 0, 255) - Purple
pixels_beach[200, 101] = (255, 165, 0)  # FROM (159, 179, 214) TO (255, 165, 0) - ORANGE
pixels_beach[200, 102] = (255, 255, 0)  # FROM (159, 179, 216) TO (255, 255, 0) - YELLOW
pixels_beach[200, 103] = (0, 255, 0)    # FROM (156, 178, 215) TO (0, 255, 0) - BLUE
pixels_beach[200, 104] = (0, 0, 255)    # FROM (158, 178, 213) TO (0, 0, 255) - GREEN

# Show the version of the picture on the screen and observe the changed pixels.
beach_img.show()

