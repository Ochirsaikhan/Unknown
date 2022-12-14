#!/usr/bin/env python
# Imports the necessary modules.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import json
import markovify
import requests
from io import BytesIO
import random

# Prepares the markovify model.
file = open("inputs")
model = markovify.NewlineText(file)

# Random integer between 1 and 2.
n = random.randint(1, 2)

#Uses the Unsplash API and get 30 or 21 image JSON file depending on the variable n.
#The collection I'm using has only 76 images. 51 images of the 76 are landscape images. 
#I'm using only landscape images because portrait images make the font size smaller since the font size is calculated by the width of an image.
#If the n == 1, the program will request the first page, which has 30 landscape images in it.
#If the n == 2, the program will request the second page which has 21 landscape images in it.
# You should use your UNSPLASH API key in the "?client_id = {YOUR-UNSPLASH-API-KEY}" section.
unsplash_api_key = os.getenv('UNSPLASH_API_KEY') # <-- correct method is getenv()
response = requests.get(f"https://api.unsplash.com/collections/1977302/photos/?client_id={unsplash_api_key}&per_page=30&page={n}&orientation=landscape")

image_json = response.json()

# Chooses a random image URL from the JSON file, which was given by the API.
if n == 2:
    random_number = random.randint(0, 20)
else:
    random_number = random.randint(0, 29) 

# Gets the link of one random image with the "regular" size option. 
img_url = image_json[random_number]["urls"]["regular"]
img_response = requests.get(img_url)

# Opens the image from the Image URL.
image = Image.open(BytesIO(img_response.content))
# Copies the image.
text_image = image.copy()
# Blurs the image using GaussianBlur.
text_image = text_image.filter(ImageFilter.GaussianBlur(2))
# Creates a draw object.
draw = ImageDraw.Draw(text_image)

# This function returns a three-line quote generated by markovify.
# The return will be a string joined by the new line character. 
def make_quote():
    quotes = []
    for i in range(3):
        # Maximum character is 100.
        quotes.append(model.make_short_sentence(100))
    quote = "\n".join(quotes)
    return quote

# Calls the make_quote function and stores the return value in the "quote" variable.
quote = make_quote()

# This function returns the font size depending on the quote length and image width.
# The font-size also depends on the font type, but I'm using only one font. 
# This function is from the professor's demo, and it helped me a lot and saved me a lot of time.
def make_font(img, text):
    # Set up basic information to load type
    font_size = 1
    face = "../data/DeliusSwashCaps-Regular.ttf"
    font = ImageFont.truetype(face)
    
    # Get image size
    x = img.size[0]
    
    # While the type width is less than 75% of the 
    # destination image size, keep increasing the
    # size of the type 1 point at a time
    while font.getsize_multiline(text)[0] < x * .85:
        font_size += 1
        font = ImageFont.truetype(face, font_size)
    
    # Return the ImageFont object at correct size
    return font

# Calls the make_font function and stores the returned object in the "font" variable.
font = make_font(text_image, quote)

# Calculates the quote location.
x, y = text_image.size
type_x, type_y = font.getsize_multiline(quote)

final_x = (x - type_x) / 2
final_y = (y - type_y) / 2.5

# Draws the quote on the image with black color and center alignment.
draw.multiline_text(
    (final_x, final_y),
    quote,
    (0, 0, 0),
    font = font,
    align = "center"
)

# This function draws a line and "UNKNOWN" text below the quote based on the quote length.
# The length of the line and the position of the "UNKNOWN" changes depending on the quote.
def make_border(img, quote, font):
    d = ImageDraw.Draw(img)
    x1, y1, x2, y2 = d.multiline_textbbox((final_x, final_y), quote, font = font, align = 'center')
    # Calculates the coordinates of the line and author text.
    x1 = x1 - 20
    y1 = y1 - 70
    x2 = x2 + 20
    y2 = y2 + 70
    x3 = (x1 + (x2 - x1) / 3) 
    x4 = (x1 + ((x2 - x1) / 3) + ((x2 - x1) / 3))

    d.line([x3, y2, x4, y2], fill = "black", width = 2)
    # Draws the "UNKNOWN" text in the middle of the line using anchor = "mt".
    d.text((x3 + (x4 - x3) / 2, y2 + 50), "UNKNOWN", fill = "black", font = font, anchor = "mt")

# Calls the make_border function and draws the line and "UNKNOWN" author.
make_border(text_image, quote, font)
# Finally, it saves the quote in the output directory.
text_image.save("../output/quote.jpg", "JPEG")
# Closes the quotes.txt file.
file.close()
