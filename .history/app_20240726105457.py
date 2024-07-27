from flask import Flask, request, jsonify, render_template
import requests
import openai
from fpdf import FPDF

class SelfIntroductionAnalyzer:
    def __init__(self, api_url):
        self.api_url = api_url

    def analyze(self, introduction):
        messages = [
            {"role": "system", "content": "당신은 자기소개서를 분석하는 AI입니다."},
            {"role": "user", "content": f"다음 자기소개서를 분석해주세요: {introduction}"}
        ]
        try:
            response = requests.post(self.api_url, json=messages)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            return response.json().get('choices')[0]['message']['content']
        except requests.RequestException as e:
            logging.error(f"Error in analyze: {e}")
            return 'Error: Unable to get a response from the API'


class PromptOptimizerApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.API_URL = 'https://open-api.jejucodingcamp.workers.dev/'
        self.analyzer = SelfIntroductionAnalyzer(self.API_URL)
        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/generate', 'generate', self.generate, methods=['POST'])
        self.app.add_url_rule('/analyze', 'analyze', self.analyze, methods=['POST'])

    def index(self):
        return render_template('index.html')

    def generate(self):
        data = request.get_json()
        question = data.get('question')

        # Example implementation of Iterative Refinement
        answer = self.iterative_refinement(question)
        return jsonify({'answer': answer})

    def iterative_refinement(self, question):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
        
        response = requests.post(self.API_URL, json=messages)
        
        # Check if the response is successful and refine the prompt if necessary
        if response.status_code == 200:
            return response.json().get('choices')[0]['message']['content']
        else:
            # Adding refinement by providing feedback and requesting clarification
            messages.append({"role": "user", "content": "Please clarify the previous answer."})
            response = requests.post(self.API_URL, json=messages)
            if response.status_code == 200:
                return response.json().get('choices')[0]['message']['content']
            else:
                return 'Error: Unable to get a response from the API'

    def get_step_by_step_response(self, question):
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
        response = requests.post(self.API_URL, json=messages)
        return response.json().get('choices')[0]['message']['content'] if response.status_code == 200 else 'Error'

    def get_few_shot_response(self, question):
        examples = [
            {"role": "user", "content": "What is the capital of France?", "role": "assistant", "content": "The capital of France is Paris."},
            {"role": "user", "content": "What is 2+2?", "role": "assistant", "content": "2+2 equals 4."}
        ]
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            *examples,
            {"role": "user", "content": question}
        ]
        response = requests.post(self.API_URL, json=messages)
        return response.json().get('choices')[0]['message']['content'] if response.status_code == 200 else 'Error'

    def get_constrained_response(self, question):
        constraints = "Please provide a brief, concise answer without any additional information."
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{question}\n{constraints}"}
        ]
        response = requests.post(self.API_URL, json=messages)
        return response.json().get('choices')[0]['message']['content'] if response.status_code == 200 else 'Error'

    def analyze(self):
        data = request.get_json()
        introduction = data.get('introduction')
        analysis = self.analyzer.analyze(introduction)
        return jsonify({'analysis': analysis})

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    app_instance = PromptOptimizerApp()
    app_instance.run()
