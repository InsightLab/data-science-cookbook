# -*- coding: utf-8 -*-	
from analises.descritiva import *


# Abre o arquivo garantindo que o mesmo será fechado ao final da manipulação
with open('iris-dataset.txt') as file:
	# Pulamos a linha do cabeçalho
	file.readline()
	# Cria uma lista contendo somente os valores da primeira coluna convertidos para float
	sepal_lengths = [float(linha.split()[0]) for linha in file.readlines()]

print 'Count: ', len(sepal_lengths)
print 'Minimum: ', medida_dispersao.minimum(sepal_lengths)
print 'Maximum: ', medida_dispersao.maximum(sepal_lengths)
print 'Mean: ', medida_central.mean(sepal_lengths)
print 'Median: ', medida_central.median(sepal_lengths)
print 'Mode: ', medida_central.mode(sepal_lengths)
print 'First Quartile: ', medida_dispersao.first_quartile(sepal_lengths)
print 'Range: ', medida_dispersao.range(sepal_lengths)
print 'Variance: ', medida_dispersao.sample_variance(sepal_lengths)
print 'Standard Deviation: ', medida_dispersao.standard_deviation(sepal_lengths)
print 'Coefficient of Variation: ', medida_dispersao.coefficient_variation(sepal_lengths)
print 'Skewness: ', medida_dispersao.skewness(sepal_lengths)
print 'Kurtosis: ', medida_dispersao.kurtosis(sepal_lengths)