import requests
import pandas as pd
import json

api_key = "69e0d756f57f03c3427c9622298bc4dc"
url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}"

data = requests.get(url)

starwars_url = url + "&query=Star%20Wars"

starwars_data = requests.get(starwars_url)
total_pages = starwars_data.json()['total_pages']

all_starwars = []
for page_num in range(total_pages):
    page_url = starwars_url + f"&page={page_num+1}"
    get_request = requests.get(page_url)
    allswjson = get_request.json()['results']
    all_starwars += (allswjson)

allswdf = pd.DataFrame(all_starwars)
allswdf.sort_values(by='popularity', ascending=False)