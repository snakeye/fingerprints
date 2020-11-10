from PIL import Image, UnidentifiedImageError
import sys
import argparse
import numpy
import pickle
import codecs

parser = argparse.ArgumentParser(
    description="Convert image to pixel array. The resulted image is returned to stdout"
)
parser.add_argument("file", type=str, help="Image file to convert")

args = parser.parse_args()

size = 192, 192

try:
    # read image file
    im = Image.open(args.file).convert('L')
    # resize
    im.thumbnail(size)
    # extract pixels as numpy array
    pixels = numpy.array(im)
    # encode and out the pixels
    pickled = codecs.encode(pickle.dumps(pixels), "base64").decode()
    sys.stdout.write(pickled)

except FileNotFoundError:
    print("File {} not found.".format(args.file))

except UnidentifiedImageError:
    print("File {} is not an image".format(args.file))
