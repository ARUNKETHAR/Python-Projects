'''
Created on Sep 30, 2016

@author: Mohamed Zahran
'''


'''
TASK 1
Inputs:
1) fileName: the name of the data file. Type: string

Returns:
1) pos: A list of positive reviews. Type: A list of strings
2) neg: A list of negative reviews. Type: A list of strings

Description:
This function takes a name of the data file (training or testing) for reading. 
Then it divides the reviews in this file into two lists, a list containing all 
positive reviews and a list containing all negative reviews
'''
import collections

def read_And_Divide_By_Sentiment(fileName):
    file = open(fileName, 'r')
    v = file.readlines()
    file.close()
    
    pos = []
    neg = []
    for line in v:
        x = line.split('\t')
        if int(x[1]) == 1:
            pos.append(x[0])
        else:
             neg.append(x[0])

    return pos, neg
        
'''
TASK 2
Inputs:
1) myData: A list of reviews. Type: A list of strings

Returns:
1) cleanedData: A list of cleaned reviews. Type: A list of strings

Description:
This function takes a list of reviews and cleans them by converting all 
characters to lower case and removing all non alphabetic characters
'''
def clean_Data(myData):
    newList = []
    
    for old in myData:
        newSentence = ""
        
        for ch in old:
            if ch == '':
                continue
            
            if ch.isalpha():
                newSentence += ch.lower()           
            elif ch == ' ':
                newSentence += ' '

        newList.append(newSentence)

    return(newList)
        
                
'''
TASK 3
Inputs:
1) trainData: A list of cleaned training reviews. Type: A list of strings

Returns:
1) vocab: A dictionary, words are keys and their frequencies are values. 
Type: A dictionary<key:word(type:string), value:frequency(type:int)>

Description:
This function takes a list of cleaned reviews and constructs a dictionary whose keys are
the unique words in all reviews of the input list, and values are the frequencies (count)
 of each word.
''' 
def calculate_Unique_Words_Freq(trainData):
    vocab = collections.defaultdict(int)
    
    for words in trainData:
        for word in words.split(" "):
            vocab[word] += 1

    return vocab

#TASK 4
#Inputs:
#1) posTrain: A list of cleaned positive training reviews. Type: A list of strings
#2) negTrain: A list of cleaned negative training reviews. Type: A list of strings

#Returns:
#1) posProb: The probability of a positive review. Type: float
#2) negProb: The probability of a negative review. Type: float

#Description:
#This function takes both the cleaned positive and negative reviews of the training set
#and returns the probability of a positive review and that of a negative review.
#'''
def calculate_Class_Probability(posTrain, negTrain):
    numberNeg = len(negTrain)
    numberPos = len(posTrain)
    P1 = numberPos + numberNeg
    probabilityNeg = numberNeg / P1
    probabilityPos = numberPos / P1
    return (probabilityPos, probabilityNeg)
    
'''
TASK 5
Inputs:
1) classProb: the probability of the class (positive or negative)
Type: float
2) uniqueVocab: A dictionary, words are keys and their frequencies are values. 
Type: A dictionary<key:word(type:string), value:frequency(type:int)>
3) testData: A list of cleaned test reviews (positive or negative).


Returns:
1) testScores: A list of scores given to the input testData according to the input
training data. Type: A list of floats

Description:
This function calculates a score for each review in the input testData using statistics 
from the input training information: trainData, classProb and uniqueVocab. Then returns
a list of the calculated scores.
Note: the review at index i in testData will have the score at index i in testScores
''' 
def calculate_Scores(classProb, uniqueVocab, testData):
    scores = []
    
    totalFreq = 0
    for word, freq in uniqueVocab.items():
        totalFreq += freq
    
    for sentence in testData:
        score = classProb
        
        for word in sentence.split(" "):
            wordScore = float((uniqueVocab[word] + 1)) / float(totalFreq + len(uniqueVocab))
            score *= wordScore

        scores.append(score)

    return(scores)

    
'''
TASK 6
Inputs:
1) positiveTestDataPostiveScores: 
A list of scores for positive test data calculated from POSITIVE training data model  
Type: A list of floats
2) positiveTestDataNegativeScores: 
A list of scores for positive test data calculated from NEGATIVE training data model  
Type: A list of floats
3) negativeTestDataPostiveScores: 
A list of scores for negative test data calculated from POSITIVE training data model  
Type: A list of floats
4) negativeTestDataNegativeScores: 
A list of scores for negative test data calculated from NEGATIVE training data model  
Type: A list of floats
Returns:
1) tp: The number of true positives. Type: integer
2) fp: The number of false positives. Type: integer 
3) tn: The number of true negatives. Type: integer
4) fn: The number of false negatives. Type: integer


Description:
This function calculates the accuracy of the predictions we made for the test set. 
Because we know the correct classification for each review, i.e.,  whether it's positive or negative, 
we can compare the prediction we made to the truth and count the number of reviews whose predictions 
matched the truth and those didn't match. Using these counts we can calculate the accuracy 
of our predictions.
'''           
def calculate_Accuracy(positiveTestDataPostiveScores, positiveTestDataNegativeScores, negativeTestDataPostiveScores, negativeTestDataNegativeScores):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for e in range(len(negativeTestDataPostiveScores)):
        if(negativeTestDataPostiveScores[e] >= 0):
           negativeTestDataNegativeScores[e]
           fp += 1
    for i in range(len(positiveTestDataPostiveScores)):
        if(positiveTestDataPostiveScores[i] >= 0):
           positiveTestDataPostiveScores[i]
           tp += 1
        else:
             tn += 1
    return (tp, fp, tn, fn)
                     
                     
'''
Do not change the main function
'''
def main(): 
        
    trainingFile = 'TRAINING.txt'
    testingFile = 'TESTING.txt'      
         
    positiveTrainingData, negativeTrainingData = read_And_Divide_By_Sentiment(trainingFile)       
    positiveTestData, negativeTestData = read_And_Divide_By_Sentiment(testingFile)  
    
    cleanedPositiveTrainingData = clean_Data(positiveTrainingData)    
    cleanedNegativeTrainingData = clean_Data(negativeTrainingData)    
    cleanedPositiveTestData = clean_Data(positiveTestData)    
    cleanedNegativeTestData = clean_Data(negativeTestData)
    
    uniqueWordsPositiveTraining = calculate_Unique_Words_Freq(cleanedPositiveTrainingData)        
    uniqueWordsNegativeTraining = calculate_Unique_Words_Freq(cleanedNegativeTrainingData)
       
    posProb, negProb = calculate_Class_Probability(cleanedPositiveTrainingData, cleanedNegativeTrainingData)
                        
    positiveTestDataPostiveScores = calculate_Scores(posProb, uniqueWordsPositiveTraining, cleanedPositiveTestData)
    negativeTestDataPostiveScores = calculate_Scores(posProb, uniqueWordsPositiveTraining, cleanedNegativeTestData)    
    positiveTestDataNegativeScores = calculate_Scores(negProb, uniqueWordsNegativeTraining, cleanedPositiveTestData)    
    negativeTestDataNegativeScores = calculate_Scores(negProb, uniqueWordsNegativeTraining, cleanedNegativeTestData)
        
    tp, fp, tn, fn = calculate_Accuracy(positiveTestDataPostiveScores, positiveTestDataNegativeScores, negativeTestDataPostiveScores, negativeTestDataNegativeScores)
    
    print('tp, fp, tn, fn = ', tp, fp, tn, fn)
    

main()
