# Trabalho 3: Sistemas de Recomendação

## Objetivo

Neste trabalho você deve implementar um Sistema de Recomendação (SR) com [Filtragem Colaborativa](https://en.wikipedia.org/wiki/Collaborative_filtering) Baseada em Memória que recomenda __notícias__ para um usuário.

## Dataset

O dataset utilizado é composto por 2 arquivos:

* `viewed_news.csv`: cada linha desse arquivo é uma interação de leitura do usuário com uma notícia. O formato de cada linha desse aquivo é: `<id do usuário>|<id da notícia>`.
* `news_data.json`: cada linha desse arquivo é um JSON que contém as informações sobre uma notícia. O formato de cada linha desse aquivo é: `{"id": <id da notícia>, "url": <url da notícia>, "title": <manchete da notícia>}`.

> O segundo arquivo é mais para fins de visualização, caso você deseje visualizar as recomendações.

## Descrição geral

Seu sistema de recomendação deve possuir uma função `F` que recebe um usuário `u` (id do usuário) e retorna um conjunto de notícias `Ru` (ids das notícias) de tamanho __k__.

__Dica__: A ideia desse SR é muito semelhante a do exemplo dado na [aula de Sistemas de Recomendação](https://github.com/ARiDa/data-science-cookbook/tree/master/recommendation-systems).


## Avaliação de Resultados

Para testar seu SR, separe __1/3__ da notícias lida por um usuário para __teste__ e __2/3__ para __treino__ (isso para todos os usuários que se encontram no dataset).

Chame `F` para cada usuário do dataset, passando como __k__ o tamanho da lista de teste do usuário (__1/3__ das notícias lidas por ele). 

Seja `Tu` o conjunto de teste do usuário `u`. Seja `Ru` o conjunto recomendado por `F` para `u`. A partir desses dois cojuntos obtemos o __índice de precisão__ `Pu` para o usuário `u` como sendo: `| Tu & Ru | / | Tu |`.

> O operador `| |` é o tamanho do conjunto. 

> O operador `&` é interseção entre dois conjuntos.

O __índice de precisão geral__ do seu SR é a média dos `Pu` do usuários, obtida por: `(Pui + Puj + Puk ... + Puz) / |V| `. Sendo `V` o conjunto de usuários e `|V|` o seu tamanho.

## Melhorias

Muitas mudanças podem alterar os resultados das recomendações:

* Verifique qual a melhor [medida de similaridade](https://reference.wolfram.com/language/guide/DistanceAndSimilarityMeasures.html) que podem ser usada nesse SR.
* O que acontece se omitirmos usuários com __poucas__ notícias lidas (outliers)?
* O que acontece se omitirmos usuários com __muitas__ notícias lidas (outliers)?
* Você usou uma Filtragem Colaborativa Usuário-Item ou Item-Item?

Na entrega, disserte um pouco sobre os porquês que você optou por uma determinada abordagem.  

## Entrega

Você deve entregar um jupyter notebook contendo todo o fluxo de definições (métodos e classes, se usá-las) e de execução do sistema de recomendação, desde a leitura e preparação do dataset até a exibição do índice de precisão geral do SR.

Bom trabalho!
