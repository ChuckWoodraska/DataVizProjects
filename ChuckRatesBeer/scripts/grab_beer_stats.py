
from chuck_pyutils import core as utils
import requests
# import pandas as pd
import urllib.parse as urllib

config = utils.read_config(utils.get_file_path(__file__, 'config.ini'))
# untappd_conn = Untappd(config['UNTAPPD']['CLIENT_ID'], config['UNTAPPD']['CLIENT_SECRET'])
# a = untappd_conn.feed('user', 'chuckwoodraska').get('response').get('checkins').get('items')
# print(a)

# api_auth = f"https://untappd.com/v4/search/beer?client_id={config['UNTAPPD']['CLIENT_ID']"
# result = requests.get(api_auth)
# print(result)
# print(result.text)


#
#
# result = requests.get(API_EP, params=kwargs).json()
# print(result)
#
# while result['response']['pagination']['next_url']:
#     for x in result['response']['checkins']['items']:
#         print(x)
#     result = requests.get(result['response']['pagination']['next_url'], params=kwargs).json()
#     print(result)

def get_search_beers(query):
    API_EP = 'https://api.untappd.com/v4/search/beer'
    kwargs = {"client_id": config['UNTAPPD']['CLIENT_ID'], "client_secret": config['UNTAPPD']['CLIENT_SECRET'],
              "q": query}
    result = requests.get(API_EP, params=kwargs).json()
    new_list = []
    for item in result["response"]["beers"]["items"]:
        new_list.append({"bid": item["beer"]["bid"], "beer_name": item["beer"]["beer_name"], "brewery_name": item["brewery"]["brewery_name"]})
    print(new_list)

get_search_beers("Guinness")

