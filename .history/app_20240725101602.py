from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API Key 설정
openai.api_key = 'https://open-api.jejucodingcamp.workers.dev/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    question = data.get('question')
    
    # OpenAI API를 통해 답변 생성
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
