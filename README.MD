# - 날씨 데이터를 통한 기온별 옷 추천 챗봇
아래와 같은 사진을 참고하여 카카오톡 오픈빌더를 통해 날씨 데이터를 수집하여<br>
지역별 기온 및 미세먼지와 이를 토대로 기온별 옷 추천해주는 카카오톡 챗봇입니다.

<img src="https://user-images.githubusercontent.com/102271691/170249520-1e02dc87-fe2a-4c02-b35b-adda3add7c44.jpg" width="300" height="450"/>

## - 정보

### 🔑채널 정보 - 카카오톡 플러스친구 : Weather_Fits
카카오톡 플러스친구를 추가하면 됩니다.

<img src="https://user-images.githubusercontent.com/102271691/170246089-b6c7d412-60d2-4d75-b606-13d74ff734c6.jpg" width="300" height="400"/>

### 주요 기능
1. 🌡 지역 날씨 정보
2. ☔ 우산 필요 유무
3. 😷 미세먼지 정보
4. 👕 기온별 옷 추천 정보
5. 🎶 노래 추천

### 테스트 화면
<img src="https://user-images.githubusercontent.com/102271691/170258939-e1626c5b-c21b-4e8f-9bc1-13f24ba3d6ca.jpg" width="300" height="500"/>
<br>
도움말이 필요할땐 "도움"을 입력하면 됨.

## 📜봇 & 서버 테스트
**개발 환경**
- Server : Ubuntu 18.04 LTS
- IDE : goorm, Visual Studio Code
- Web Framework : flask
- languages : python

### 사전 설치 프로그램

    $ git clone https://github.com/myeongsu0923/Weather_fits.git
    $ pip install -r requirements.txt

### 웹 서버 실행
    $ cd Weather_fits
    $ python kakaoBot.py

