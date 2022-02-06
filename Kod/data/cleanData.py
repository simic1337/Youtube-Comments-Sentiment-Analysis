import pandas as pd
from os import path
import numpy as np
import spacy
import string
import re

# spacy is library for natural language processing and 'en_core_web_sm' file contains stopwords which
# are not needed for model training. Some examples are often, the, therefore, another, if, whereafter, your, thereby, does, etc...
english = spacy.load('en_core_web_sm')
stopWords = english.Defaults.stop_words


def removePunctuationFromString(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def removeWordsFromString(text):
    return ' '.join([word for word in text.split() if word.lower() not in stopWords])


def cleanFile(file):
    for index in range(len(file)):
        # remove punctuation from string
        file.at[index, 'comment'] = removePunctuationFromString(
            str(file.at[index, 'comment']))
        # remove stop words from string
        file.at[index, 'comment'] = removeWordsFromString(
            str(file.at[index, 'comment']))
        # remove everything other than number or letter, in this case remove emojis
        file.at[index, 'comment'] = re.sub(
            '[^A-Za-z0-9]+', ' ', file.at[index, 'comment'])
    # remove empty lines, first mark them as NaN, then drop them from dataframe
    file['comment'].replace(' ', np.nan, inplace=True)
    file.dropna(subset=["comment"], inplace=True)
    file['comment'].replace('', np.nan, inplace=True)
    file.dropna(subset=["comment"], inplace=True)
    return file


def makeValidCSV(fileName):
    file = pd.read_csv(path.join('files\\raw\\', fileName +
                       '.csv'), names=['comment', 'polarity'])
    validFile = cleanFile(file)
    # index is False in order to remove adding line numbers, and float format is set to '%.0f', because by deafult numbers are in a float format
    validFile.to_csv(path.join('files\\cleaned\\', fileName +
                     '.csv'), index=False, float_format='%.0f')
