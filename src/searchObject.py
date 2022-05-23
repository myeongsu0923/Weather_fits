import requests
import re

api_key = 'b57c89bcdaa776e98f2de85501de1a4b'
totals = list()

def storeSearch(region):
    page_num = 1
    region += '주변 편의점'
    placeName = list()
    placeAddr = list()
    placeUrl = list()
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': region,'page': page_num,'category_group_code' : 'CS2'}
    headers = {"Authorization": "KakaoAK " + api_key}
    places = requests.get(url, params=params, headers=headers).json()['documents']
    
    for i in range(0, 3):
        placeName.append(places[i]['place_name'])
        placeAddr.append(places[i]['address_name'])
        placeUrl.append(places[i]['place_url'])

    total = list(zip(placeName, placeAddr, placeUrl))

    return total

# * testing
stores = storeSearch('대구대학교 정문')

j = 0

for store in stores:
    for i in store:
        print(j, i)
        j = j + 1
    print("\n")