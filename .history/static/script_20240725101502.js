document.addEventListener('DOMContentLoaded', function() {
    const questionInput = document.getElementById('question');
    const sendBtn = document.getElementById('sendBtn');
    const conversation = document.getElementById('conversation');

    function sendQuestion() {
        const question = questionInput.value;
        if (question.trim() === '') return;

        // 사용자 질문 화면에 출력
        const userQuestionDiv = document.createElement('div');
        userQuestionDiv.textContent = `You: ${question}`;
        conversation.appendChild(userQuestionDiv);

        // HTTP 요청 보내기
        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: question })
        })
        .then(response => response.json())
        .then(data => {
            // AI의 답변 화면에 출력
            const aiAnswerDiv = document.createElement('div');
            aiAnswerDiv.textContent = `AI: ${data.answer}`;
            conversation.appendChild(aiAnswerDiv);

            // 스크롤을 맨 아래로
            conversation.scrollTop = conversation.scrollHeight;
        });

        // 입력창 초기화
        questionInput.value = '';
    }

    // 버튼 클릭 이벤트 핸들러
    sendBtn.addEventListener('click', sendQuestion);

    // Enter 키 입력 이벤트 핸들러
    questionInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendQuestion();
        }
    });
});
