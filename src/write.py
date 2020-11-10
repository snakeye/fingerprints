from PIL import Image, UnidentifiedImageError
import sys
import argparse
import numpy
import pickle
import codecs

parser = argparse.ArgumentParser(
    description="Pixel array to image"
)
parser.add_argument("file", type=str, help="Image file to save")

args = parser.parse_args()

pickled = "".join(sys.stdin.readlines())
unpickled = pickle.loads(codecs.decode(pickled.encode(), "base64"))

im = Image.fromarray(unpickled).convert("RGB")

im.save(args.file)
