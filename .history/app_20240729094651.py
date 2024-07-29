from flask import Flask, request, jsonify, render_template
import requests
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
        self.known_texts = [
            "이것은 표절 탐지를 위한 알려진 샘플 텍스트입니다.",
            "표절 검사를 위해 사용할 수 있는 또 다른 예제 텍스트입니다.",
            "알려진 텍스트 데이터베이스를 시뮬레이션하기 위한 세 번째 텍스트입니다."
        ]
        self.api_url = api_url
    
    def update_known_texts(self, prompt, num_samples=5):
        new_texts = self.generate_sample_texts(prompt, num_samples)
        self.known_texts.extend(new_texts)

    def generate_sample_texts(self, prompt, num_samples=5):
        response = requests.post(self.api_url, json={
            "prompt": prompt,
            "num_samples": num_samples
        })
        response.raise_for_status()
        data = response.json()
        return [choice['text'].strip() for choice in data['choices']]

    def preprocess_text(self, text):
        # 모든 문자를 소문자로 변환하고, 숫자와 알파벳 이외의 문자는 제거
        return ' '.join(''.join(e for e in word if e.isalnum()).lower() for word in text.split())

    def calculate_similarity(self, text1, text2):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        return cosine_sim[0][0]

    def is_plagiarized(self, similarity, threshold=0.8):
        return similarity >= threshold

    def check_plagiarism(self, text, threshold=0.8):
        text = self.preprocess_text(text)
        results = []
        for known_text in self.known_texts:
            known_text_processed = self.preprocess_text(known_text)
            similarity = self.calculate_similarity(text, known_text_processed)
            is_plagiarized_flag = self.is_plagiarized(similarity, threshold)
            results.append({
                "known_text": known_text,
                "similarity": similarity,
                "is_plagiarized": 'true' if is_plagiarized_flag else 'false'
            })
        return results


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
        logging.debug(f"Received text for plagiarism check: {text}")
        report = self.plagiarism_detector.check_plagiarism(text)
        
        # Convert boolean values to strings for JSON serialization
        for entry in report:
            entry['is_plagiarized'] = 'true' if entry['is_plagiarized'] else 'false'
        
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
