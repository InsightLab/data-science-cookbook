from collections import defaultdict
from functools import reduce
import math

class NaiveBayes:

    def __init__(self):

        self.freqFeature = defaultdict(int)
        self.freqLabel = defaultdict(int)

        #Estrutura -> condFreqFeature[label][feature]
        self.condFreqFeature = defaultdict(lambda: defaultdict(int))

    def countFrequencies(self):
        allFeatures = reduce(lambda x, y: x+y, self.dataSet_x)

        for f in allFeatures:
            self.freqFeature[f] += 1

        for l in self.dataSet_y:
            self.freqLabel[l] += 1

    def countCondFrequencies(self):

        dataSet = list(zip(self.dataSet_x, self.dataSet_y)) #A partir de python 3, zip retorna object. Entao mudo para list

        for t in dataSet:
            for f in t[0]:
                # condFreqFeature[label][feature]
                self.condFreqFeature[t[1]][f] += 1


    def train(self, dataSet_x, dataSet_y):

        self.dataSet_x = dataSet_x
        self.dataSet_y = dataSet_y

        self.countFrequencies()
        self.countCondFrequencies()


    def probLikelihood(self, f, l, vocabulary):
        laplace = 1

        condFreq = self.condFreqFeature[l][f]
        prob = (float)(condFreq + laplace) / (self.freqLabel[l] + vocabulary)

        # print l + " - " + f + " = " + str(prob)

        return prob

    def predict(self, dataSet_x):

        # Correcao de Laplace
        # P( f | l) = (freq( f | l ) + laplace*) / ( freq(l)** + qnt(distinct(f))*** )
        #
        # * -> laplace smoothing: add 1
        # ** -> Frequencia com que o valor de label aparece
        # *** -> Quantidade de features distintas
        #

        # Devido a possibilidade de underflow de pontos flutuantes, eh interessante fazer
        # P(x1|l)*P(x2|l) ... -> exp(Log(P(x1|l)) + Log(P(x2|l))) ...



        probs = []
        totalTuples = len(self.dataSet_y)
        vocabulary = len(self.freqFeature)

        #Cada tupla
        for index, t in enumerate(dataSet_x):
            probs.append(defaultdict(float))

            #Cada label
            for l in self.dataSet_y:
                prob = 0.0

                #Cada feature
                for f in t:
                    prob += math.log(self.probLikelihood(f, l, vocabulary))

                prob += (self.freqLabel[l] / totalTuples)

                probs[index][l] = math.exp(prob)

        return probs
