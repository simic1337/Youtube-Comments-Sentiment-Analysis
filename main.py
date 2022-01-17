from os import system
from train.testTrain import testClassifier

def linearSVC():
    system('cls')
    print ("You choose LinearSVC.\n")
    testClassifier(1)

def multinomialNB():
    system('cls')
    print ("You choose MultinomialNB.\n")
    testClassifier(2)

def complementNB():
    system('cls')
    print ("You choose ComplementNB.\n")
    testClassifier(3)

def bernoulliNB():
    system('cls')
    print ("You choose BernoulliNB.\n")
    testClassifier(4)

def logisticRegression():
    system('cls')
    print ("You choose Logistic Regression.\n")
    testClassifier(5)

def decisionTreeClassifier():
    system('cls')
    print ("You choose Decision Tree Classifier.\n")
    testClassifier(6)
    
def SVC():
    system('cls')
    print ("You choose SVC.\n")
    testClassifier(7)

def customYoutubeVideo():
    system('cls')
    print ("You choose Custom Youtube Video.\n")
    testClassifier(8)
    
def dataINfo():
    system('cls')
    print ("You choose Data Info.\n")
    testClassifier(9)

def exitProgram():
    system('cls')
    print('Goodbye!')

menuOptions = '[0] Exit program\n[1] LinearSVC\n[2] MultinomialNB\n[3] ComplementNB\n[4] BernoulliNB\n[5] LogisticRegression\n[6] DecisionTreeClassifier\n[7] SVC\n[8] Custom Youtube video\n[9] Dataset Info\n'

options = {
    0 : exitProgram,
    1 : linearSVC,
    2 : multinomialNB,
    3 : complementNB,
    4 : bernoulliNB,
    5 : logisticRegression,
    6 : decisionTreeClassifier,
    7 : SVC,
    8 : customYoutubeVideo,
    9 : dataINfo
    }

while True:
    try:
        print(menuOptions)
        number = int(input('Choose an option: '))
        if number < 0 or number > 9:
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