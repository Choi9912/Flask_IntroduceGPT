# Flask_GPTapi 프로젝트

**배포주소** : http://43.203.240.66:5000/

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
자기소개서+면접 GPT는 취업 준비 중인 지원자들이 자기소개서 작성부터 면접 대비까지 한 곳에서 준비할 수 있도록 돕는 웹 애플리케이션입니다. 이 애플리케이션은 Flask 프레임워크와 GPT API 기술을 활용하여 구현됩니다. 주요 기능은 다음과 같습니다:

- **자기소개서 작성**: 사용자가 입력한 정보를 바탕으로 자기소개서를 자동으로 생성합니다.
- **자기소개서 분석**: 작성된 자기소개서를 분석하여 개선점을 제시합니다.
- **카피킬러**: 유사도 검사를 통해 자기소개서의 독창성을 확인합니다.
- **맞춤법 검사기**: 자기소개서의 맞춤법 및 문법 오류를 검사하고 수정 제안을 합니다.
- **면접 예상 질문**: 사용자의 이력서와 자기소개서를 기반으로 예상 면접 질문을 제공합니다.
  
## 목표
**1.사용자 경험 개선**
   - 취준생들이 자기소개서 작성부터 면접 준비를 효율적으로 할 수 있도록 도와주는 사용자 친화적인 환경 제공 기술적 우수성
     
**2. 최신 GPT API 기술을 활용한 자연어 처리**
   - 안정적이고 확장 가능한 Flask 기반의 백엔드 구현
     
**3. AWS EC2를 활용한 배포**

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
| ![자기소개서 작성](https://github.com/user-attachments/assets/48424487-a90c-47de-8c8f-f85979deafd7) | ![자기소개서 분석](https://github.com/user-attachments/assets/847b8f3a-8c26-4d72-81a8-47b2dd035406)



| 카피 킬러 | 맞춤법 검사 | 면접 질문 예상 |
| --- | --- | -- |
| ![카피킬러](https://github.com/user-attachments/assets/e88faebf-b297-45ae-9634-98b6e2e8cd71) | ![맞춤법검사](https://github.com/user-attachments/assets/c66c4655-bca1-413d-a4d0-a093a1d90096) | ![면접 질문 예상](https://github.com/user-attachments/assets/053c3f1c-15cd-4992-b16c-7e8af886d451)

 


## 코드 
### 프롬프트 최적화
```python
class SelfIntroductionWriter: # 자기소개서 작성
   def check(self,text,method)
        if method == 'improved_prompt':
            return self.improved_prompt(job_description)
        elif method == 'step_by_step_prompt':
            return self.step_by_step_prompt(job_description)
        elif method == 'example_prompt':
            return self.example_prompt(job_description)
        elif method == 'constrained_prompt':
            return self.constrained_prompt(job_description)
        else:
            return 'Error: Invalid method'

class SelfIntroductionAnalyzer: # 자기소개서 분석
    ~
class PlagiarismDetector: # AI카피킬러
   ~
class SpellChecker: # 맞춤법 검사
   ~
```
- 각 기능의 클래스에 들어가는 프롬프트 최적화 기법
  - improved_prompt : 여러 번의 반복을 통해 자기소개서를 점진적으로 개선합니다.
  - step_by_step_prompt : 자기소개서를 개별 단계로 나누어 상세히 분석합니다.
  - example_prompt : 예제를 사용하여 분석을 안내하고 타겟 피드백을 제공합니다.
  - constrained_prompt  : 특정 제약 조건을 가지고 자기소개서를 분석하여 철저함을 보장합니다.
    
### 웹 애플리케이션 설정 및 엔드포인트 처리
```python
class PromptOptimizerApp # 위의 다양한 기능들을 작업 수행
   def setup_routes(self) # 라우트 설정 메서드
   def index(self) # 인덱스 페이지
   def generate(self) # 자기소개서 작성 
   def analyze_route(self) # 자기소개서 분석
   def plagiarism_check_route(self) #표절 검사
   def spell_check_route(self) # 맞춤법 검사
   def generate_interview_questions_route(self) # 면접 예상 질문

```



