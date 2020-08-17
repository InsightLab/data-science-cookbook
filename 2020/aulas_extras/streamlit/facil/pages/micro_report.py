# Bibliotecas
import streamlit as st
from pages.page_interface import Page
import pandas as pd
from datetime import datetime

class MicroReport(Page):

	def __init__(self, path):
		self.path = path

	def cabeçalho(self):
		st.markdown('# (Micro)Relatório do catálogo da Netflix')

	def imports(self):

		st.markdown(
			'''Este (micro)relatório apresenta algumas informações extraídas de um dataset com o [catálogo da Netflix](https://www.kaggle.com/shivamb/netflix-shows), disponível no [Kaggle](https://www.kaggle.com/).
			
			As bibliotecas utilizadas são as seguintes:'''
		)

		code = '''
		import pandas as pd
		import matplotlib.pyplot as plt
		'''

		st.code(code)


	def carregar_dataset(self):

		st.markdown('## Passo 1: carregar o dataset')
		
		df = pd.read_csv("{}/netflix_titles.csv".format(self.path))

		code = '''df = pd.read_csv("{}/netflix_titles.csv".format(path))'''
		st.code(code)

		st.dataframe(df.head())

		st.markdown(
			''' Nosso dataset contém 6234 elementos, com 12 atributos cada, além de possuir missing data.
				Dentre os atributos existentes pra cada elemento do catálogo, vamos focar apenas nos seguintes (uma vez que esse é apenas um exemplo):

			* `type` - o tipo da obra (série ou filme)
			* `release_year` - ano de lançamento da obra
			* `date_added`- data de lançamento da obra
			* `director` - diretor da obra 
			'''
		)

		self.df = df

	def contagem_obras(self):
		
		st.markdown('### Contagem de tipos de obras')

		st.markdown('Uma coisa que podemos nos perguntar, nesse dataset, é se na Netflix existem mais filmes ou séries. Para descobrir isso, basta selecionarmos a série `type`, realizar uma contagem dos valores e desenhar um gráfico de barras')

		code = '''df.type.value_counts().plot(kind="bar")'''

		st.code(code)

		st.bar_chart(self.df.type.value_counts())


	def adicoes_tempo(self):
		
		st.markdown('## Adições ao passar do tempo')

		st.markdown(
			'''
			Outra informação interessante de se obter é analisar a "idade" dos conteúdos (ou seja, o quão antigos eles são) e quanta sadições são feitas por dia. Para isso, precisamos de dois gráficos:

			* o primeiro faz uma contagem do ano de produção das obras. Como este (micro)relatório foi escrito em meados de 2020, é injusto comparar os dados desse ano com os restantes. Logo, iremos filtrar os dados para apenas os de 2019 ou antes. Em seguida, fazemos a contagem dos elementos

			* o segundo é análogo ao anterior, porém não precisamos fazer o corte do ano de 2020, visto que a ideia é analisar as adições por dia. Logo, basta fazer a contagem pelas datas. Porém,temos dois problemas:
				- uma mesma data pode estar escrita de maneira diferente ('September 9, 2019' e ' Semptember 9, 2019'), logo realizar uma simples contagem não será o suficiente;
				- as "datas" são strings. Precisamos transformá-las para datas.
			'''
		)


		### PLOT 1 ###
		
		code = '''
		year_count = df.release_year.value_counts().sort_index()
		
		years_before_2020 = year_count.index < 2020
		
		year_count[years_before_2020].plot()
		'''
		st.code(code)


		year_count = self.df.release_year.value_counts().sort_index()
		years_before_2020 = year_count.index < 2020

		st.write('Ano em que foi produzido')
		st.line_chart(year_count[years_before_2020])
		
		###################


		### PLOT 2 ###

		code = '''
		from datetime import datetime
		
		# primeiramente, vamos remover todos os dados que não possuem data definida
		# depois vamos fazer o parser das datas
		dates = df.date_added\
		.dropna()\
		.apply(lambda d: datetime.strptime(d.strip(), '%B %d, %Y')) 

		dates.value_counts().sort_index().plot(ax=plt.gca())
		'''
		st.code(code)

		dates = self.df.date_added\
		.dropna()\
		.apply(lambda d: datetime.strptime(d.strip(), '%B %d, %Y')) 

		st.write('Data em que foi adicionado')
		st.line_chart(dates.value_counts().sort_index())

		###################


	def diretores_prestigiados(self):

		st.markdown('### Diretores mais prestigiados')

		st.markdown(
			'''
			Por último, podemos identificar quais os diretores que possuem mais obras no catálogo. Para isso, realizamos a contagem dos diretores. Por padrão, o `value_counts()` já ordena a série em ordem decrescente de valor. Como são muitas obras e muitos diretores, vamos nos atentar apenas aos top 10 diretores mais prestigiados
			'''
		)

		code = '''df.director.value_counts().head(10).plot(kind="bar")'''
		st.code(code)

		st.bar_chart(self.df.director.value_counts().head(10))



	def analises(self):
		
		st.markdown('## Análises')

		st.markdown('Agora que o dado está carregado e identificamos (algum)as informações importantes, podemos começar as análises')

		self.contagem_obras()
		
		self.adicoes_tempo()

		self.diretores_prestigiados()

	def render(self):

		"""Função para renderizar a pagina, note a ordem dos elementos
		"""

		self.cabeçalho()

		self.imports()
		
		self.carregar_dataset()

		self.analises()

		

		


















		