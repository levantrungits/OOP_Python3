import numpy as np
from random import randint
import os
import json
import setting
import _pickle as cPickle
import nltk.data
from pyvi.pyvi import ViTokenizer
from sklearn.svm import LinearSVC
from gensim import corpora, matutils
from sklearn.metrics import classification_report

if __name__ == '__main__':
    print('Ok con ga den')