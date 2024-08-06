import requests
import pandas as pd
import json

api_key = "69e0d756f57f03c3427c9622298bc4dc"
url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}"

data = requests.get(url)

starwars_url = url + "&query=Star%20Wars"

starwars_data = requests.get(starwars_url)
starwars_data.content

starwars_df = pd.DataFrame(starwars_data.json()['results'])

starwars_df.sort_values(by='popularity', ascending=False)