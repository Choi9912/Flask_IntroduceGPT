document.addEventListener('DOMContentLoaded', function() {
    const sendBtn = document.getElementById('sendBtn');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const plagiarismBtn = document.getElementById('plagiarismBtn');
    const spellCheckBtn = document.getElementById('spellCheckBtn');
    const actionBtn = document.getElementById('actionBtn');
    const inputArea = document.getElementById('inputArea');
    const methodSelect = document.getElementById('methodSelect');  // 추가된 선택 박스
    const outputDiv = document.getElementById('output');

    let currentAction = null;

    sendBtn.addEventListener('click', () => {
        currentAction = 'generate';
        inputArea.placeholder = 'Enter your question here';
        methodSelect.style.display = 'none';  // 방법 선택 숨기기
    });

    analyzeBtn.addEventListener('click', () => {
        currentAction = 'analyze';
        inputArea.placeholder = 'Enter your self-introduction here';
        methodSelect.style.display = 'block';  // 방법 선택 보이기
    });

    plagiarismBtn.addEventListener('click', () => {
        currentAction = 'plagiarism_check';
        inputArea.placeholder = 'Enter your text for plagiarism check';
        methodSelect.style.display = 'block';  // 방법 선택 보이기
    });

    spellCheckBtn.addEventListener('click', () => {
        currentAction = 'spell_check';
        inputArea.placeholder = 'Enter your text for spell check';
        methodSelect.style.display = 'block';  // 방법 선택 보이기
    });

    actionBtn.addEventListener('click', () => {
        const text = inputArea.value;
        const method = methodSelect.value;  // 선택된 방법
        if (text.trim() === '' || !currentAction) return;

        let url;
        const body = { text: text, method: method };  // method 추가

        switch (currentAction) {
            case 'generate':
                url = '/generate';
                body.question = text;
                delete body.text;
                delete body.method;  // method 제거
                break;
            case 'analyze':
                url = '/analyze';
                body.introduction = text;
                delete body.text;
                break;
            case 'plagiarism_check':
                url = '/plagiarism_check';
                break;
            case 'spell_check':
                url = '/spell_check';
                break;
            default:
                return;
        }

        console.log(`Sending request to ${url} with body:`, body);  // 디버그 로그 추가

        // Disable the action button and show loading indicator
        actionBtn.disabled = true;
        outputDiv.textContent = 'Loading...';

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Received response:', data);  // 디버그 로그 추가
            let resultText;
            if (currentAction === 'generate') {
                resultText = `Generated Response: ${data.answer || 'No response'}`;
            } else if (currentAction === 'analyze') {
                resultText = `Analysis Result: ${data.analysis || 'No response'}`;
            } else if (currentAction === 'plagiarism_check') {
                resultText = `Plagiarism Report: ${data.plagiarism_report || 'No report'}`;
            } else if (currentAction === 'spell_check') {
                resultText = `Spell Check Report: ${data.spell_check_report || 'No report'}`;
            }
            outputDiv.textContent = resultText;
        })
        .catch(error => {
            console.error('Error:', error);
            outputDiv.textContent = 'Error: Unable to get a response from the server.';
        })
        .finally(() => {
            // Re-enable the action button and clear the input
            actionBtn.disabled = false;
            inputArea.value = '';
        });
    });
});