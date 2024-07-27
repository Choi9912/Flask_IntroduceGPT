from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# API URL 설정
API_URL = 'https://open-api.jejucodingcamp.workers.dev/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    question = data.get('question')

    # API 요청 보내기
    response = requests.post(API_URL, json={"query": question})
    if response.status_code == 200:
        answer = response.json().get('answer', 'No answer available')
    else:
        answer = 'Error: Unable to get a response from the API'
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
