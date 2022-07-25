"""
File: w08_Prove.py
Author: Leah Tajon

Project: Image Manipulation using PIL 
"""

from PIL import Image
# Final Requirements

# 1 - Load a green image and a background image.
beach_img = Image.open("beach.jpg")     # Backround image
cactus_img = Image.open("cactus.jpg")   # Green image 

# 2 - Create a new image that is the same size as the other images.
combined_img = Image.new("RGB", beach_img.size) # The new image will have a 800 x 600 size

pixels_beach = beach_img.load()         # Retrieves the pixels of the background image
pixels_cactus = cactus_img.load()       # Retrieves the pixels of the green image                
pixels_combined = combined_img.load()   # Retrieves the pixels of the new image (combination of green and background image)

(width, height) = beach_img.size        # Retrieves the size of the background image (800 x 600)

# 3 - Iterate through all the pixels of the background image.
for x in range(0, width):
    for y in range(0, height):
        (r, g, b) = pixels_cactus[x, y]
        
        # Create conditions for the RGB values. 
        # 4 - Set the pixel in your new image to have the appropriate red, green, and blue values.
        if r < 155 and g >= 210 and b <= 155:
            pixels_cactus[x, y] = pixels_beach[x, y]
        else:
            pixels_beach[x, y] = pixels_cactus[x, y]
        pixels_combined[x, y] = pixels_beach[x, y]


# 5 - Save the new image to a file.
combined_img.save('beach_cactus1.jpg')
# 6 - Show the new image
combined_img.show()

# SHOWING CREATIVITY AND EXCEEDING  REQUIREMENTS
# Create a thumbnail for the new image

# Open the new image
img = Image.open("beach_cactus1.jpg")
# Set the thumbnail values
img.thumbnail((200, 200))

# Save the thumbnail in an image file
img.save("beach_cactus_thumbnail.jpg")
# Open the thumbnail file
thumbnail_img = Image.open("beach_cactus_thumbnail.jpg")
# Display the thumbnail image
thumbnail_img.show()


