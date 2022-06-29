import pandas as pd
from os import path
import numpy as np
import spacy
import string
import re

english = spacy.load('en_core_web_sm')
stopWords = english.Defaults.stop_words

def removePunctuationFromString(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def removeWordsFromString(text):
    return ' '.join([word for word in text.split() if word.lower() not in stopWords])

def cleanFile(file):
    for index in range(len(file)):
        file.at[index, 'comment'] = removePunctuationFromString(
            str(file.at[index, 'comment']))
        file.at[index, 'comment'] = removeWordsFromString(
            str(file.at[index, 'comment']))
        file.at[index, 'comment'] = re.sub(
            '[^A-Za-z0-9]+', ' ', file.at[index, 'comment'])
    file['comment'].replace(' ', np.nan, inplace=True)
    file.dropna(subset=["comment"], inplace=True)
    file['comment'].replace('', np.nan, inplace=True)
    file.dropna(subset=["comment"], inplace=True)
    return file

def makeValidCSV(fileName):
    file = pd.read_csv(path.join('files\\raw\\', fileName +
                       '.csv'), names=['comment', 'polarity'])
    validFile = cleanFile(file)
    validFile.to_csv(path.join('files\\cleaned\\', fileName +
                     '.csv'), index=False, float_format='%.0f')