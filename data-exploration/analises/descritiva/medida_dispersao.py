# -*- coding: utf-8 -*-
from __future__ import division
import medida_central
import sys
import math


# Função para encontrar o valor mínimo em uma coleção
# Esta é uma funcionalidade built-in function chamada min()
# https://docs.python.org/2/library/functions.html#min
def minimum(iterable):
	# Inicializa a variável com o maior int possível
	minimum = sys.maxint
	for value in iterable:
		if value < minimum:
			minimum = value
	return minimum


# Função para encontrar o valor máximo em uma coleção
# Esta é uma funcionalidade built-in function chamada max()
# https://docs.python.org/2/library/functions.html#max
def maximum(iterable):
	maximum = 0
	for value in iterable:
		if value > maximum:
			maximum = value
	return maximum

# Função para calcular o primeiro quartil dos valores de uma coleção
# É o valor aos 25% da amostra ordenada
# Um quartil é qualquer um dos três valores que divide o conjunto ordenado de dados em quatro partes iguais, e assim cada parte representa 1/4 da amostra ou população.
def first_quartile(iterable):
	aux = list(iterable	)
	aux.sort()
	first = int( round( ( len(iterable) + 1 ) / 4.0 ) - 1 )
	return aux[first]


# Função que calcula a diferença entre o valor máximo e mínimo dos valores de uma coleção
def range(iterable):
	return maximum(iterable) - minimum(iterable)


# Função para calcular a variância amostral dos valores de uma coleção
# É a medida de dispersão que mostra quão distantes os valores estão da média.
# https://pt.wikipedia.org/wiki/Vari%C3%A2ncia
def sample_variance(iterable):
	mean = medida_central.mean(iterable)
	return sum([(value - mean)**2 for value in iterable]) / (len(iterable) - 1)


# Função para calcular a variância da população dos valores de uma coleção
# https://pt.wikipedia.org/wiki/Vari%C3%A2ncia
def population_variance(iterable):
	mean = medida_central.mean(iterable)
	return sum([(value - mean)**2 for value in iterable]) / len(iterable)


# Função para calcular o desvio padrão dos valores de uma coleção
"""
É a medida mais comum da dispersão estatística. Ele mostra o quanto de variação ou "dispersão" existe em relação à média (ou valor esperado). 
Um baixo desvio padrão indica que os dados tendem a estar próximos da média; um desvio padrão alto indica que os dados estão espalhados por uma gama de valores.
"""
def standard_deviation(iterable): 
	return math.sqrt(sample_variance(iterable))


# Função para calcular o coeficiente de variação dos valores de uma coleção
"""
Coeficiente de variação é uma medida de dispersão relativa, empregada para estimar a precisão de experimentos e representa o desvio-padrão expresso como porcentagem da média.
"""
def coefficient_variation(iterable):
	return (standard_deviation(iterable)/medida_central.mean(iterable)) * 100


# Função para cacular a obliquidade dos valores de uma coleção
# Obliquidade é uma medida da assimetria de uma determinada distribuição de frequência.
def skewness(iterable):
	mean = medida_central.mean(iterable)
	amount = len(iterable)
	sd = standard_deviation(iterable)
	total_sum = sum([((value - mean)/sd)**3 for value in iterable])
	return (amount/((amount - 1) * (amount - 2))) * total_sum


# Função para cacular a curtose dos valores de uma coleção
# Curtose é uma medida de dispersão que caracteriza o pico ou "achatamento" da curva da função de distribuição de probabilidade
def kurtosis(iterable):
	mean = medida_central.mean(iterable)
	amount = len(iterable)
	sd = standard_deviation(iterable)
	total_sum = sum([((value - mean)/sd)**4 for value in iterable])	
	return (((amount * (amount + 1)) / ((amount - 1) * (amount - 2) * (amount - 3))) * total_sum) - (3 * ((amount - 1)**2) / (amount - 2) * (amount - 3))
