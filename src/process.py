import os
from PIL import Image


def process_image(image):
    new_image = Image.new('L', image.size)

    width, height = image.size

    for x in range(width):
        for y in range(height):
            px = image.getpixel((x, y))

            pxnew = int(px)

            new_image.putpixel((x, y), pxnew)

    return new_image


def process(file):
    # load image
    image = Image.open(file)

    # process image
    new_image = process_image(image)

    # save the result
    ofilename = os.path.join('results', os.path.basename(file))
    new_image.save(ofilename, 'PNG')


for file in os.listdir("database"):
    if file.endswith(".png"):
        print("Processing `{}`".format(file))
        process(os.path.join("database", file))
