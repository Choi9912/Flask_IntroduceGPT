from flask import Flask, request, jsonify, render_template
import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('API_URL')

# Configure logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

def send_api_request(api_url, role, user_content):
    messages = [
        {"role": "system", "content": role},
        {"role": "user", "content": user_content}
    ]
    try:
        response = requests.post(api_url, json=messages)
        response.raise_for_status()
        return response.json().get('choices')[0]['message']['content']
    except requests.RequestException as e:
        logging.error(f"Error in API request: {e}")
        return 'Error: Unable to get a response from the API'

class UnifiedPromptHandler:
    def __init__(self, api_url):
        self.api_url = api_url

    def handle(self, content, method, role_template, user_content_template):
        if method == 'unified_prompt':
            role = role_template
            user_content = user_content_template.format(content)
            return send_api_request(self.api_url, role, user_content)
        return 'Error: Invalid method'

class SelfIntroductionAnalyzer(UnifiedPromptHandler):
    def analyze(self, introduction, method):
        role_template = "당신은 자기소개서를 분석하는 AI입니다."
        user_content_template = "다음 자기소개서를 분석해주세요: {} 자기소개서를 분석하여 주요 포인트와 주제를 식별하고, 구조와 일관성을 평가합니다. 자기소개서의 강점과 개선할 점을 자세하게 알려주세요."
        return self.handle(introduction, method, role_template, user_content_template)

class SelfIntroductionWriter(UnifiedPromptHandler):
    def write(self, prompt, method):
        role_template = "당신은 자기소개서를 작성하는 AI입니다."
        user_content_template = "다음 프롬프트로 자기소개서를 작성해주세요: {} 소제목을 포함하고, 문단을 나누어 500자 이상으로 자기소개서를 작성해주세요."
        return self.handle(prompt, method, role_template, user_content_template)

class PlagiarismDetector(UnifiedPromptHandler):
    def check_plagiarism(self, text, method):
        role_template = "당신은 텍스트를 분석하여 표절 여부를 판단하는 AI입니다."
        user_content_template = "다음 텍스트의 표절 여부를 검사해주세요: {} 텍스트를 분석하여 주요 포인트와 주제를 식별하고, 문장 구조와 단어 선택을 평가합니다. 아이디어의 독창성을 평가하고, 다른 출처와의 유사성을 평가하여 표절 여부를 판단해주세요."
        return self.handle(text, method, role_template, user_content_template)

class SpellChecker(UnifiedPromptHandler):
    def check(self, text, method):
        role_template = "당신은 맞춤법 검사 AI입니다."
        user_content_template = "다음 글의 맞춤법을 확인해주세요: {} 텍스트의 철자와 문법을 철저히 검사하고, 문장 구조와 일관성을 고려하여 전체 텍스트를 평가해주세요."
        return self.handle(text, method, role_template, user_content_template)

class InterviewQuestionGenerator(UnifiedPromptHandler):
    def generate_questions(self, job_description, method):
        role_template = "당신은 채용정보를 분석하여 면접 질문을 생성하는 AI입니다."
        user_content_template = "다음 채용정보를 바탕으로 면접 질문을 생성해주세요: {} 채용정보를 분석하여 주요 요구사항과 필수 스킬을 식별하고, 이에 맞는 면접 질문을 생성합니다. 채용정보에 명시된 요구사항과 필수 스킬을 기반으로 질문을 만들어 주세요."
        return self.handle(job_description, method, role_template, user_content_template)

class PromptOptimizerApp:
    def __init__(self, analyzer, writer, plagiarism_detector, spell_checker, interview_question_generator):
        self.app = Flask(__name__)
        self.analyzer = analyzer
        self.writer = writer
        self.plagiarism_detector = plagiarism_detector
        self.spell_checker = spell_checker
        self.interview_question_generator = interview_question_generator
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.add_route('/generate', 'generate', self.writer.write, 'question')
        self.add_route('/analyze', 'analyze', self.analyzer.analyze, 'introduction')
        self.add_route('/write', 'write', self.writer.write, 'prompt')
        self.add_route('/plagiarism_check', 'plagiarism_check', self.plagiarism_detector.check_plagiarism, 'text')
        self.add_route('/spell_check', 'spell_check', self.spell_checker.check, 'text')
        self.add_route('/generate_interview_questions', 'generate_interview_questions', self.interview_question_generator.generate_questions, 'job_description')

    def add_route(self, rule, endpoint, handler, data_key):
        self.app.add_url_rule(rule, endpoint, lambda: self.generic_route(handler, data_key), methods=['POST'])

    def generic_route(self, handler, data_key):
        data = request.get_json()
        content = data.get(data_key)
        method = data.get('method', 'unified_prompt')
        logging.debug(f"Received {data_key}: {content} with method: {method}")
        result = handler(content, method)
        return jsonify({f'{data_key}_result': result})

    def index(self):
        return render_template('index.html')

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    analyzer = SelfIntroductionAnalyzer(API_URL)
    writer = SelfIntroductionWriter(API_URL)
    plagiarism_detector = PlagiarismDetector(API_URL)
    spell_checker = SpellChecker(API_URL)
    interview_question_generator = InterviewQuestionGenerator(API_URL)
    app_instance = PromptOptimizerApp(analyzer, writer, plagiarism_detector, spell_checker, interview_question_generator)
    app_instance.run()
