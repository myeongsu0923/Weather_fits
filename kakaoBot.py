from src.Weather import *
from src.searchObject import *
from flask import Flask, request, jsonify

kakaoBot = Flask(__name__)

global outputFits #복장 목록
global outputDust
global outputSun
outputFits = ""
outputDust = ""
outputSun = ""

@kakaoBot.route("/")
def hello():
    return "Hello goorm!"

@kakaoBot.route("/weather",methods=['POST'])
def weatherPrint():
    req = request.get_json()
        
    location = req["action"]["detailParams"]["sys_location"]["value"]	# json파일 읽기
    
    temp = Weather(location)
    
    answer = temp.getWeather()
    
    global outputDust
    outputDust = "[미세먼지 수치]\n"
    outputDust += temp.getDust()
    
    global outputSun
    outputSun = "[자외선]\n"
    outputSun += temp.getSunlight()
    
    global outputFits
    outputFits = "[오늘 기온에 맞는 옷 추천]\n"
    for fits in temp.getFits():
        outputFits += fits.replace('"','').strip() + "\n"
    
    #https://img.freepik.com/free-vector/clothes-cartoon_119631-167.jpg 카드 이미지
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                },
                {
        "basicCard": {
          "title": "오늘의 추천 복장은?",
          "thumbnail": {
            "imageUrl": "https://img.freepik.com/free-vector/clothes-cartoon_119631-167.jpg"
          },
          "buttons": [
            {
              "action": "message",
              "label": "옷 추천 목록 보기",
              "messageText": "옷 추천"
            }
          ]
        }
      }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

@kakaoBot.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']['utterance'] #사용자 발화값 받아오기
    content=content.replace("\n","")
    
    global outputFits
    global outputDust
    global outputSun
    
    if content.find("옷") != -1 or content.find("외출복") != -1 or content.find("복장") != -1:
        content = "옷"
    
    if content == u"편의점":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
        "listCard": {
          "header": {
            "title": "대구대 근처 편의점"
          },
          "items": [
            {
              "title": stores[0][0],
              "description": stores[0][1],
              "link": {
                "web": stores[0][2]
              }
            }
          ],
        }
      }
                ]
            }
        }
        return jsonify(dataSend)
    
    if outputFits == "" or outputDust == "" or outputSun == "":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "지역이름을 먼저 검색해주세요"
                        }
                    }
                ]
            }
        }
        return jsonify(dataSend)
    
    if content == u"미세먼지":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : outputDust
                        }
                    }
                ]
            }
        }
        return jsonify(dataSend)
    
    if content == u"자외선":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : outputSun
                        }
                    }
                ]
            }
        }
        return jsonify(dataSend)
    
    if content == u"옷":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : outputFits
                        }
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "error입니다."
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    kakaoBot.run(host="0.0.0.0", port=5000, threaded=True)
