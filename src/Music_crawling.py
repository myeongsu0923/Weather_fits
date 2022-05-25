from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests

session = requests.Session() 
session.encoding = 'utf-8'
driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
url = 'https://www.youtube.com/c/%ED%84%B0%EB%8B%9D%ED%8F%AC%EC%9D%B8%ED%8A%B8music7/videos'
video = 'https://www.youtube.com'

file = open('music_link.txt', 'w')
driver.get(url)
req = session.get(url)
driver.maximize_window()

body = driver.find_element_by_tag_name('body')

num_of_pagedowns = 20
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_pagedowns -= 1

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
music = soup.find('div', id='items', class_="style-scope ytd-grid-renderer")
links = music.find_all('a') # 모든 a 태그 추출
cell_line = []
for i in links:
    href = i['href']
    cell_line.append(href)

cell_set = set(cell_line)

for i in cell_set:
    file.write(video+i+"\n")

file.close()
driver.close()
