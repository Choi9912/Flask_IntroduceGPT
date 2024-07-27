from flask import Flask, request, jsonify, render_template
import requests
import openai
from fpdf import FPDF

app = Flask(__name__)

API_URL = 'https://open-api.jejucodingcamp.workers.dev/'

# 2.3 프롬프트 최적화 기법
# 1. 이론 소개

# a) 반복적 개선 (Iterative Refinement)
# 초기 프롬프트로 시작하여 결과를 분석하고 지속적으로 개선하는 과정
# 목표: 원하는 결과에 가장 근접한 프롬프트 도출

# b) 단계별 지시 (Step-by-Step Instructions)
# 복잡한 작업을 작은 단계로 나누어 AI에게 안내
# 목표: 정확성 향상 및 논리적 흐름 유지

# c) 예시 제공 (Few-Shot Learning)
# 원하는 출력 형식의 예시를 프롬프트에 포함
# 목표: AI가 패턴을 학습하여 유사한 형식의 응답 생성

# d) 제약 조건 설정 (Constraint Setting)
# 원하지 않는 내용 제외 요청 또는 특정 조건 지정
# 목표: 더 집중적이고 관련성 높은 응답 유도

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    question = data.get('question')

    # Example implementation of Iterative Refinement
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]
    
    response = requests.post(API_URL, json=messages)
    
    # Check if the response is successful and refine the prompt if necessary
    if response.status_code == 200:
        answer = response.json().get('choices')[0]['message']['content']
    else:
        # Adding refinement by providing feedback and requesting clarification
        messages.append({"role": "user", "content": "Please clarify the previous answer."})
        response = requests.post(API_URL, json=messages)
        if response.status_code == 200:
            answer = response.json().get('choices')[0]['message']['content']
        else:
            answer = 'Error: Unable to get a response from the API'

    return jsonify({'answer': answer})

# Example implementation of Step-by-Step Instructions
def get_step_by_step_response(question):
    steps = [
        "Step 1: Analyze the question.",
        "Step 2: Break down the components of the question.",
        "Step 3: Formulate a detailed response based on the analysis."
    ]
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
        {"role": "assistant", "content": " ".join(steps)}
    ]
    response = requests.post(API_URL, json=messages)
    return response.json().get('choices')[0]['message']['content'] if response.status_code == 200 else 'Error'

# Example implementation of Few-Shot Learning
def get_few_shot_response(question):
    examples = [
        {"role": "user", "content": "What is the capital of France?", "role": "assistant", "content": "The capital of France is Paris."},
        {"role": "user", "content": "What is 2+2?", "role": "assistant", "content": "2+2 equals 4."}
    ]
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        *examples,
        {"role": "user", "content": question}
    ]
    response = requests.post(API_URL, json=messages)
    return response.json().get('choices')[0]['message']['content'] if response.status_code == 200 else 'Error'

# Example implementation of Constraint Setting
def get_constrained_response(question):
    constraints = "Please provide a brief, concise answer without any additional information."
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{question}\n{constraints}"}
    ]
    response = requests.post(API_URL, json=messages)
    return response.json().get('choices')[0]['message']['content'] if response.status_code == 200 else 'Error'

if __name__ == '__main__':
    app.run(debug=True)
