# Pràctica 1 - Tipologia i Cicle de Vida de les Dades

Assignatura: M2.851 / Semestre: 2024-2 / Data: 16-04-2024

## Autors
  * Eric Farran Moreno - [efarran0@uoc.edu](efarran0@uoc.edu)
  * Jordi Alvarez Pitarque - [jalvarezpit@uoc.edu](jalvarezpit@uoc.edu)

## Portal web escollit
[https://www.imdb.com/chart/top/?ref_=nv_mv_250](https://www.imdb.com/chart/top/?ref_=nv_mv_250)

## Enllaç DOI Zenodo
El dataset ha estat publicat en Zenodo amb DOI [10.5281/zenodo.0000000](https://doi.org/10.5281/zenodo.0000000).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.0000000.svg)](https://doi.org/10.5281/zenodo.0000000)

## Descripció del repositori
  * `/source/main.py`: Arxiu principal.
  * `/source/scraper.py`: Arxiu executor.
  * `/source/requirements.txt`: Llistat de paquets utilitzats (Python 3.11.7).
  * `/dataset/data.csv`: Dataset generat en format csv.

## Instruccions
El programa main.py inclou totes les classes i funcions utilitzades en l'arxiu executor.
Per a generar el dataset cal assignar en l'arxiu executor un llistat de 2 users-agents a elecció pròpia com a paràmetre de la funció get_top250_movies de main.py.

***
**Exemple**

from main import get_top250_movies

user_agent_list = [user_agent_1, user_agent_2]

data = get_top250_movies(user_agent_list)
