import os
from PIL import Image


def process(file):
    print("Processing `{}`".format(file))
    image = Image.open(file)

    width, height = image.size

    

for file in os.listdir("database"):
    if file.endswith(".png"):
        process(os.path.join("database", file))
