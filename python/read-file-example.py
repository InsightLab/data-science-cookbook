# -*- coding: utf-8 -*-
import os
import sys

def contador(arquivo):
    """
    Método para contar a quantidade de espaços, tabs e linhas de um determinado arquivo.

    :arg arquivo: arquivo que será utilizado

    :return: Uma tupla com a contagem dos espaços, tabs e linhas.
    """
    with open(arquivo, 'r') as file:
	    i = 0
	    espacos = 0
	    tabs = 0
	    for i, linha in enumerate(file):
	        espacos += linha.count(' ')
	        tabs += linha.count('\t')

	    #Retorna a tupla dos resultados
	    return espacos, tabs, i + 1


espacos, tabs, linhas = contador('iris-dataset.txt')
print("Espaços %d. Tabs %d. Linhas %d" % (espacos, tabs, linhas))