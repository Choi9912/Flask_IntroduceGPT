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

class SelfIntroductionAnalyzer:
    def __init__(self, api_url):
        self.api_url = api_url

    def analyze(self, introduction, method):
        if method == 'unified_prompt':
            return self.unified_prompt(introduction)
        else:
            return 'Error: Invalid method'

    def unified_prompt(self, introduction):
        steps = (
            "자기소개서를 분석하여 주요 포인트와 주제를 식별하고, "
            "구조와 일관성을 평가합니다. "
            "자기소개서의 강점과 개선할 점을 자세하게 알려주세요."
        )
        messages = self.create_messages(introduction, steps)
        return self.send_request(messages)

    def create_messages(self, introduction, additional_content=""):
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 분석하는 AI입니다."},
            {"role": "user", "content": f"다음 자기소개서를 분석해주세요: {introduction} {additional_content}"}
        ]
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
        if method == 'unified_prompt':
            return self.unified_prompt(prompt)
        else:
            return 'Error: Invalid method'

    def unified_prompt(self, prompt):
        steps = (
            "소제목을 포함하고, 두괄식으로 작성하며, 문장을 간결하게 쓰고, 문단을 나누어 "
            "자기소개서를 작성해주세요."
        )
        messages = self.create_messages(prompt, steps)
        return self.send_request(messages)

    def create_messages(self, prompt, additional_content=""):
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 작성하는 AI입니다."},
            {"role": "user", "content": f"다음 프롬프트로 자기소개서를 작성해주세요: {prompt} {additional_content}"}
        ]
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
        if method == 'unified_prompt':
            return self.unified_prompt(text)
        else:
            return 'Error: Invalid method'
    
    def unified_prompt(self, text):
        steps = (
            "텍스트를 분석하여 주요 포인트와 주제를 식별하고, 문장 구조와 단어 선택을 평가합니다. "
            "아이디어의 독창성을 평가하고, 다른 출처와의 유사성을 평가하여 표절 여부를 판단해주세요."
        )
        messages = self.create_messages(text, steps)
        return self.send_request(messages)

    def create_messages(self, text, additional_content=""):
        messages = [
            {"role": "system", "content": "당신은 텍스트를 분석하여 표절 여부를 판단하는 AI입니다."},
            {"role": "user", "content": f"다음 텍스트의 표절 여부를 검사해주세요: {text} {additional_content}"}
        ]
        return messages

    def send_request(self, messages):
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in PlagiarismDetector: {e}")
            return 'Error: Unable to get a response from the API'


class SpellChecker:
    def __init__(self, api_url):
        self.api_url = api_url

    def check(self, text, method):
        if method == 'unified_prompt':
            return self.unified_prompt(text)
        else:
            return 'Error: Invalid method'
    
    def unified_prompt(self, text):
        steps = (
            "텍스트의 철자와 문법을 철저히 검사하고, 문장 구조와 일관성을 고려하여 전체 텍스트를 평가해주세요."
        )
        messages = self.create_messages(text, steps)
        return self.send_request(messages)
    
    def create_messages(self, text, additional_content=""):
        messages = [
            {"role": "system", "content": "당신은 맞춤법 검사 AI입니다."},
            {"role": "user", "content": f"다음 글의 맞춤법을 확인해주세요: {text} {additional_content}"}
        ]
        return messages

    def send_request(self, messages):
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in SpellChecker: {e}")
            return 'Error: Unable to get a response from the API'


class InterviewQuestionGenerator:
    def __init__(self, api_url):
        self.api_url = api_url

    def generate_questions(self, job_description, method):
        if method == 'unified_prompt':
            return self.unified_prompt(job_description)
        else:
            return 'Error: Invalid method'

    def unified_prompt(self, job_description):
        steps = (
            "채용정보를 분석하여 주요 요구사항과 필수 스킬을 식별하고, 이에 맞는 면접 질문을 생성합니다. "
            "채용정보에 명시된 요구사항과 필수 스킬을 기반으로 질문을 만들어 주세요."
        )
        messages = self.create_messages(job_description, steps)
        return self.send_request(messages)

    def create_messages(self, job_description, additional_content=""):
        messages = [
            {"role": "system", "content": "당신은 채용정보를 분석하여 면접 질문을 생성하는 AI입니다."},
            {"role": "user", "content": f"다음 채용정보를 바탕으로 면접 질문을 생성해주세요: {job_description} {additional_content}"}
        ]
        return messages

    def send_request(self, messages):
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in InterviewQuestionGenerator: {e}")
            return 'Error: Unable to get a response from the API'


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
        self.app.add_url_rule('/generate', 'generate', self.generate, methods=['POST'])
        self.app.add_url_rule('/analyze', 'analyze', self.analyze_route, methods=['POST'])
        self.app.add_url_rule('/write', 'write', self.write_route, methods=['POST'])
        self.app.add_url_rule('/plagiarism_check', 'plagiarism_check', self.plagiarism_check_route, methods=['POST'])
        self.app.add_url_rule('/spell_check', 'spell_check', self.spell_check_route, methods=['POST'])
        self.app.add_url_rule('/generate_interview_questions', 'generate_interview_questions', self.generate_interview_questions_route, methods=['POST'])

    def index(self):
        return render_template('index.html')

    def generate(self):
        data = request.get_json()
        question = data.get('question')
        logging.debug(f"Received question: {question}")
        answer = self.writer.unified_prompt(question)
        return jsonify({'answer': answer})

    def analyze_route(self):
        data = request.get_json()
        introduction = data.get('introduction')
        method = data.get('method', 'unified_prompt')
        logging.debug(f"Received introduction: {introduction} with method: {method}")
        analysis = self.analyzer.analyze(introduction, method)
        return jsonify({'analysis': analysis})

    def write_route(self):
        data = request.get_json()
        prompt = data.get('prompt')
        method = data.get('method', 'unified_prompt')
        logging.debug(f"Received prompt: {prompt} with method: {method}")
        writing = self.writer.write(prompt, method)
        return jsonify({'writing': writing})

    def plagiarism_check_route(self):
        data = request.get_json()
        text = data.get('text')
        method = data.get('method', 'unified_prompt')
        logging.debug(f"Received text for plagiarism check: {text} with method: {method}")
        report = self.plagiarism_detector.check_plagiarism(text, method)
        return jsonify({'plagiarism_report': report})

    def spell_check_route(self):
        data = request.get_json()
        text = data.get('text')
        method = data.get('method', 'unified_prompt')
        logging.debug(f"Received text for spell check: {text} with method: {method}")
        report = self.spell_checker.check(text, method)
        return jsonify({'spell_check_report': report})

    def generate_interview_questions_route(self):
        data = request.get_json()
        job_description = data.get('job_description')
        method = data.get('method', 'unified_prompt')
        logging.debug(f"Received job description: {job_description} with method: {method}")
        questions = self.interview_question_generator.generate_questions(job_description, method)
        return jsonify({'questions': questions})

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
