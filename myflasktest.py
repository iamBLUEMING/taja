import time
import flask
from flask import Flask, render_template, request, jsonify
from colorama import init, Fore, Style

init()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/typing-result', methods=['POST'])
def typing_result():
    data = request.get_json()
    input_text = data['inputText']

    string = "dong hae mul ga bek du san yi ma lu go dal do luok ha nu nim me bo wu ha sa wu li nala maen sae"
    string2 = "mu gung hua saem chull li huaa lveae gwuang sann"
    string3 = "daehan saramm dae hann wuu lo gatt chee bo zhun ha saee"
    word_count = len(string.split()) + len(string2.split()) + len(string3.split())

    t0 = time.time()  # 계산기 시작
    acc = len(set(input_text.split()) & set(string.split()))
    accuracy = acc / word_count
    t1 = time.time()  # 스톱!
    time_taken = t1 - t0
    word_per_minute = (word_count / time_taken) * 60

    result = {
        'wpm': word_per_minute,
        'accuracy': accuracy
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run()
