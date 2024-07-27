from flask import Flask, request, jsonify, render_template
import requests
import logging

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
            "Step 1: Analyze the introduction.",
            "Step 2: Identify key points and themes.",
            "Step 3: Evaluate the structure and coherence."
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
        
def plagiarism_check(self, introduction):
    prompt = f"Evaluate the uniqueness of the following text and compare it with common knowledge and sources: {introduction}"
    messages = [
        {"role": "system", "content": "You are an AI that evaluates text for plagiarism by comparing it with common knowledge and existing sources."},
        {"role": "user", "content": prompt}
    ]
    try:
        response = requests.post(self.api_url, json={"model": "gpt-4", "messages": messages})
        response.raise_for_status()
        
        # Check if response is in the expected format
        json_response = response.json()
        if 'choices' in json_response and json_response['choices']:
            return json_response['choices'][0]['message']['content']
        else:
            logging.error(f"Unexpected API response format: {json_response}")
            return 'Error: Unexpected response format from the API'
    except requests.RequestException as e:
        logging.error(f"Error in plagiarism_check: {e}")
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
            "Step 1: Understand the prompt.",
            "Step 2: Identify key points to include.",
            "Step 3: Draft the introduction with a logical flow."
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
        constraints = """다음 조건을 반드시 지켜주세요: 
        - 500장 이상으로 작성해줘
        """
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


class PromptOptimizerApp:
    def __init__(self, analyzer, writer):
        self.app = Flask(__name__)
        self.analyzer = analyzer
        self.writer = writer
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/generate', 'generate', self.generate, methods=['POST'])
        self.app.add_url_rule('/analyze', 'analyze', self.analyze_route, methods=['POST'])
        self.app.add_url_rule('/write', 'write', self.write_route, methods=['POST'])
        self.app.add_url_rule('/plagiarism_check', 'plagiarism_check', self.plagiarism_check_route, methods=['POST'])

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
        introduction = data.get('introduction')
        logging.debug(f"Received introduction for plagiarism check: {introduction}")
        plagiarism_result = self.analyzer.plagiarism_check(introduction)
        return jsonify({'plagiarism_result': plagiarism_result})


    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    API_URL = 'https://open-api.jejucodingcamp.workers.dev/'
    analyzer = SelfIntroductionAnalyzer(API_URL)
    writer = SelfIntroductionWriter(API_URL)
    app_instance = PromptOptimizerApp(analyzer, writer)
    app_instance.run()