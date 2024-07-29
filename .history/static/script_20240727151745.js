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
                break;
            case 'spell_check':
                url = '/spell_check';
                break;
            default:
                return;
        }

        // Disable the action button and show loading indicator
        actionBtn.disabled = true;
        outputDiv.innerHTML = '<p>Loading...</p>';

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        })
        .then(response => response.json())
        .then(data => {
            let resultHTML = '';
            if (currentAction === 'generate') {
                resultHTML = `<h3>Generated Response:</h3><p>${data.answer || 'No response'}</p>`;
            } else if (currentAction === 'analyze') {
                resultHTML = `<h3>Analysis Result:</h3><p>${data.analysis || 'No response'}</p>`;
            } else if (currentAction === 'plagiarism_check') {
                const report = data.plagiarism_report;
                if (typeof report === 'object' && report !== null) {
                    resultHTML = `
                        <h3>Plagiarism Report:</h3>
                        <p><strong>Similarity Score:</strong> ${report.similarity_score}</p>
                        <p><strong>AI Analysis:</strong> ${report.ai_analysis}</p>
                        <p><strong>Preprocessed Text:</strong> ${report.preprocessed_text}</p>
                    `;
                } else {
                    resultHTML = `<p>Plagiarism Report: ${report || 'No report'}</p>`;
                }
            } else if (currentAction === 'spell_check') {
                resultHTML = `<h3>Spell Check Report:</h3><p>${data.spell_check_report || 'No report'}</p>`;
            }
            outputDiv.innerHTML = resultHTML;
        })
        .catch(error => {
            console.error('Error:', error);
            outputDiv.innerHTML = '<p>Error: Unable to get a response from the server.</p>';
        })
        .finally(() => {
            // Re-enable the action button and clear the input
            actionBtn.disabled = false;
            inputArea.value = '';
        });
    });
});