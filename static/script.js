document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('file-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    // Display uploaded image before sending to server
    const file = fileInput.files[0];
    const reader = new FileReader();
    
    reader.onloadend = () => {
        const uploadedImage = document.getElementById('uploaded-image');
        uploadedImage.src = reader.result;
        uploadedImage.style.display = 'block'; // Show image
    };
    
    if (file) {
        reader.readAsDataURL(file); // This will trigger the onloadend event
    }

    try {
        const response = await fetch('/classify', {
            method: 'POST',
            body: formData,
        });
        const data = await response.json();
        document.getElementById('result').textContent = `Classification Result: ${data.result}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'An error occurred. Please try again.';
    }
});
