from flask import Flask, request, jsonify, render_template
import requests
import logging
import re
from collections import Counter
import math
import json
# Configure logging
logging.basicConfig(level=logging.DEBUG)

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
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 분석하는 AI입니다."},
            {"role": "user", "content": f"다음 자기소개서를 분석해주세요: {introduction}"}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in iterative_refinement: {e}")
            messages.append({"role": "user", "content": "Please clarify the previous answer."})
            try:
                response = requests.post(self.api_url, json=messages)
                response.raise_for_status()
                return response.json().get('choices')[0]['message']['content']
            except requests.RequestException as e:
                logging.error(f"Error in refinement retry: {e}")
                return 'Error: Unable to get a response from the API'

    def step_by_step(self, introduction):
        steps = [
            "단계 1: 자기소개서를 분석합니다.",
            "단계 2: 주요 포인트와 주제를 식별합니다.",
            "단계 3: 구조와 일관성을 평가합니다."
        ]
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 분석하는 AI입니다."},
            {"role": "user", "content": f"다음 자기소개서를 분석해주세요: {introduction}"},
            {"role": "assistant", "content": " ".join(steps)}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in step_by_step: {e}")
            return 'Error: Unable to get a response from the API'

    def few_shot(self, introduction):
        examples = [
            {"role": "user", "content": "자기소개서의 강점을 분석해주세요.", "role": "assistant", "content": "자기소개서의 강점은 명확한 목표 설정과 구체적인 경험 사례입니다."},
            {"role": "user", "content": "자기소개서에서 개선할 점을 알려주세요.", "role": "assistant", "content": "자기소개서의 개선할 점은 내용의 일관성과 논리적 흐름입니다."}
        ]
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 분석하는 AI입니다."},
            *examples,
            {"role": "user", "content": f"다음 자기소개서를 분석해주세요: {introduction}"}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in few_shot: {e}")
            return 'Error: Unable to get a response from the API'

    def constraint_setting(self, introduction):
        constraints = "최대한 자세하게 알려주세요."
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 분석하는 AI입니다."},
            {"role": "user", "content": f"다음 자기소개서를 분석해주세요: {introduction}\n{constraints}"}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in constraint_setting: {e}")
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
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 작성하는 AI입니다."},
            {"role": "user", "content": f"다음 프롬프트로 자기소개서를 작성해주세요: {prompt}"}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in iterative_refinement: {e}")
            messages.append({"role": "user", "content": "Please improve the previous version."})
            try:
                response = requests.post(self.api_url, json=messages)
                response.raise_for_status()
                return response.json().get('choices')[0]['message']['content']
            except requests.RequestException as e:
                logging.error(f"Error in refinement retry: {e}")
                return 'Error: Unable to get a response from the API'

    def step_by_step(self, prompt):
        steps = [
                "단계 1: 지시사항을 이해합니다.",
                "단계 2: 포함할 주요 포인트를 식별합니다.",
                "단계 3: 논리적인 흐름으로 자기소개서를 작성합니다."
        ]
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 작성하는 AI입니다."},
            {"role": "user", "content": f"다음 프롬프트로 자기소개서를 작성해주세요: {prompt}"},
            {"role": "assistant", "content": " ".join(steps)}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in step_by_step: {e}")
            return 'Error: Unable to get a response from the API'

    def few_shot(self, prompt):
        examples = [
            {"role": "user", "content": "자기소개서를 작성해주세요.", "role": "assistant", "content": "저는 열정적이고 성실한 사람입니다. 저는 다양한 경험을 통해 성장했습니다."},
            {"role": "user", "content": "자기소개서의 핵심을 작성해주세요.", "role": "assistant", "content": "저는 협력과 도전정신을 중요시하며, 항상 새로운 것을 배우고자 합니다."}
        ]
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 작성하는 AI입니다."},
            *examples,
            {"role": "user", "content": f"다음 프롬프트로 자기소개서를 작성해주세요: {prompt}"}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in few_shot: {e}")
            return 'Error: Unable to get a response from the API'

    def constraint_setting(self, prompt):
        constraints = ""
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 작성하는 AI입니다."},
            {"role": "user", "content": f"다음 프롬프트로 자기소개서를 작성해주세요: {prompt}\n{constraints}"}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in constraint_setting: {e}")
            return 'Error: Unable to get a response from the API'


class PlagiarismChecker:
    def __init__(self, api_url):
        self.api_url = api_url

    def preprocess_text(self, text):
        # 텍스트 전처리: 소문자 변환, 특수문자 제거 등
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def calculate_similarity(self, text1, text2):
        # 간단한 코사인 유사도 계산
        vector1 = Counter(text1.split())
        vector2 = Counter(text2.split())
        
        intersection = set(vector1.keys()) & set(vector2.keys())
        numerator = sum([vector1[x] * vector2[x] for x in intersection])
        
        sum1 = sum([vector1[x]**2 for x in vector1.keys()])
        sum2 = sum([vector2[x]**2 for x in vector2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        
        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    def check(self, text):
        preprocessed_text = self.preprocess_text(text)
        
        messages = [
            {"role": "system", "content": "You are an AI trained to detect plagiarism. Analyze the given text and provide a detailed report on potential plagiarism."},
            {"role": "user", "content": f"Analyze this text for potential plagiarism: {preprocessed_text}"}
        ]
        
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            ai_analysis = response.json().get('choices')[0]['message']['content']
            
            # 유사도 점수 계산 (예시 - 실제로는 데이터베이스나 외부 소스와 비교해야 함)
            similarity_score = self.calculate_similarity(preprocessed_text, preprocessed_text[::-1])  # 임시로 텍스트를 뒤집어 비교
            
            report = {
                "similarity_score": similarity_score,
                "ai_analysis": ai_analysis,
                "preprocessed_text": preprocessed_text
            }
            
            return json.dumps(report)
        except requests.RequestException as e:
            logging.error(f"Error in PlagiarismChecker: {e}")
            return json.dumps({'error': 'Unable to get a response from the API'})


class SpellChecker:
    def __init__(self, api_url):
        self.api_url = api_url

    def check(self, text):
        messages = [
            {"role": "system", "content": "당신은 맞춤법 검사 AI입니다."},
            {"role": "user", "content": f"다음 글의 맞춤법을 확인해주세요: {text}"}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in SpellChecker: {e}")
            return 'Error: Unable to get a response from the API'


class PromptOptimizerApp:
    def __init__(self, analyzer, writer, plagiarism_checker, spell_checker):
        self.app = Flask(__name__)
        self.analyzer = analyzer
        self.writer = writer
        self.plagiarism_checker = plagiarism_checker
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
        logging.debug(f"Received text for plagiarism check: {text}")
        report = self.plagiarism_checker.check(text)
        return jsonify({'plagiarism_report': json.loads(report)})

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
    plagiarism_checker = PlagiarismChecker(API_URL)
    spell_checker = SpellChecker(API_URL)
    app_instance = PromptOptimizerApp(analyzer, writer, plagiarism_checker, spell_checker)
    app_instance.run()