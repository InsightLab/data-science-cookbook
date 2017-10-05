# -*- coding: utf-8 -*-


# Função para calcular a média dos valores de uma coleção
def mean(iterable):
	# https://docs.python.org/2/library/functions.html#sum
	# Ou simplesmente: total = sum(iterable)
	total = 0.
	for value in iterable:
		total += value
	return total/len(iterable)


# Função para calcular a mediana dos valores de uma coleção
# https://docs.python.org/2/library/functions.html#divmod
def median(iterable):
	quotient, remainder = divmod(len(iterable), 2)
	
	if remainder:
		return sorted(iterable)[quotient]
	return sum(sorted(iterable)[quotient - 1:quotient + 1]) / 2.


# Função para encontrar a moda entre os valores de uma coleção
def mode(iterable):
	# https://docs.python.org/2/library/collections.html#collections.Counter.most_common
	# Ou simplesmente: return Counter(iterable).most_common()
	# Mas é importante destacar que o retorno do Counter não é ordenado por default

	# https://docs.python.org/2/library/functions.html#max
	# Ou usando a função max(): return max(iterable, key=iterable.count), porém não funcionará para multiplos modes
	maxFrequency = max([iterable.count(value) for value in iterable])
	return [value for value in iterable if iterable.count(value) == maxFrequency][0] if maxFrequency > 1 else None