""" Disply version for somme modules
"""
import sys

print("Version de Python :" + sys.version)

# import "dm-tree"
# print("dm-tree: " + dm-tree.__version__)

import numpy
print("numpy: " + numpy.__version__)

import pandas
print("pandas: " + pandas.__version__)

import sklearn
print("sklearn: " + sklearn.__version__)

import keras
print("Keras: " + keras.__version__)

import tensorflow
print( "Tensorflow: " + tensorflow.__version__ )
print( f"Is GPU available: {tensorflow.test.is_gpu_available()}" )

# import cmake
# print("cmake: " + cmake.__version__)