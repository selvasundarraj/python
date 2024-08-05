document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file', document.getElementById('fileInput').files[0]);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    const resultDiv = document.getElementById('result');
    if (result.error) {
        resultDiv.innerHTML = ⁠ <p>Error: ${result.error}</p> ⁠;
    } else {
        resultDiv.innerHTML = ⁠ <a href="${result.downloadLink}">Download CSV</a> ⁠;
    }
});
