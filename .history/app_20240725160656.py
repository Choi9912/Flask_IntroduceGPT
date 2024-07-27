from flask import Flask, request, jsonify, render_template
import requests
import difflib
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

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    if request.method == 'POST':
        data = request.form
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Resume", ln=True, align='C')

        pdf.cell(200, 10, txt=f"Name: {data.get('name')}".encode('latin-1', 'replace').decode('latin-1'), ln=True)
        pdf.cell(200, 10, txt=f"Email: {data.get('email')}".encode('latin-1', 'replace').decode('latin-1'), ln=True)
        pdf.cell(200, 10, txt=f"Phone: {data.get('phone')}".encode('latin-1', 'replace').decode('latin-1'), ln=True)

        pdf.cell(200, 10, txt="Education:".encode('latin-1', 'replace').decode('latin-1'), ln=True)
        pdf.multi_cell(0, 10, data.get('education').encode('latin-1', 'replace').decode('latin-1'))

        pdf.cell(200, 10, txt="Experience:".encode('latin-1', 'replace').decode('latin-1'), ln=True)
        pdf.multi_cell(0, 10, data.get('experience').encode('latin-1', 'replace').decode('latin-1'))

        pdf.cell(200, 10, txt="Skills:".encode('latin-1', 'replace').decode('latin-1'), ln=True)
        pdf.multi_cell(0, 10, data.get('skills').encode('latin-1', 'replace').decode('latin-1'))

        pdf_output = 'resume.pdf'
        pdf.output(pdf_output)

        return jsonify({'result': 'success', 'pdf': pdf_output})
    return render_template('resume.html')

