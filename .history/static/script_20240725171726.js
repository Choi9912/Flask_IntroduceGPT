function generateIntro() {
    const form = document.getElementById('introForm');
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => data[key] = value);

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('generatedIntro').textContent = data.answer;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('generatedIntro').textContent = 'Error: Unable to generate the introduction';
    });
}

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
