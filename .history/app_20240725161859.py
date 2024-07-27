from flask import Flask, request, jsonify, render_template
import requests
import difflib
from fpdf import FPDF
import openai

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

@app.route('/resume', methods=['POST'])
def resume():
    data = request.get_json()
    resume_content = (
        f"이름: {data['name']}\n"
        f"이메일: {data['email']}\n"
        f"전화번호: {data['phone']}\n"
        f"학력: {data['education']}\n"
        f"경력: {data['experience']}\n"
        f"기술: {data['skills']}\n"
    )
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, resume_content.encode('latin-1', 'replace').decode('latin-1'))

    pdf_output = 'resume.pdf'
    pdf.output(pdf_output)

    return jsonify({'result': 'success', 'pdf': pdf_output})

if __name__ == '__main__':
    app.run(debug=True)