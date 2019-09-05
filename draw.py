import numpy as np
from PIL import Image

# Create a NumPy array, which has four elements. The top-left should be pure red, the top-right should be pure blue, the bottom-left should be pure green, and the bottom-right should be yellow
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]
black = [0, 0, 0]
white = [255, 255, 255]

# pixels = np.array([[red, green], [blue, yellow]])

pixel_data = []

for i in range(100):
    for j in range(100):

        # Create a PIL image from the NumPy array
image = Image.fromarray(pixels.astype('uint8'), 'RGB')

# Print out the pixel values
# print image.getpixel((0, 0))
# print image.getpixel((0, 1))
# print image.getpixel((1, 0))
# print image.getpixel((1, 1))

# Save the image
image.show()
