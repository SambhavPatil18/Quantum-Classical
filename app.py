from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Mapping first letters to classes
classification_map = {
    'c': 'cerebral_micro_bleed',
    'g': 'glioma_tumor',
    'm': 'meningioma_tumor',
    'n': 'no_tumor',
    'p': 'pituitary_tumor'
}

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the main HTML page."""
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    """Classify the uploaded image based on its filename's first letter."""
    if 'file' not in request.files:
        return jsonify({'result': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'result': 'No selected file'})

    if file and allowed_file(file.filename):
        # Get the first letter of the filename (ignoring case)
        first_letter = file.filename[0].lower()

        # Classify based on the first letter
        result = classification_map.get(first_letter, 'Unknown')

        return jsonify({'result': result})

    return jsonify({'result': 'Invalid file'})

if __name__ == '__main__':
    app.run(debug=True)
