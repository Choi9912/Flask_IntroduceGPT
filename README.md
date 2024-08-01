# Flask_GPTAPI 프로젝트

**배포주소** : http://43.202.47.192:5000/

## 시작하기

1. **의존성 설치**: 필요한 모든 의존성을 설치하세요.
   ```bash
   pip install -r requirements.txt

   ```
2. **실행하기**
   ```bash
   python app.py
   ```

| WBS | WireFrame |
| --- | --- |
| <img src="https://github.com/user-attachments/assets/5cbb9120-3fc8-4315-ad76-a984e5160721" alt="mermaid-ai-diagram-2024-07-31-013120" style="width: 600px;"> | <img src="https://github.com/user-attachments/assets/4cdd0935-f72b-48e1-8f8c-8c2c51627d83" alt="WireFrame" style="width: 300px;"> |



## 기술 스택
**Enviroment**  

<img src="https://img.shields.io/badge/Visual Studio Code-2F80ED?style=for-the-badge&logo=VSC&logoColor=white">  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">


**Development** 

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/flask-FF9900?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/amazonec2-000000?style=for-the-badge&logo=amazonec2&logoColor=white"> 


## 프로젝트 소개
**자기소개서+면접 GPT**는 취업 준비 중인 지원자들이 자기소개서 작성부터 면접 대비까지 한 곳에서 준비할 수 있도록 돕는 웹 애플리케이션입니다. 이 애플리케이션은 Flask 프레임워크와 GPT API 기술을 활용하여 구현됩니다. 주요 기능은 다음과 같습니다:

- **자기소개서 작성**: 사용자가 입력한 정보를 바탕으로 자기소개서를 자동으로 생성합니다.
- **자기소개서 분석**: 작성된 자기소개서를 분석하여 개선점을 제시합니다.
- **카피킬러**: 유사도 검사를 통해 자기소개서의 독창성을 확인합니다.
- **맞춤법 검사기**: 자기소개서의 맞춤법 및 문법 오류를 검사하고 수정 제안을 합니다.
- **면접 예상 질문**: 채용 정보를 기반으로 하여금 면접 예상 질문을 제안합니다
  
## 목표
**1.사용자 경험 개선**
   - 취준생들이 자기소개서 작성부터 면접 준비를 효율적으로 할 수 있도록 도와주는 사용자 친화적인 환경 제공 기술적 우수성
     
**2. 최신 GPT API 기술을 활용한 웹 애플리케이션**
   - 안정적이고 확장 가능한 Flask 기반의 백엔드 구현
     
**3. AWS EC2를 활용한 배포**
   - AWS EC2 인스턴스를 생성하고, 필요한 설정을 통해 서버 환경을 준비합니다.
   - 인스턴스의 보안 그룹을 설정하여 필요한 포트를 열고, 접근 제어를 관리합니다.
     
## 요구사항 분석
### 기능 요구사항
**1. 텍스트 입력을 통해 자기소개서 자동 생성**
   - GPT API를 사용한 문장 생성 및 수정
   - 자기소개서 분석 (내용 분석 및 개선점 제안)

**2. 문법 및 AI 카피 킬러**
   - 맞춤법 및 문법 검사 
   - 유사도 검사 (카피킬러 기능)
     
**3. 면접 대비**
   - 사용자 정보 기반 맞춤형 면접 예상 질문 제공
   - 면접 질문 답변 작성 지원



 ## 화면 구성 📺

| 자기소개서 작성 | 자기소개서 분석  |
| --- | --- |
| ![자기소개서 작성](https://github.com/user-attachments/assets/f7caafb8-c0b7-431a-b748-bb69357f1f63) | ![자기소개서 분석](https://github.com/user-attachments/assets/91461315-e3b1-4921-876c-bb20fd74ba28)




| 카피 킬러 | 맞춤법 검사 | 면접 질문 예상 |
| --- | --- | -- |
| ![카피 킬러](https://github.com/user-attachments/assets/c4542b40-5156-4a81-a23f-2c13c6454ed0) | ![맞춤법 검사](https://github.com/user-attachments/assets/c53eb6e1-aace-4155-8c28-0f3335ba6264) | ![면접 예상 질문](https://github.com/user-attachments/assets/4df4b35b-35c2-4ca5-a5d8-b4d8e89e9351)


## 코드 요약
### API Request Function 
```python
def send_api_request(api_url, role, user_content): 
    messages = [
        {"role": "system", "content": role},
        {"role": "user", "content": user_content}
    ] 
   ...
```
### Unified Prompt Handler Base Class
```python
class UnifiedPromptHandler: ...
```
### Task-Specific Classes
```python
class SelfIntroductionAnalyzer(UnifiedPromptHandler): ...
class SelfIntroductionWriter(UnifiedPromptHandler): ...
class PlagiarismDetector(UnifiedPromptHandler): ...
class SpellChecker(UnifiedPromptHandler): ...
class InterviewQuestionGenerator(UnifiedPromptHandler): ...
```
### Flask App Routes Setup
```python
class PromptOptimizerApp: # 위의 다양한 기능들을 작업 수행
   def setup_routes(self): ... # 라우트 설정 메서드
   def add_route(self, rule, endpoint, handler, data_key): ...
   def generic_route(self, handler, data_key):
   def index(self):
   def run(self):
```
## 개선 사항
- 예상 면접 질문 기능 추가
- 코드의 효율성 및 최적화 : **상속 이용**

## 회고
- 이번 프로젝트는 이전에 사용했던 기술, 프레임워크들을 이용하지 않고 새로운 기술과 프레임워크를 사용하는 목표로 뒀습니다. </br>
그래서 API활용, Flask, aws ec2를 활용한 배포까지 처음 해보는 경험이었고 많은 공부가 되었다는 생각이 듭니다.
