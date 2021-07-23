import numpy as np
import json
import nltk
from nltk.stem import WordNetLemmatizer
import random
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD


lematizer = WordNetLemmatizer

intents = json.loads(open('intents.json').read())

words = []
classes = []
docs = []
ignires = ['?', '!', '.', ',']


#iterate through thejson file for responses
for intents in intents:
    with open 
