from flask import Flask, request, jsonify, render_template
import requests
import logging
from flask_cors import CORS


# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)  
class SelfIntroductionAnalyzer:
    def __init__(self, api_url):
        self.api_url = api_url

    def analyze(self, introduction, method):
        if method == 'iterative_refinement':
            return self.iterative_refinement(introduction)
        elif method == 'step_by_step':
            return self.step_by_step(introduction)
        elif method == 'few_shot':
            return self.few_shot(introduction)
        elif method == 'constraint_setting':
            return self.constraint_setting(introduction)
        else:
            return 'Error: Invalid method'

    def iterative_refinement(self, introduction):
        return self.send_request(self.create_messages(introduction))

    def step_by_step(self, introduction):
        steps = [
            "단계 1: 자기소개서를 분석합니다.",
            "단계 2: 주요 포인트와 주제를 식별합니다.",
            "단계 3: 구조와 일관성을 평가합니다."
        ]
        messages = self.create_messages(introduction, " ".join(steps))
        return self.send_request(messages)

    def few_shot(self, introduction):
        examples = [
            {"role": "user", "content": "자기소개서의 강점을 분석해주세요.", "role": "assistant", "content": "자기소개서의 강점은 명확한 목표 설정과 구체적인 경험 사례입니다."},
            {"role": "user", "content": "자기소개서에서 개선할 점을 알려주세요.", "role": "assistant", "content": "자기소개서의 개선할 점은 내용의 일관성과 논리적 흐름입니다."}
        ]
        messages = self.create_messages(introduction, examples=examples)
        return self.send_request(messages)

    def constraint_setting(self, introduction):
        constraints = "최대한 자세하게 알려주세요."
        messages = self.create_messages(introduction, constraints)
        return self.send_request(messages)

    def create_messages(self, introduction, additional_content="", examples=None):
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 분석하는 AI입니다."},
            {"role": "user", "content": f"다음 자기소개서를 분석해주세요: {introduction} {additional_content}"}
        ]
        if examples:
            messages = [{"role": ex["role"], "content": ex["content"]} for ex in examples] + messages
        return messages

    def send_request(self, messages):
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in SelfIntroductionAnalyzer: {e}")
            return 'Error: Unable to get a response from the API'


class SelfIntroductionWriter:
    def __init__(self, api_url):
        self.api_url = api_url

    def write(self, prompt, method):
        if method == 'iterative_refinement':
            return self.iterative_refinement(prompt)
        elif method == 'step_by_step':
            return self.step_by_step(prompt)
        elif method == 'few_shot':
            return self.few_shot(prompt)
        elif method == 'constraint_setting':
            return self.constraint_setting(prompt)
        else:
            return 'Error: Invalid method'

    def iterative_refinement(self, prompt):
        return self.send_request(self.create_messages(prompt))

    def step_by_step(self, prompt):
        steps = [
            "단계 1: 지시사항을 이해합니다.",
            "단계 2: 포함할 주요 포인트를 식별합니다.",
            "단계 3: 논리적인 흐름으로 자기소개서를 작성합니다."
        ]
        messages = self.create_messages(prompt, " ".join(steps))
        return self.send_request(messages)

    def few_shot(self, prompt):
... (191줄 남음)
접기
app.py
14KB
document.addEventListener('DOMContentLoaded', function() {
    const sendBtn = document.getElementById('sendBtn');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const plagiarismBtn = document.getElementById('plagiarismBtn');
    const spellCheckBtn = document.getElementById('spellCheckBtn');
    const actionBtn = document.getElementById('actionBtn');
확장
script.js
5KB
깃에 커밋하려했는데 살짝 이슈있어서 좀 걸릴거같아서 파일로 드리겠습니당..
초원범 — 오늘 오전 10:44
html도 부탁드립니다 ㅎㅎ
최규성 — 오늘 오전 10:44
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Q&A</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
확장
index.html
1KB
초원범 — 오늘 오전 10:46
전체프로젝트 압축해서 주시겠어요?
최규성 — 오늘 오전 10:46
https://github.com/Choi9912/Flask_GPTapi
GitHub
GitHub - Choi9912/Flask_GPTapi
Contribute to Choi9912/Flask_GPTapi development by creating an account on GitHub.
GitHub - Choi9912/Flask_GPTapi
깃허브 올렸습니다!
초원범 — 오늘 오전 10:51
84번째 줄에있는 해당 조건식은 무엇을 위한것인가요

data.plagiarism_report && Array.isArray(data.plagiarism_report)
data.plagiarism_report 값은 문자열로 오는데 문자열이 아니면 무조건 no report로 나오게 되어있네요
최규성 — 오늘 오전 10:54
아하...
이게 수정수정하면서  이부분을 수정못한 거 같습니다
초원범 — 오늘 오전 10:54
아하 그렇군요
저부분만 만지면 잘될것 같네요 ㅎㅎㅎ
최규성 — 오늘 오전 10:55
앗 넵 감사합니다
오.. 됐습니다 감사합니다~
초원범 — 오늘 오전 11:01
굿입니다 🙂
초원범 — 오늘 오후 12:34
혹시 질문주신 공개페이지가 어디 명시되어있는지 알 수 있을까요??
이미지
최규성 — 오늘 오후 12:35
이미지
저희 과제란에 있는 엑셀파일에 있어요!
초원범 — 오늘 오후 12:37
아하 감사합니다 🙂
﻿
초원범
wonbeomchoi
 
초원범 본명아님.
from flask import Flask, request, jsonify, render_template
import requests
import logging
from flask_cors import CORS


# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)  
class SelfIntroductionAnalyzer:
    def __init__(self, api_url):
        self.api_url = api_url

    def analyze(self, introduction, method):
        if method == 'iterative_refinement':
            return self.iterative_refinement(introduction)
        elif method == 'step_by_step':
            return self.step_by_step(introduction)
        elif method == 'few_shot':
            return self.few_shot(introduction)
        elif method == 'constraint_setting':
            return self.constraint_setting(introduction)
        else:
            return 'Error: Invalid method'

    def iterative_refinement(self, introduction):
        return self.send_request(self.create_messages(introduction))

    def step_by_step(self, introduction):
        steps = [
            "단계 1: 자기소개서를 분석합니다.",
            "단계 2: 주요 포인트와 주제를 식별합니다.",
            "단계 3: 구조와 일관성을 평가합니다."
        ]
        messages = self.create_messages(introduction, " ".join(steps))
        return self.send_request(messages)

    def few_shot(self, introduction):
        examples = [
            {"role": "user", "content": "자기소개서의 강점을 분석해주세요.", "role": "assistant", "content": "자기소개서의 강점은 명확한 목표 설정과 구체적인 경험 사례입니다."},
            {"role": "user", "content": "자기소개서에서 개선할 점을 알려주세요.", "role": "assistant", "content": "자기소개서의 개선할 점은 내용의 일관성과 논리적 흐름입니다."}
        ]
        messages = self.create_messages(introduction, examples=examples)
        return self.send_request(messages)

    def constraint_setting(self, introduction):
        constraints = "최대한 자세하게 알려주세요."
        messages = self.create_messages(introduction, constraints)
        return self.send_request(messages)

    def create_messages(self, introduction, additional_content="", examples=None):
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 분석하는 AI입니다."},
            {"role": "user", "content": f"다음 자기소개서를 분석해주세요: {introduction} {additional_content}"}
        ]
        if examples:
            messages = [{"role": ex["role"], "content": ex["content"]} for ex in examples] + messages
        return messages

    def send_request(self, messages):
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in SelfIntroductionAnalyzer: {e}")
            return 'Error: Unable to get a response from the API'


class SelfIntroductionWriter:
    def __init__(self, api_url):
        self.api_url = api_url

    def write(self, prompt, method):
        if method == 'iterative_refinement':
            return self.iterative_refinement(prompt)
        elif method == 'step_by_step':
            return self.step_by_step(prompt)
        elif method == 'few_shot':
            return self.few_shot(prompt)
        elif method == 'constraint_setting':
            return self.constraint_setting(prompt)
        else:
            return 'Error: Invalid method'

    def iterative_refinement(self, prompt):
        return self.send_request(self.create_messages(prompt))

    def step_by_step(self, prompt):
        steps = [
            "단계 1: 지시사항을 이해합니다.",
            "단계 2: 포함할 주요 포인트를 식별합니다.",
            "단계 3: 논리적인 흐름으로 자기소개서를 작성합니다."
        ]
        messages = self.create_messages(prompt, " ".join(steps))
        return self.send_request(messages)

    def few_shot(self, prompt):
        examples = [
            {"role": "user", "content": "자기소개서를 작성해주세요.", "role": "assistant", "content": "저는 열정적이고 성실한 사람입니다. 저는 다양한 경험을 통해 성장했습니다."},
            {"role": "user", "content": "자기소개서의 핵심을 작성해주세요.", "role": "assistant", "content": "저는 협력과 도전정신을 중요시하며, 항상 새로운 것을 배우고자 합니다."}
        ]
        messages = self.create_messages(prompt, examples=examples)
        return self.send_request(messages)

    def constraint_setting(self, prompt):
        constraints = ""
        messages = self.create_messages(prompt, constraints)
        return self.send_request(messages)

    def create_messages(self, prompt, additional_content="", examples=None):
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 작성하는 AI입니다."},
            {"role": "user", "content": f"다음 프롬프트로 자기소개서를 작성해주세요: {prompt} {additional_content}"}
        ]
        if examples:
            messages = [{"role": ex["role"], "content": ex["content"]} for ex in examples] + messages
        return messages

    def send_request(self, messages):
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in SelfIntroductionWriter: {e}")
            return 'Error: Unable to get a response from the API'



class PlagiarismDetector:
    def __init__(self, api_url):
        self.api_url = api_url

    
    def check_plagiarism(self, text, method):
        if method == 'iterative_refinement':
            return self.iterative_refinement(text)
        elif method == 'step_by_step':
            return self.step_by_step(text)
        elif method == 'few_shot':
            return self.few_shot(text)
        elif method == 'constraint_setting':
            return self.constraint_setting(text)
        else:
            return 'Error: Invalid method'
    
    def iterative_refinement(self, text):
        return self.send_request(self.create_messages(text))

    def step_by_step(self, text):
        steps = [
            "단계 1: 텍스트를 분석합니다.",
            "단계 2: 주요 포인트와 주제를 식별합니다.",
            "단계 3: 문장 구조와 단어 선택을 평가합니다.",
            "단계 4: 아이디어의 독창성을 평가합니다.",
            "단계 5: 다른 출처와의 유사성을 평가합니다."
        ]
        messages = self.create_messages(text, " ".join(steps))
        return self.send_request(messages)

    def few_shot(self, text):
        examples = [
            {"role": "user", "content": "다음 텍스트의 표절 여부를 검사해주세요.", "role": "assistant", "content": "이 텍스트는 다음 알려진 텍스트와 유사합니다: [알려진 텍스트]."},
            {"role": "user", "content": "이 텍스트는 표절인가요?", "role": "assistant", "content": "이 텍스트는 [알려진 텍스트]와 유사하므로 표절로 간주됩니다."}
        ]
        messages = self.create_messages(text, examples=examples)
        return self.send_request(messages)

    def constraint_setting(self, text):
        constraints = "텍스트의 모든 부분을 꼼꼼히 검사하고, 문장 구조, 단어 선택, 아이디어의 독창성을 고려하여 다른 출처와의 유사성을 평가해주세요."
        messages = self.create_messages(text, constraints)
        return self.send_request(messages)

    def create_messages(self, text, additional_content="", examples=None):
        messages = [
            {"role": "system", "content": "당신은 텍스트를 분석하여 표절 여부를 판단하는 AI입니다. 문장 구조, 단어 선택, 아이디어의 독창성을 고려하여 다른 출처와의 유사성을 평가합니다."},
            {"role": "user", "content": f"다음 텍스트의 표절 여부를 검사해주세요: {text} {additional_content}"}
        ]
        if examples:
            messages = [{"role": ex["role"], "content": ex["content"]} for ex in examples] + messages
        return messages

    def send_request(self, messages):
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            logging.debug(f"API Response: {response.json()}")  # 추가된 디버그 로그
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
                logging.error(f"Error in PlagiarismDetector: {e}")
                return 'Error: Unable to get a response from the API'


class SpellChecker:
    def __init__(self, api_url):
        self.api_url = api_url

    def check(self, text):
        messages = self.create_messages(text)
        return self.send_request(messages)

    def create_messages(self, text):
        return [
            {"role": "system", "content": "당신은 맞춤법 검사 AI입니다."},
            {"role": "user", "content": f"다음 글의 맞춤법을 확인해주세요: {text}"}
        ]

    def send_request(self, messages):
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in SpellChecker: {e}")
            return 'Error: Unable to get a response from the API'


class PromptOptimizerApp:
    def __init__(self, analyzer, writer, plagiarism_detector, spell_checker):
        self.app = Flask(__name__)
        self.analyzer = analyzer
        self.writer = writer
        self.plagiarism_detector = plagiarism_detector
        self.spell_checker = spell_checker
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/generate', 'generate', self.generate, methods=['POST'])
        self.app.add_url_rule('/analyze', 'analyze', self.analyze_route, methods=['POST'])
        self.app.add_url_rule('/write', 'write', self.write_route, methods=['POST'])
        self.app.add_url_rule('/plagiarism_check', 'plagiarism_check', self.plagiarism_check_route, methods=['POST'])
        self.app.add_url_rule('/spell_check', 'spell_check', self.spell_check_route, methods=['POST'])

    def index(self):
        return render_template('index.html')

    def generate(self):
        data = request.get_json()
        question = data.get('question')
        logging.debug(f"Received question: {question}")

        answer = self.writer.iterative_refinement(question)
        return jsonify({'answer': answer})

    def analyze_route(self):
        data = request.get_json()
        introduction = data.get('introduction')
        method = data.get('method', 'iterative_refinement')  # Default to 'iterative_refinement'
        logging.debug(f"Received introduction: {introduction} with method: {method}")
        analysis = self.analyzer.analyze(introduction, method)
        return jsonify({'analysis': analysis})

    def write_route(self):
        data = request.get_json()
        prompt = data.get('prompt')
        method = data.get('method', 'iterative_refinement')  # Default to 'iterative_refinement'
        logging.debug(f"Received prompt: {prompt} with method: {method}")
        writing = self.writer.write(prompt, method)
        return jsonify({'writing': writing})
        
    def plagiarism_check_route(self):
        data = request.get_json()
        text = data.get('text')
        method = data.get('method', 'iterative_refinement')  # Default to 'iterative_refinement'
        logging.debug(f"Received text for plagiarism check: {text} with method: {method}")
        report = self.plagiarism_detector.check_plagiarism(text, method)
        logging.debug(f"Plagiarism report: {report}")
        return jsonify({'plagiarism_report': report})

    def spell_check_route(self):
        data = request.get_json()
        text = data.get('text')
        logging.debug(f"Received text for spell check: {text}")
        report = self.spell_checker.check(text)
        return jsonify({'spell_check_report': report})

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    API_URL = 'https://open-api.jejucodingcamp.workers.dev/'
    analyzer = SelfIntroductionAnalyzer(API_URL)
    writer = SelfIntroductionWriter(API_URL)
    plagiarism_detector = PlagiarismDetector(API_URL)
    spell_checker = SpellChecker(API_URL)
    app_instance = PromptOptimizerApp(analyzer, writer, plagiarism_detector, spell_checker)
    app_instance.run()
