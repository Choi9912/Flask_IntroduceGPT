document.addEventListener('DOMContentLoaded', function() {
    const sendBtn = document.getElementById('sendBtn');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const plagiarismBtn = document.getElementById('plagiarismBtn');
    const spellCheckBtn = document.getElementById('spellCheckBtn');
    const actionBtn = document.getElementById('actionBtn');
    const inputArea = document.getElementById('inputArea');
    const outputDiv = document.getElementById('output');

    let currentAction = null;

    sendBtn.addEventListener('click', () => {
        currentAction = 'generate';
        inputArea.placeholder = 'Enter your question here';
    });

    analyzeBtn.addEventListener('click', () => {
        currentAction = 'analyze';
        inputArea.placeholder = 'Enter your self-introduction here';
    });

    plagiarismBtn.addEventListener('click', () => {
        currentAction = 'plagiarism_check';
        inputArea.placeholder = 'Enter your text for plagiarism check';
    });

    spellCheckBtn.addEventListener('click', () => {
        currentAction = 'spell_check';
        inputArea.placeholder = 'Enter your text for spell check';
    });

    actionBtn.addEventListener('click', () => {
        const text = inputArea.value;
        if (text.trim() === '' || !currentAction) return;

        let url;
        const body = { text: text };

        switch (currentAction) {
            case 'generate':
                url = '/generate';
                body.question = text;
                delete body.text;
                break;
            case 'analyze':
                url = '/analyze';
                body.introduction = text;
                delete body.text;
                break;
            case 'plagiarism_check':
                url = '/plagiarism_check';
                body.method = 'iterative_refinement'; // 예: 원하는 방법을 지정
                break;
            case 'spell_check':
                url = '/spell_check';
                break;
            default:
                return;
        }

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
            let resultText;
            if (currentAction === 'generate') {
                resultText = `Generated Response: ${data.answer || 'No response'}`;
            } else if (currentAction === 'analyze') {
                resultText = `Analysis Result: ${data.analysis || 'No response'}`;
            } else if (currentAction === 'plagiarism_check') {
                resultText = `Plagiarism Report: ${data.plagiarism_report.map(report => `\nKnown Text: ${report.known_text}\nSimilarity: ${report.similarity}\nIs Plagiarized: ${report.is_plagiarized}`).join('\n\n') || 'No report'}`;
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
