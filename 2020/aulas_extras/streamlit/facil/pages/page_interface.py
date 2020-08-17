import abc

"""
Funções obrigatórias para uma página
"""


class Page(abc.ABC):

	@abc.abstractmethod
	def render(self):
		"""
		Função para renderizar a página

		Returns:
			A instanciação dos elementos desejados

		"""
		pass