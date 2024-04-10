# S'importen llibreries request i BeautifulSoup
import requests
from bs4 import BeautifulSoup

# Es crea la funció que retorna el document 'robots.txt' de la pàgina web
def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    request = requests.get(path + "robots.txt", data=None)

    return request.text


# Es crea la classe 'url_scrap' per rascar la pàgina principal
class url_scrap():
    def __init__(self,
                 url,
                 user_agent):
        self.url = url
        self.user_agent = user_agent

    def get_soup(self,
                 url,
                 user_agent):
        response = requests.get(self.url,
                                headers={"user-agent": self.user_agent})

        # S'obté la sopa
        soup = BeautifulSoup(response.text,
                             'html.parser')

        return soup

    def get_movie(self):
        movie = self.get_soup(self.url,
                              self.user_agent).find('ul',
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
