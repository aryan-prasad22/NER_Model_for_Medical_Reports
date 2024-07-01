from flask import Flask, render_template, request
from spacy import displacy
import spacy
import json

app = Flask(__name__)

# Load the trained model
nlp_loaded = spacy.load("E:\\Projects\\NER_Project\\NER_medical_model")

def process_text(text):
    # Process the input text using the loaded model
    doc_loaded = nlp_loaded(text)

    # Extract named entities
    entities = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc_loaded.ents]

    # Generate HTML for visualization
    html = displacy.render(doc_loaded, style="ent", options={"colors": {"PATHOGEN": "#F67DE3", "MEDICINE": "#7DF6D9", "MEDICALCONDITION": "#a6e22d"}})

    return html, entities

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                app.logger.info('File received: %s', file.filename)
                # Check file type
                if file.filename.endswith('.json'):
                    # Read JSON file
                    data = json.load(file)
                    if isinstance(data, dict):
                        text = " ".join(str(v) for v in data.values())
                    elif isinstance(data, list):
                        text = " ".join(str(item) for sublist in data for item in sublist)
                    else:
                        return "Error: Invalid JSON format.", 400
                else:
                    # Read the uploaded file
                    text = file.read().decode('utf-8')
                app.logger.info('File content: %s', text)
                # Process the text
                html, entities = process_text(text)
                return render_template('index.html', text=text, visualization=html, entities=entities)

        # If file is not uploaded or other form data is submitted, handle it as text input
        text = request.form['text']
        app.logger.info('Text input: %s', text)
        html, entities = process_text(text)
        return render_template('index.html', text=text, visualization=html, entities=entities)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
