from flask import Flask, Markup, render_template, request
app = Flask(__name__)

@app.route('/',methods=['GET'])
           # http://127.0.0.1:8000'/' < ''요부분
def main():
    return render_template('gugu.html')
           # 랜더링 템플릿 (화면)

@app.route('/gugu_result', methods=['POST'])
def gugu_result():
    dan = int(request.form['dan'])
              # request = Flask 내장객체
    result=''
    for i in range(1,10):
        result += f'{dan}x{i}={dan*i}<br>'
        # <br> = break line / 줄바꿈
    #html 태그를 인식하게 하는 함수
    result = Markup(result) # Markup = <br> 태그를 작동하게끔 하기위해
    return render_template('gugu_result.html', result=result)

if __name__ == '__main__':
    app.run(port=8000, threaded=False)
# threaded를 True로 설정하면 신경망 모형을 불러오는 코드에서 에러가 발생하므로 False로 설정
# thread 거미줄, 작업단위
# single thread 프로그램 하나당 작업단위 1개
# multi thread 프로그램 하나당 작업단위 여러개
#