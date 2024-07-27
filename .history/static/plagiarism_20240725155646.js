document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('plagiarismForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const text1 = document.getElementById('text1').value;
        const text2 = document.getElementById('text2').value;

        fetch('/check_plagiarism', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text1: text1, text2: text2 })
        })
        .then(response => response.json())
        .then(data => {
            const similarity = data.similarity;
            resultDiv.textContent = `Similarity: ${(similarity * 100).toFixed(2)}%`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.textContent = 'Error: Unable to check similarity.';
        });
    });
});
