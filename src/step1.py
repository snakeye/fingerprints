import sys
import codecs
import pickle
import numpy

pickled = "".join(sys.stdin.readlines())
pixels = pickle.loads(codecs.decode(pickled.encode(), "base64"))



pickled = codecs.encode(pickle.dumps(pixels), "base64").decode()
sys.stdout.write(pickled)
