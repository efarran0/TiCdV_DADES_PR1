# S'importa la classe collector de main i la llibreria os
from main import get_top250_movies
import os

# Es defineix user_agent_list
user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36']

# S'obté la data
data = get_top250_movies(user_agent_list)

# Es remou el csv antic en cas d'existir
if os.path.exists('data.csv'):
    os.remove('data.csv')

# S'exporta data en format csv
data.to_csv('data.csv', index=False)
