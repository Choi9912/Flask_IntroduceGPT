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
            "단계 1. 소제목을 넣자: 자기소개서에 소제목을 추가합니다.",
            "단계 2. 두괄식으로 작성하자: 결론부터 말하고 자세한 내용을 덧붙입니다.",
            "단계 3. 문장을 간결하게, 문단을 나눠서 쓰자: 간결하고 명확한 문장을 사용하고, 적절한 문단 나누기로 가독성을 높입니다."
   ]
        messages = self.create_messages(prompt, " ".join(steps))
        return self.send_request(messages)

    def few_shot(self, prompt):
        examples = [
            {
                "role": "user", 
                "content": "자기소개서를 작성해주세요.", 
                "role": "assistant", 
                "content": (
                    "① 경력 소개: 저는 열정적이고 성실한 사람입니다. "
                    "② 성장 과정: 다양한 경험을 통해 성장했습니다. "
                    "③ 결론: 저의 협력과 도전정신을 바탕으로 회사에 기여하고 싶습니다."
                )
            },
            {
                "role": "user", 
                "content": "자기소개서의 핵심을 작성해주세요.", 
                "role": "assistant", 
                "content": (
                    "- 소개: 저는 협력과 도전정신을 중요시합니다. "
                    "- 경험: 항상 새로운 것을 배우고자 합니다. "
                    "- 목표: 이러한 태도로 귀사에 큰 기여를 하고 싶습니다."
                )
            }
        ]
        messages = self.create_messages(prompt, examples=examples)
        return self.send_request(messages)

    def constraint_setting(self, prompt):
        constraints = "소제목을 포함하고, 두괄식으로 작성하며, 문장을 간결하게 쓰고, 문단을 나누어 주세요."
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
            {"role": "system", "content": "당신은 텍스트를 분석하여 표절 여부를 판단하는 AI입니다."},
            {"role": "user", "content": f"다음 텍스트의 표절 여부를 검사해주세요: {text} {additional_content}"}
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
            logging.error(f"Error in PlagiarismDetector: {e}")
            return 'Error: Unable to get a response from the API'



class SpellChecker:
    def __init__(self, api_url):
        self.api_url = api_url

    def check(self, text, method):
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
            "단계 2: 철자 오류를 식별합니다.",
            "단계 3: 문법 오류를 식별합니다.",
            "단계 4: 문장 구조를 평가합니다.",
            "단계 5: 전체 텍스트의 일관성을 평가합니다."
        ]
        messages = self.create_messages(text, " ".join(steps))
        return self.send_request(messages)

    def few_shot(self, text):
        examples = [
            {"role": "user", "content": "다음 텍스트의 맞춤법을 검사해주세요.", "role": "assistant", "content": "이 텍스트에는 다음과 같은 철자 오류가 있습니다: [오류 예시]."},
            {"role": "user", "content": "이 텍스트의 문법 오류를 수정해주세요.", "role": "assistant", "content": "이 텍스트에는 다음과 같은 문법 오류가 있습니다: [오류 예시]."}
        ]
        messages = self.create_messages(text, examples=examples)
        return self.send_request(messages)

    def constraint_setting(self, text):
        constraints = "텍스트의 철자와 문법을 철저히 검사하고, 문장 구조와 일관성을 고려하여 전체 텍스트를 평가해주세요."
        messages = self.create_messages(text, constraints)
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

        return jsonify({'plagiarism_report': report})


    def spell_check_route(self):
        data = request.get_json()
        text = data.get('text')
        method = data.get('method', 'iterative_refinement')  # Default to 'iterative_refinement'
        logging.debug(f"Received text for spell check: {text} with method: {method}")
        report = self.spell_checker.check(text, method)
        return jsonify({'spell_check_report': report})

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    analyzer = SelfIntroductionAnalyzer(API_URL)
    writer = SelfIntroductionWriter(API_URL)
    plagiarism_detector = PlagiarismDetector(API_URL)
    spell_checker = SpellChecker(API_URL)
    app_instance = PromptOptimizerApp(analyzer, writer, plagiarism_detector, spell_checker)
    app_instance.run()