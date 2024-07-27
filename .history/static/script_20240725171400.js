document.addEventListener('DOMContentLoaded', function() {
    const questionInput = document.getElementById('question');
    const sendBtn = document.getElementById('sendBtn');
    const conversation = document.getElementById('conversation');

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

    sendBtn.addEventListener('click', sendQuestion);
    questionInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendQuestion();
        }
    });
});


function checkSpelling() {
    const text = document.getElementById('generatedIntro').textContent;
    fetch('/check_spelling', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('spellingResult').textContent = JSON.stringify(data.corrections, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('spellingResult').textContent = 'Error: Unable to check spelling';
    });
}

function checkSimilarity() {
    const text1 = document.getElementById('generatedIntro').textContent;
    const text2 = document.getElementById('textToCompare').value;

    fetch('/check_similarity', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text1: text1, text2: text2 })
    })
    .then(response => response.json())
    .then(data => {
        const similarity = data.similarity;
        document.getElementById('similarityResult').textContent = `유사도: ${(similarity * 100).toFixed(2)}%`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('similarityResult').textContent = 'Error: Unable to check similarity';
    });
}