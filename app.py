from flask import Flask, render_template
# クイズ2用
# import requests
# import random
import os

app = Flask(__name__)

quiz_answer=os.getenv("TEST")
print(quiz_answer)

@app.route('/')
def index():
    if quiz_answer=="correct":
        return render_template("yes.html")
    else:
        return render_template("no.html")

# クイズ2用
# @app.route('/omikuji')
# def omikuji():
#     num = random.randint(1, 3)
#     result = {1: "大吉", 2: "中吉", 3: "凶"}[num]
#     return f"<h1>今日の運勢は {result}！</h1>"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)

# クイズ3用
# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0', port=5000)