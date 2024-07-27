from flask import Flask, request, jsonify, render_template
import requests
import openai
from fpdf import FPDF

app = Flask(__name__)

API_URL = 'https://open-api.jejucodingcamp.workers.dev/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    question = data.get('question')
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]
    response = requests.post(API_URL, json=messages)
    if response.status_code == 200:
        answer = response.json().get('choices')[0]['message']['content']
    else:
        answer = 'Error: Unable to get a response from the API'
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)
