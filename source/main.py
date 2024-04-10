# S'importen llibreries requerides
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import time


# Es crea la funció que retorna el document 'robots.txt' de la pàgina web
def get_robots_txt(page_url):
    if page_url.endswith('/'):
        path = page_url
    else:
        path = page_url + '/'
    request = requests.get(path + "robots.txt", data=None)

    return request.text


# Es crea la classe 'url_scrap' per rascar la pàgina principal
class url_scrap():
    def __init__(self,
                 user_agent):
        self.user_agent = user_agent

    def get_soup(self,
                 user_agent):
        url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

        response = requests.get(url,
                                headers={"user-agent": self.user_agent})

        # S'obté la sopa
        soup = BeautifulSoup(response.text,
                             'html.parser')

        return soup

    def get_movie(self):
        movie = self.get_soup(self.user_agent).find('ul',
                                                    class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base').find_all('li',
                                                                                                                                                                                            class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')

        return movie

    def get_movie_link(self):
        link = ['https://www.imdb.com/' + i.find('a')['href'] for i in self.get_movie()]

        return link


# Es crea la classe 'link_scrap' per rascar les pàgines d'interès
class link_scrap():
    def __init__(self,
                 link,
                 user_agent):
        self.link = link
        self.user_agent = user_agent

    def get_movie_soup(self,
                       link,
                       user_agent):
        response = requests.get(self.link,
                                headers={"user-agent": self.user_agent})
        movie_soup = BeautifulSoup(response.text,
                                   'html.parser')

        return movie_soup

    # Es defineixen les funcions d'extracció de dades

    def get_title(self):
        try:
            title_text = self.get_movie_soup(self.link,
                                             self.user_agent).find('div',
                                                                   class_='sc-d8941411-1 fTeJrK').text
        except Exception:
            title_text = self.get_movie_soup(self.link,
                                             self.user_agent).find('span',
                                                                   class_='hero__primary-text').text

        return title_text

    def get_genre(self):
        try:
            genre_list = [i.text for i in self.get_movie_soup(self.link,
                                                              self.user_agent).find_all('a',
                                                                                        class_='ipc-chip ipc-chip--on-baseAlt')]
            genre_text = ', '.join(genre_list)

        except Exception:
            genre_text = 'NA'

        return genre_text

    def get_year(self):
        try:
            year_text = self.get_movie_soup(self.link,
                                            self.user_agent).find('ul',
                                                                  class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt').find_all('li',
                                                                                                                                                                 class_='ipc-inline-list__item')[0].text

        except Exception:
            year_text = 'NA'

        return year_text

    def get_classification(self):
        try:
            classification_text = self.get_movie_soup(self.link,
                                                      self.user_agent).find('ul',
                                                                            class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt').find_all('li',
                                                                                                                                                                           class_='ipc-inline-list__item')[1:-1][0].text

        except Exception:
            classification_text = 'NA'

        return classification_text

    def get_duration(self):
        try:
            duration_text = self.get_movie_soup(self.link,
                                                self.user_agent).find('ul',
                                                                      class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt').find_all('li',
                                                                                                                                                                     class_='ipc-inline-list__item')[-1].text

        except Exception:
            duration_text = 'NA'

        return duration_text

    def get_rating(self):
        try:
            rating_text = self.get_movie_soup(self.link,
                                              self.user_agent).find('span',
                                                                    class_='sc-bde20123-1 cMEQkK').text
        except Exception:
            rating_text = 'NA'

        return rating_text

    def get_review(self):
        try:
            review_text = self.get_movie_soup(self.link,
                                              self.user_agent).find('div',
                                                                    class_='sc-bde20123-3 gPVQxL').text
        except Exception:
            review_text = 'NA'

        return review_text

    def get_director(self):
        try:
            director_text = self.get_movie_soup(self.link,
                                                self.user_agent).find('a',
                                                                      class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text
        except Exception:
            director_text = 'NA'

        return director_text

    def get_budget(self):
        try:
            budget_text = self.get_movie_soup(self.link,
                                              self.user_agent).find_all('span',
                                                                        class_='ipc-metadata-list-item__list-content-item')[2].text
        except Exception:
            budget_text = 'NA'

        if 'estimated' not in budget_text:
            budget_text = 'NA'

        return budget_text

    def get_collection(self):
        try:
            collection_text = self.get_movie_soup(self.link,
                                                  self.user_agent).find_all('span',
                                                                            class_='ipc-metadata-list-item__list-content-item')[-2].text
        except Exception:
            collection_text = 'NA'

        if ('$' not in collection_text) | ('estimated' in collection_text):
            collection_text = 'NA'

        return collection_text


# Es crea la funció que recopila les dades i retorna un DataFrame
def get_top250_movies(user_agent_list):
    # Es comprova que l'extracció de dades és permesa
    # pel propietàri de la pàgina web
    page_url = 'https://www.imdb.com/'
    print(get_robots_txt(page_url))

    # El web scraping aplicat en aquesta pràctica és permès

    user_agent = user_agent_list[0]

    url_instance = url_scrap(user_agent)

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

        if k > 125:
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
    return pd.DataFrame(dict(Title=titles,
                             Genre=genres,
                             Year=years,
                             Classification=classifications,
                             Duration=durations,
                             Rating=ratings,
                             Review=reviews,
                             Director=directors,
                             Budget=budgets,
                             Collection=collections))
