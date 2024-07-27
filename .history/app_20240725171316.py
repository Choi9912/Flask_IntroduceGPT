from flask import Flask, request, jsonify, render_template
import requests
import openai
from fpdf import FPDF

app = Flask(__name__)

API_URL = 'https://open-api.jejucodingcamp.workers.dev/'


@app.route('/')
def index():
    return render_template('resume.html')

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
@app.route('/check_similarity', methods=['POST'])
def check_similarity():
    data = request.get_json()
    text1 = data.get('text1')
    text2 = data.get('text2')
    similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
    return jsonify({'similarity': similarity_ratio})

@app.route('/check_spelling', methods=['POST'])
def check_spelling():
    data = request.get_json()
    text = data.get('text')
    response = requests.post('http://speller.cs.pusan.ac.kr/results', data={'text1': text})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('td', class_='tdReplace')
        corrections = []
        for result in results:
            original = result.find('span', class_='tdText').text
            corrected = result.find('a').text
            corrections.append(f"{original} -> {corrected}")
        return jsonify({'corrections': corrections})
    else:
        return jsonify({'error': 'Unable to check spelling'}), 500

if __name__ == '__main__':
    app.run(debug=True)
