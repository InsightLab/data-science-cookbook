# Trabalho 3: Sistemas de Recomendação

Neste trabalho você deve implementar um Sistema de Recomendação com [Filtragem Colaborativa](https://en.wikipedia.org/wiki/Collaborative_filtering) Baseado em Memória.

O dataset utilizado é composto por 2 arquivos:
* `viewed_news.csv`: cada linha desse arquivo é uma interação _usuário U viu a notícia N_. O formato de cada linha desse aquivo é: `<id do usuário>|<id da notícia>`.
* `news_data.json`: cada linha desse arquivo é um JSON que contém as informações sobre uma notícia. O formato de cada linha desse aquivo é: `{"id": <id da notícia>, "url": <url da notícia>, "title": <manchete da notícia>}`.

> O segundo arquivo é mais para fins de visualização, caso você deseje visualizar as recomendações.

