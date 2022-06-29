from os import system, path
import re
from ML.train import testModel
from scrapers.youtubeCommentsScraper import scrapeCommentsOnVideo
from data.cleanData import makeValidCSV
from data.plotData import getAllDataMetrics
from ML.train import trainClassifierForYoutubeComments


def linearSVC():
    system('cls')
    print("LinearSVC.\n")
    testModel(1)


def multinomialNB():
    system('cls')
    print("MultinomialNB.\n")
    testModel(2)


def complementNB():
    system('cls')
    print("ComplementNB.\n")
    testModel(3)


def bernoulliNB():
    system('cls')
    print("BernoulliNB.\n")
    testModel(4)


def logisticRegression():
    system('cls')
    print("Logistic Regression.\n")
    testModel(5)


def decisionTreeClassifier():
    system('cls')
    print("Decision Tree Classifier.\n")
    testModel(6)


def customYoutubeVideo():
    system('cls')
    print("Custom Youtube video.\n")
    youtubeLink = str(input("Enter Youtube Video ID: "))
    # Rxtract Youtube video ID from URL
    regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
    match = regex.match(youtubeLink)
    if not match:
        print('Invalid Youtube Link')
    else:
        scrapeCommentsOnVideo(match.group('id'), path.join(
            'files\\raw\\', match.group('id') + '.csv'), None)
        makeValidCSV(match.group('id'))
        trainClassifierForYoutubeComments(match.group('id'))


def datasetInfo():
    system('cls')
    print("Dataset Info.\n")
    getAllDataMetrics('files\\cleaned\\cleanedDataset.csv')


def exitProgram():
    system('cls')
    print('Goodbye!')


menuOptions = '[0] Exit program\n[1] LinearSVC\n[2] MultinomialNB\n[3] ComplementNB\n[4] BernoulliNB\n[5] LogisticRegression\n[6] DecisionTreeClassifier\n[7] Custom Youtube video\n[8] Dataset Info\n'

options = {
    0: exitProgram,
    1: linearSVC,
    2: multinomialNB,
    3: complementNB,
    4: bernoulliNB,
    5: logisticRegression,
    6: decisionTreeClassifier,
    7: customYoutubeVideo,
    8: datasetInfo
}

while True:
    try:
        print(menuOptions)
        number = int(input('Choose an option: '))
        if number < 0 or number > 8:
            raise ValueError
    except ValueError:
        system('cls')
        print('ERROR: Enter a number in range [0 - 9]! \n')
        continue
    except:
        system('cls')
        print('ERROR: Something went wrong! \n')
        continue
    break

options[number]()