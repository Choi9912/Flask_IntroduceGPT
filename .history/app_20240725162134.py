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

@app.route('/resume', methods=['POST'])
def resume():
    data = request.get_json()
    messages = [
        {"role": "system", "content": "Create a professional resume."},
        {"role": "user", "content": (
            f"Name: {data['name']}\n"
            f"Email: {data['email']}\n"
            f"Phone: {data['phone']}\n"
            f"Education: {data['education']}\n"
            f"Experience: {data['experience']}\n"
            f"Skills: {data['skills']}\n"
        )}
    ]
    response = requests.post(API_URL, json=messages)
    if response.status_code == 200:
        resume_text = response.json()['choices'][0]['message']['content'].strip()
    else:
        return jsonify({'error': 'Unable to get a response from the API'}), 500

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, resume_text.encode('latin-1', 'replace').decode('latin-1'))

    pdf_output = 'resume.pdf'
    pdf.output(pdf_output)

    return jsonify({'result': 'success', 'pdf': pdf_output})

if __name__ == '__main__':
    app.run(debug=True)
