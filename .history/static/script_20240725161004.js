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

function generateResume() {
    const form = document.getElementById('resumeForm');
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => data[key] = value);

    fetch('/resume', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.result === 'success') {
            window.open(data.pdf, '_blank');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
