document.addEventListener('DOMContentLoaded', function() {
    const sendBtn = document.getElementById('sendBtn');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const plagiarismBtn = document.getElementById('plagiarismBtn');
    const spellCheckBtn = document.getElementById('spellCheckBtn');
    const actionBtn = document.getElementById('actionBtn');
    const inputArea = document.getElementById('inputArea');
    const chatBox = document.getElementById('chat-box');

    let currentAction = null;

    sendBtn.addEventListener('click', () => {
        currentAction = 'generate';
        inputArea.placeholder = 'Enter your question here';
        appendMessage('bot', '자기소개서 작성 기능을 선택하셨습니다.');
    });

    analyzeBtn.addEventListener('click', () => {
        currentAction = 'analyze';
        inputArea.placeholder = 'Enter your self-introduction here';
        appendMessage('bot', '자기소개서 분석 기능을 선택하셨습니다.');
    });

    plagiarismBtn.addEventListener('click', () => {
        currentAction = 'plagiarism_check';
        inputArea.placeholder = 'Enter your text for plagiarism check';
        appendMessage('bot', '카피킬러 기능을 선택하셨습니다.');
    });

    spellCheckBtn.addEventListener('click', () => {
        currentAction = 'spell_check';
        inputArea.placeholder = 'Enter your text for spell check';
        appendMessage('bot', '맞춤법 검사 기능을 선택하셨습니다.');
    });

    actionBtn.addEventListener('click', () => {
        const text = inputArea.value;
        if (text.trim() === '' || !currentAction) return;

        let url;
        const body = {};

        switch (currentAction) {
            case 'generate':
                url = '/generate';
                body.question = text;
                break;
            case 'analyze':
                url = '/analyze';
                body.introduction = text;
                break;
            case 'plagiarism_check':
                url = '/plagiarism_check';
                body.text = text;
                break;
            case 'spell_check':
                url = '/spell_check';
                body.text = text;
                break;
            default:
                return;
        }

        console.log(`Sending request to ${url} with body:`, body);  

        actionBtn.disabled = true;
        appendMessage('user', text);
        inputArea.value = '';

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Received response:', data);  
            let resultText;
            switch (currentAction) {
                case 'generate':
                    resultText = data.answer || 'No response';
                    break;
                case 'analyze':
                    resultText = data.analysis || 'No response';
                    break;
                case 'plagiarism_check':
                    resultText = data.plagiarism_report || 'No report';
                    break;
                case 'spell_check':
                    resultText = data.spell_check_report || 'No report';
                    break;
                default:
                    resultText = 'No valid action performed.';
            }
            appendParagraphs('bot', resultText);
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('bot', 'Error: Unable to get a response from the server.');
        })
        .finally(() => {
            // Re-enable the action button
            actionBtn.disabled = false;
        });
    });

    function appendMessage(sender, message) {
        let messageElement = document.createElement('div');
        messageElement.classList.add('chat-message', sender);
        messageElement.textContent = message;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function appendParagraphs(sender, text) {
        const paragraphs = text.split('\n\n');
        paragraphs.forEach(paragraph => {
            appendMessage(sender, paragraph);
        });
    }
});
