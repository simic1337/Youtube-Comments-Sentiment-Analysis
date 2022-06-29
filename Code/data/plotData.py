import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from wordcloud import WordCloud

def loadFile(filePath):
    return pd.read_csv(filePath)

def getWordFrequencyInComments(data):
    return pd.Series(' '.join(data['comment']).split()).value_counts()

def getTenMostFrequentWordsInComments(data):
    return getWordFrequencyInComments(data)[:10]

def getCommentsCount(data):
    totalNumberOfComments = len(data.index)
    positiveCommentsCount = (data['polarity'] == 1).sum()
    negativeCommentsCount = (data['polarity'] == -1).sum()
    neutralCommentsCount = (data['polarity'] == 0).sum()
    return totalNumberOfComments, positiveCommentsCount, negativeCommentsCount, neutralCommentsCount

def getCommentsPercentage(data):
    totalNumberOfComments, positiveCommentsCount, negativeCommentsCount, neutralCommentsCount = getCommentsCount(
        data)
    positiveCommentPercentage = round(
        positiveCommentsCount / totalNumberOfComments, 4) * 100
    negativeCommentPercentage = round(
        negativeCommentsCount / totalNumberOfComments, 4) * 100
    neutralCommentPercentage = round(
        neutralCommentsCount / totalNumberOfComments, 4) * 100
    return positiveCommentPercentage, negativeCommentPercentage, neutralCommentPercentage

def showDataInfo(data):
    print('Data head:\n', data.head())
    print('\nData tail:\n', data.tail())
    totalNumberOfComments, positiveCommentsCount, negativeCommentsCount, neutralCommentsCount = getCommentsCount(
        data)
    positiveCommentPercentage, negativeCommentPercentage, neutralCommentPercentage = getCommentsPercentage(
        data)
    print('\nComments info: \n')
    print('Total number of comments:', totalNumberOfComments)
    print('Number of positive comments:', positiveCommentsCount)
    print('Number of negative comments:', negativeCommentsCount)
    print('Number of neutral comments:', neutralCommentsCount)
    print('Percentage of positive comments:', positiveCommentPercentage, '%')
    print('Percentage of negative comments:', negativeCommentPercentage, '%')
    print('Percentage of neutral comments:', neutralCommentPercentage, '%')

def createBarChartAndPie(data):
    positiveCommentsCount, negativeCommentsCount, neutralCommentsCount = getCommentsCount(
        data)
    positiveCommentPercentage, negativeCommentPercentage, neutralCommentPercentage = getCommentsPercentage(
        data)
    sentiment = ['Positive', 'Negative', 'Neutral']
    commentsCount = [positiveCommentsCount,
                     negativeCommentsCount, neutralCommentsCount]
    plt.figure(1)
    plt.subplot(1, 2, 1)
    plt.bar(sentiment, commentsCount, color='gry', width=0.5)
    plt.title('Comments Sentiments Count')
    plt.ylabel('Number of comments')
    plt.subplot(1, 2, 2)
    plt.pie([positiveCommentPercentage, negativeCommentPercentage, neutralCommentPercentage],
            labels=sentiment, colors='gry', autopct='%1.2f%%', startangle=90)

def createWordFrequencyWordCloud(data):
    wordFrequency = getWordFrequencyInComments(data)
    tenMostFrequentWords = getTenMostFrequentWordsInComments(data)
    text = wordFrequency.to_string()
    wordcloud = WordCloud(width=1600, height=800).generate(text)
    plt.figure(2)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('Word frequency in comments')
    plt.figure(3)
    tenMostFrequentWords.plot.bar()
    plt.title('Ten most frequent words in comments')

def getAllDataMetrics(filePath):
    data = loadFile(filePath)
    data['comment'] = data['comment'].apply(str)
    showDataInfo(data)
    createBarChartAndPie(data)
    createWordFrequencyWordCloud(data)
    plt.show()

def getDataMetricsForAlgorithm(predictedValue):
    positiveCommentsCount = np.count_nonzero(predictedValue == "1")
    negativeCommentsCount = np.count_nonzero(predictedValue == "-1")
    neutralCommentsCount = np.count_nonzero(predictedValue == "0")
    totalNumberOfComments = len(predictedValue)
    positiveCommentPercentage = round(
        positiveCommentsCount / totalNumberOfComments, 4) * 100
    negativeCommentPercentage = round(
        negativeCommentsCount / totalNumberOfComments, 4) * 100
    neutralCommentPercentage = round(
        neutralCommentsCount / totalNumberOfComments, 4) * 100
    print('Number of positive comments:', positiveCommentsCount)
    print('Number of negative comments:', negativeCommentsCount)
    print('Number of neutral comments:', neutralCommentsCount)
    print('Percentage of positive comments:', positiveCommentPercentage, '%')
    print('Percentage of negative comments:', negativeCommentPercentage, '%')
    print('Percentage of neutral comments:', neutralCommentPercentage, '%')
    sentiment = ['Positive', 'Negative', 'Neutral']
    commentsCount = [positiveCommentsCount,
                     negativeCommentsCount, neutralCommentsCount]
    plt.figure(1)
    plt.subplot(1, 2, 1)
    plt.bar(sentiment, commentsCount, color=["green", "red", "yellow"], width=0.5)
    plt.title('Comments Sentiments Count')
    plt.ylabel('Number of comments')
    plt.subplot(1, 2, 2)
    plt.pie([positiveCommentPercentage, negativeCommentPercentage, neutralCommentPercentage],
            labels=sentiment, colors=["green", "red", "yellow"], autopct='%1.2f%%', startangle=90)
    plt.show()