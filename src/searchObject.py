import requests
import random

# 편의점 추천 사용중단. 
# api_key = 'api_key입력'
# totals = list()

# def storeSearch(region):
#     page_num = 1
#     region += '주변 편의점'
#     placeName = list()
#     placeAddr = list()
#     placeUrl = list()
#     url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
#     params = {'query': region,'page': page_num,'category_group_code' : 'CS2'}
#     headers = {"Authorization": "KakaoAK " + api_key}
#     places = requests.get(url, params=params, headers=headers).json()['documents']
    
#     for i in range(0, 3):
#         placeName.append(places[i]['place_name'])
#         placeAddr.append(places[i]['address_name'])
#         placeUrl.append(places[i]['place_url'])

#     total = list(zip(placeName, placeAddr, placeUrl))

#     return total


def musicSearch():
    with open('src/music_link.txt', mode='r', encoding="utf-8") as musics:
        music = list(musics)
    
    recommandMusic = random.choice(music)

    return recommandMusic


#testing
#print(musicSearch())
#print(musicSearch())
