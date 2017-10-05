#!/usr/bin/env python
from naiveBayes import NaiveBayes
import random
import math

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

    #Adicionamos os sufixos para cada valor de feature relativo a sua coluna,
    #para que a contagem de frequencias nao conflite com valores semelhantes em diferentes features
    suffix = ['_buy', '_maint', '_doors', '_pers', '_lug', '_safety', '_class']

    dataset = []

    rawDataset.seek(0)
    for line in rawDataset:
    	l = line.split(',')
        #Elimina o caractere de breakline do texto
        l[-1] = l[-1].replace("\n", "")
        newTuple = map(lambda (x,y): x+y, zip( l , suffix))
        dataset.append( newTuple )

    return dataset

def main():

    preparedDataset = readFile('carData')

    #Para toda execucao da main, randomiza os dados
    random.shuffle(preparedDataset)

    dataset = []
    #Features
    dataset.append([])
    #Label
    dataset.append([])

    #Separa para dataset[0] como um vetor de vetores, onde cada elemento eh uma linha de features
    #Para dataset[1] eh o vetor com as labels (classes)
    for t in preparedDataset:
        dataset[0].append(t[:-1])
        dataset[1].append(t[-1])

    #Conjunto de features
    dataSet_x = dataset[0]
    #Conjunto de classes
    dataSet_y = dataset[1]
    #Repare acima, dataSet_x[0] representa as features da linha 1 do conjunto, bem como dataSet_y[0] eh a classe da linha 1

    nTuples = len(dataSet_x)

    nToTrain = int(math.floor(nTuples * 0.7))

    dataSet_x_train = dataSet_x[:nToTrain]
    dataSet_y_train = dataSet_y[:nToTrain]

    dataSet_x_test = dataSet_x[nToTrain:]
    dataSet_y_test = dataSet_y[nToTrain:]

    #Instancia o NaiveBayes
    naive = NaiveBayes()

    #Passa os dados para treino
    #naive.train(features, class)
    naive.train(dataSet_x_train, dataSet_y_train)

    accuracy = 0.0

    #Faz a predicao
    #naive.predict(dados_para_classificar -> apenas features)
    results = naive.predict(dataSet_x_test)

    #Faz apenas o "score" do modelos, calculando quantos foram preditos corretamente
    for index, r in enumerate(results):
        yPredicted = max(r, key=r.get)
        y = dataSet_y_test[index]

        if(y == yPredicted):
            accuracy += 1.0

    print accuracy / len(dataSet_y_test)

main()
