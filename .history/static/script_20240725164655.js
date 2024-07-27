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
        document.getElementById('spellingResult').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('spellingResult').textContent = 'Error: Unable to check spelling';
    });
}
