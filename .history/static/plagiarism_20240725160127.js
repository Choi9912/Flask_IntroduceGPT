document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('plagiarismForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const text = document.getElementById('text').value;

        fetch('/check_plagiarism', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        })
        .then(response => response.json())
        .then(data => {
            if (data.similarity) {
                resultDiv.textContent = `Similarity: ${(data.similarity * 100).toFixed(2)}%`;
            } else if (data.error) {
                resultDiv.textContent = `Error: ${data.error}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.textContent = 'Error: Unable to check similarity.';
        });
    });
});
