#!/usr/bin/env python
from naiveBayes import NaiveBayes
import random

# Car dataset
# Attribute Information:
#
# Class Values:
#
# unacc, acc, good, vgood
#
# Attributes:
#
# buying: vhigh, high, med, low.
# maint: vhigh, high, med, low.
# doors: 2, 3, 4, 5more.
# persons: 2, 4, more.
# lug_boot: small, med, big.
# safety: low, med, high.

#Retur dataset
def readFile(path):
    rawDataset = open(path, 'r')


    suffix = ['_buy', '_maint', '_doors', '_pers', '_lug', '_safety', '_class']

    dataset = []

    rawDataset.seek(0)
    for line in rawDataset:
    	l = line.split(',')
        l[-1] = l[-1].replace("\n", "")
        newTuple = map(lambda (x,y): x+y, zip( l , suffix))
        dataset.append( newTuple )

    return dataset

def main():

    preparedDataset = readFile('carData.txt')

    random.shuffle(preparedDataset)

    dataset = []
    #Features
    dataset.append([])
    #Label
    dataset.append([])

    for t in preparedDataset:
        dataset[0].append(t[:-1])
        dataset[1].append(t[-1])


    dataSet_x = dataset[0]
    dataSet_y = dataset[1]

    nTuples = len(dataSet_x)

    nToTrain = int(nTuples * 0.7)

    dataSet_x_train = dataSet_x[:nToTrain]
    dataSet_y_train = dataSet_y[:nToTrain]

    dataSet_x_test = dataSet_x[nToTrain:]
    dataSet_y_test = dataSet_y[nToTrain:]

    naive = NaiveBayes()

    naive.train(dataSet_x_train, dataSet_y_train)

    accuracy = 0.0

    results = naive.predict(dataSet_x_test)

    for index, r in enumerate(results):
        yPredicted = max(r, key=r.get)
        y = dataSet_y_test[index]
        
        if(y == yPredicted):
            accuracy += 1.0

    print accuracy / len(dataSet_y_test)

main()
