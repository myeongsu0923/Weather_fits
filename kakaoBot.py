from Weather import *
from flask import Flask, request, jsonify

kakaoBot = Flask(__name__)

@kakaoBot.route("/")
def hello():
    return "Hello goorm!"

@kakaoBot.route("/weather",methods=['POST'])
def weatherPrint():
    req = request.get_json()
    
    location = req["action"]["detailParams"]["sys_location"]["value"]	# json파일 읽기
    
    temp = Weather(location)
    
    answer = temp.getWeather()
    
    outputFits = "==== 오늘 기온에 맞는 옷 추천 ====\n"
    for fits in temp.getFits():
        outputFits += fits.replace('"','').strip() + "\n"
    
    answerFits = outputFits
    
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
                    "simpleText": {
                        "text": answerFits
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

if __name__ == "__main__":
    kakaoBot.run(host="0.0.0.0", port=5000, threaded=True)