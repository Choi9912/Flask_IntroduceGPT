document.addEventListener('DOMContentLoaded', function() {
    const questionInput = document.getElementById('question');
    const sendBtn = document.getElementById('sendBtn');
    const conversation = document.getElementById('conversation');
    const introductionInput = document.getElementById('introduction');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const analysisDiv = document.getElementById('analysis');
    const plagiarismInput = document.getElementById('plagiarismText');
    const plagiarismBtn = document.getElementById('plagiarismBtn');
    const plagiarismResultDiv = document.getElementById('plagiarismResult');

    function sendQuestion() {
        const question = questionInput.value;
        if (question.trim() === '') return;

        const userQuestionDiv = document.createElement('div');
        userQuestionDiv.textContent = `You: ${question}`;
        conversation.appendChild(userQuestionDiv);

        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: question })
        })
        .then(response => response.json())
        .then(data => {
            const aiAnswerDiv = document.createElement('div');
            aiAnswerDiv.textContent = `AI: ${data.answer}`;
            conversation.appendChild(aiAnswerDiv);
            conversation.scrollTop = conversation.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
            const errorDiv = document.createElement('div');
            errorDiv.textContent = 'Error: Unable to get a response from the server.';
            conversation.appendChild(errorDiv);
        });

        questionInput.value = '';
    }

    function analyzeIntroduction() {
        const introduction = introductionInput.value;
        if (introduction.trim() === '') return;

        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ introduction: introduction })
        })
        .then(response => response.json())
        .then(data => {
            const analysisResultDiv = document.createElement('div');
            analysisResultDiv.textContent = `Analysis: ${data.analysis}`;
            analysisDiv.appendChild(analysisResultDiv);
            analysisDiv.scrollTop = analysisDiv.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
            const errorDiv = document.createElement('div');
            errorDiv.textContent = 'Error: Unable to get a response from the server.';
            analysisDiv.appendChild(errorDiv);
        });

        introductionInput.value = '';
    }

    function checkPlagiarism() {
        const text = plagiarismInput.value;
        if (text.trim() === '') return;

        fetch('/plagiarism_check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ introduction: text })
        })
        .then(response => response.json())
        .then(data => {
            const plagiarismResultDiv = document.createElement('div');
            plagiarismResultDiv.textContent = `Plagiarism Result: ${data.plagiarism_result}`;
            plagiarismResultDiv.appendChild(plagiarismResultDiv);
            plagiarismResultDiv.scrollTop = plagiarismResultDiv.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
            const errorDiv = document.createElement('div');
            errorDiv.textContent = 'Error: Unable to get a response from the server.';
            plagiarismResultDiv.appendChild(errorDiv);
        });

        plagiarismInput.value = '';
    }

    sendBtn.addEventListener('click', sendQuestion);
    questionInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendQuestion();
        }
    });

    analyzeBtn.addEventListener('click', analyzeIntroduction);
    plagiarismBtn.addEventListener('click', checkPlagiarism);
});
