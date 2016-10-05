# -*- coding: utf-8 -*-
from __future__ import division
from descritiva import medida_central, medida_dispersao
import math


# Função para calcular a correlação linear entre os valores de duas coleções numéricas
# Indica a força e a direção do relacionamento linear entre duas variáveis aleatórias. 
def correlation(x, y):
	return covariance(x, y) / math.sqrt(medida_dispersao.population_variance(x) * medida_dispersao.population_variance(y))


# Função para calcular a covariância entre os valores de duas coleções numéricas
# É uma medida do grau de interdependência (ou inter-relação) numérica entre duas variáveis aleatórias
def covariance(x, y):
	x_mean = medida_central.mean(x)
	y_mean = medida_central.mean(y)
	# https://docs.python.org/2.7/library/functions.html#zip
	return sum([(v1 - x_mean)*(v2 - y_mean) for v1, v2 in zip(x, y)]) / len(x)