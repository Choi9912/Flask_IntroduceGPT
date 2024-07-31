# Flask_GPTapi 프로젝트

## 배포주소
http://43.203.240.66:5000/

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
자기소개서+면접 GPT는 GPTAPI 기술을 사용하는 Flask 기반 애플리케이션입니다. 이 애플리케이션은 취업준비를 하고 있는 취준생들에게 자소서부터 면접까지 
한 웹사이트에서 준비할 수 있는 애플리케이션입니다. 기능은 다음과 같습니다.

- 자기소개서 작성
- 자기소개서 분석
- 카피킬러
- 맞춤법 검사기
- 면접 예상 질문

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



