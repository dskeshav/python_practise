# UCI repository link
# https://archive.ics.uci.edu/ml/datasets/Energy+efficiency

# Reserach paper
# http://people.maths.ox.ac.uk/tsanas/Preprints/ENB2012.pdf

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

dataset=pd.read_excel('ENB2012_data.xlsx')

print(dataset.head())