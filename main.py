import json
import os
import re
import datetime
import requests

from bs4 import BeautifulSoup
from termcolor import colored


site_url = 'https://www.balldontlie.io/api/v1/games'


def first():
    res = (requests.get(site_url)).json()
    res2 = (requests.get('https://weatherstack.com/')).text
    list_ = []
    a = 0
    for i in res['data']:
        list_.append(i['home_team_score'])
        a += i['home_team_score']
    len_i = int(len(list_))
    char = a//len_i
    print(res2)
    return char


start = datetime.datetime.now()
print('Start')
# asyncio.run(main(SITE, TAG, datetime.datetime.now().strftime('%Y-%m-%d')))
print(first())
print("Done")
print(datetime.datetime.now() - start)
