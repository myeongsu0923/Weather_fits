from regex import R
import requests
from bs4 import BeautifulSoup
import re
import csv

class Weather():
    session = requests.Session() 
    addr = "https://weather.naver.com/today/"
    addrAir = "https://weather.naver.com/air/"
    addrSun = 'https://search.naver.com/search.naver?query='
    map_cityNum = {}
    temp_wearingFits = list()

    with open('csv/cityNumber.csv', mode='r', encoding="utf-8") as citys:
        reader = csv.reader(citys)
        map_cityNum = {rows[0]:rows[1].replace('"','').strip() for rows in reader}

    with open('csv/wearing.csv', mode='r', encoding="utf-8") as clothes:
        reader = csv.reader(clothes)
        temp_wearingFits = list(reader)

    def __init__(self, area):
        self.session.encoding = 'utf-8'
        self.area = area
        self.addr += self.map_cityNum[area]
        self.addrAir += self.map_cityNum[area]
        self.addrSun += area + '날씨'
        self.tempResult = None
        self.dustResult = None
        self.sunResult = None
        self.fits = list()

        self.tempSearch()
        self.dustSearch()
        self.sunLight()
    
    def tempSearch(self):
        req = self.session.get(self.addr)
        soup = BeautifulSoup(req.text, 'html.parser')
        location = soup.find(class_='location_name')
        table = soup.find(class_="week_list")
        currentWeather = soup.find(class_='weather')
        t_ary = list(table.stripped_strings)

        self.tempResult = ("[" + self.area + "(" + location.text + ")" + " 날씨 검색 결과]\n" 
            + "오전 - " + t_ary[11][:-1] + "℃ (" + t_ary[5] + ", 강수확률 : " + t_ary[4] + ")\n"
            + "오후 - " + t_ary[14][:-1] + "℃ (" + t_ary[6] + ", 강수확률 : " + t_ary[9] + ")\n"
            + "현재 날씨상태 - " + currentWeather.text + self.umbrella(currentWeather.text))

        self.fits = self.todayRecommandFits(t_ary)

    def dustSearch(self):
        reqAir = self.session.get(self.addrAir)
        soupAir = BeautifulSoup(reqAir.text, "html.parser")
        air = soupAir.find(class_='top_area')
        t_aryAir = list(air.stripped_strings)

        self.dustResult =  ("미세먼지 - " + t_aryAir[15] + "㎍/㎥ (" + t_aryAir[16] + ")\n"
                            + "초미세먼지 - " + t_aryAir[32] + "㎍/㎥ (" + t_aryAir[33] + ")\n")


    def sunLight(self):
        reqSun = self.session.get(self.addrSun)
        soup = BeautifulSoup(reqSun.text, 'html.parser')
        sunlight = soup.find(class_="today_chart_list")
        s_ary = list(sunlight.stripped_strings)

        self.sunResult = s_ary[5]

    def umbrella(self, currentWeather):
        if currentWeather == '비':
            return "\n*비오니깐 우산챙겨요!"
        else:
            return "\n*우산이 필요없을거 같아요!"

    def todayRecommandFits(self, t_ary):
        fits = list()
        avr = (int(t_ary[11][:-1]) + int(t_ary[14][:-1])) / 2

        if (avr >= 28.0):
            fits = self.temp_wearingFits[0]
        elif (avr >= 23.0):
            fits = self.temp_wearingFits[1]
        elif (avr >= 20.0):
            fits = self.temp_wearingFits[2]
        elif (avr >= 17.0):
            fits = self.temp_wearingFits[3]
        elif (avr >= 12.0):
            fits = self.temp_wearingFits[4]
        elif (avr >= 9.0):
            fits = self.temp_wearingFits[5]
        elif (avr >= 5.0):
            fits = self.temp_wearingFits[6]
        elif (avr >= 1.0):
            fits = self.temp_wearingFits[7]
        else:
            fits = self.temp_wearingFits[8]
        
        return fits

    def getWeather(self):
        if not self.tempResult:
            return "잘못된 도시명입니다"
        return self.tempResult

    def getFits(self):
        if not self.fits:
            return "기온이 잘못되었습니다."
        return self.fits

    def getDust(self):
        if not self.dustResult:
            return "잘못된 입력입니다"
        return self.dustResult

    def getSunlight(self):
        if not self.sunResult:
            return "잘못된 입력입니다"
        return self.sunResult