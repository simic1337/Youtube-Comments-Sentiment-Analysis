import pandas as pd
from os import path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, ComplementNB, BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
from data.plotData import getAllDataMetrics
import matplotlib.pyplot as plt
import time
from data.plotData import getDataMetricsForAlgorithm


def loadTrainingData():
    return pd.read_csv('files\\cleaned\\cleanedDataset.csv')

def loadInputData(fileName):
    return pd.read_csv(path.join('files\\cleaned\\', fileName + '.csv'))

def transformComments(data):
    cv = CountVectorizer(ngram_range=(1, 1))
    return cv.fit_transform(data['comment'].values.astype('U'))

def transformPolarity(data):
    return data['polarity'].values.astype('U')

def createModelMetrics(yTest, yPredict, trainingTime):
    confusionMatrix = confusion_matrix(yTest, yPredict)
    accuracyScore = accuracy_score(yTest, yPredict)
    disp = ConfusionMatrixDisplay(confusion_matrix=confusionMatrix, display_labels=[
                                  'negative', 'neutral', 'positive'])
    disp.plot()
    plt.show()
    print('Accuracy:', round(accuracyScore, 4) * 100, '%')
    print('Training time:', round(trainingTime, 4), 'seconds')
    getDataMetricsForAlgorithm(yPredict)

def trainModel(choice):
    modelOption = {
        1: LinearSVC(),
        2: MultinomialNB(),
        3: ComplementNB(),
        4: BernoulliNB(),
        5: LogisticRegression(),
        6: tree.DecisionTreeClassifier()
    }
    data = loadTrainingData()

    x = transformComments(data)
    y = transformPolarity(data)

    startTime = time.time()
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.20)
    model = modelOption[choice]
    model.fit(xTrain, yTrain)
    yPredict = model.predict(xTest)
    trainingTime = time.time() - startTime
    return yTest, yPredict, trainingTime

def testModel(menuChoice):
    yTest, yPredict, trainingTime = trainModel(menuChoice)
    createModelMetrics(yTest, yPredict, trainingTime)

def trainClassifierForYoutubeComments(videoID):
    trainingData = loadTrainingData()
    inputData = loadInputData(videoID)

    trainingComments = transformComments(trainingData)
    inputComments = transformComments(inputData)
    polarities = transformPolarity(trainingData)

    model = LogisticRegression()
    trainingComments.resize(
        (trainingComments.shape[0], inputComments.shape[1]))
    model.fit(trainingComments, polarities)
    prediction = model.predict(inputComments)

    for index in range(len(inputData)):
        inputData.at[index, 'polarity'] = prediction[index]
    inputData.to_csv(path.join('files\\cleaned\\', videoID +
                     '.csv'), index=False, float_format='%.0f')
    filePath = path.join('files\\cleaned\\', videoID + '.csv')
    getAllDataMetrics(filePath)