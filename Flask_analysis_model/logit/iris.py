from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
@app.route('/', methods=['GET'])
def main():
    return render_template('iris/input.html')

@app.route('/iris_result', methods=["POST"])
def iris_result():
    flowers = ['setosa', 'versicolor', 'virginica']
    model = joblib.load('d:/workspace/Python2/models/iris_logit.model')
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])
    test_set = [[a, b, c, d]] # 2차원 배열로 만들기
    n = model.predict(test_set)
    result = flowers[n[0]]
    return render_template('iris/result.html',
                           result=result, a=a, b=b, c=c, d=d)

if __name__ == '__main__':
    # 웹브라우저에서 실행할 때 http://localhost:8000 으로 하면 속도가 매우 느려지므로 http://127.0.0.1:8000으로 실행
    app.run(port=8000, threaded=False)