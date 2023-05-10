from flask import Flask, render_template, request
from statsmodels.regression.linear_model import OLSResults

app = Flask(__name__)

@app.route('/', methods=['GET'])
# @ = at, at app
# .route(url patten, method)
# method = GET
#          POST
#          PUT
#          DELETE
def main():
    return render_template('ozone/input.html')

@app.route('/result', methods=['POST'])
def result():
    model = OLSResults.load("d:/workspace/Python2/models/ozone_regress.model")
            # 미리 저장된 회귀분석 모형 불러오기
    a = float(request.form['a'])
                    # form에서 전달된 값은 str이므로 변환이 필요하면 변환해야한다.
    b = float(request.form['b'])
    c = float(request.form['c'])
    test_set = [a, b, c] # 1차원 배열로 변경
    ozone = model.predict(test_set)
    return render_template('ozone/result.html', ozone = '{:.2f}'.format(ozone[0]), a=a, b=b, c=c)
        #  render_template 패이지를 출력해라                출력형식.format(출력값)

if __name__ == '__main__':
            # '__main__' = 현재 파일에서 실행한 경우.
    app.run(port=8080, threaded=False)