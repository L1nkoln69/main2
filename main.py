import asyncio

import aiohttp
import datetime
import requests


async def first(url, session):
    response = await session.request(method='GET', url=url)
    return await response.json()


async def main(url, session):
    result = await first(url, session)
    return int(result['team_all_season']['queryResults']['row'][0]['mlb_org_id'])


async def main2(url, session):
    result = await first(url, session)
    list_ = []
    a = 0
    for i in result['data']:
        list_.append(i['home_team_score'])
        a += i['home_team_score']
    len_i = len(list_)
    char = a // len_i
    return char


async def maxim():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[main("http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code=%27mlb%27&all_star_sw=%27N%27&sort_order=name_asc&season=%272021%27", session),
                                        main2('https://www.balldontlie.io/api/v1/games', session)])
        res = sum(result)
        len_res = len(result)
    return res/len_res


start = datetime.datetime.now()
print('Start')
print(asyncio.run(maxim()))
print("Done")
print(datetime.datetime.now() - start)
