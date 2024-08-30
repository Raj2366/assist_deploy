document.getElementById('speakBtn').addEventListener('click', function() {
    fetch('/command', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').textContent = data.response;
    })
    .catch(error => console.error('Error:', error));
});
