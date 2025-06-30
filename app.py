from flask import Flask, render_template
import os

app = Flask(__name__)

quiz_answer=os.getenv("TEST")
print(quiz_answer)

@app.route('/')
def index():
    if quiz_answer=="correct":
        return render_template("index.html")
    else:
        return render_template("no.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)