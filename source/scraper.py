# S'importen les classes de main, la llibreria pandas, time, numpy i os
from main import get_robots_txt, url_scrap, link_scrap
import pandas as pd
import time
import numpy as np
import os

# Es comprova que l'extracció de dades és permesa
# pel propietàri de la pàgina web
print(get_robots_txt('https://www.imdb.com/'))

# El web scraping aplicat en aquesta pràctica és permès

# Es defineixen els paràmetres inicials
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36']

url_instance = url_scrap(url,
                         user_agent_list[0])

# Es creen les llistes per emmagatzemar dades
titles = []
genres = []
years = []
classifications = []
durations = []
ratings = []
reviews = []
directors = []
budgets = []
collections = []

# Es cerquen les direccions webs a les pel·lícules requerides
k = 0
for link in url_instance.get_movie_link():

    k += 1

    if k <= 125:
        user_agent = user_agent_list[0]
    else:
        user_agent = user_agent_list[1]

    link_instance = link_scrap(link,
                               user_agent)

    # S'emmagatzemen les dades
    
    film = link_instance.get_title()
    print('{} <started>'.format(film))

    titles.append(film)
    print('{} <1/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    genres.append(link_instance.get_genre())
    print('{} <2/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    years.append(link_instance.get_year())
    print('{} <3/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    classifications.append(link_instance.get_classification())
    print('{} <4/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    durations.append(link_instance.get_duration())
    print('{} <5/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    ratings.append(link_instance.get_rating())
    print('{} <6/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    reviews.append(link_instance.get_review())
    print('{} <7/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    directors.append(link_instance.get_director())
    print('{} <8/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    budgets.append(link_instance.get_budget())
    print('{} <9/10>'.format(film))
    time.sleep(np.random.normal(1, 0.2))

    collections.append(link_instance.get_collection())
    print('{} <finished>\n'.format(film))
    time.sleep(np.random.normal(2, 0.3))

# Es construeix el dataframe a partir de les llistes
data = pd.DataFrame(dict(Title=titles,
                         Genre=genres,
                         Year=years,
                         Classification=classifications,
                         Duration=durations,
                         Rating=ratings,
                         Review=reviews,
                         Director=directors,
                         Budget=budgets,
                         Collection=collections))

# Es remou el csv antic en cas d'existir
if os.path.exists('data.csv'):
    os.remove('data.csv')

# S'exporta data en format csv
data.to_csv('data.csv', index=False)
