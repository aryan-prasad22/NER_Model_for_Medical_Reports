# NER_Model_for_Medical_Reports
Model used: SpaCy
This project demonstrates how to create a web application using Flask that processes text for named entity recognition (NER) using a pre-trained spaCy model. The app can handle both text input and file uploads (JSON or text files) and visualizes the named entities in the text.

Prerequisites
To run this project, you need to have Python installed on your machine. It is recommended to use Python 3.6 or above.

Installation
Follow these steps to set up and run the application:

Clone the repository:

sh
git clone https://github.com/yourusername/NER_Project.git
cd NER_Project

Create and activate a virtual environment:

On Windows:
sh
python -m venv venv
venv\Scripts\activate

On macOS and Linux:
sh
python3 -m venv venv
source venv/bin/activate
Install the required packages:

sh

pip install -r requirements.txt
Download and place the pre-trained spaCy model:

Ensure you have the spaCy model saved at the specified path (E:\Projects\NER_Project\NER_medical_model). If the model is in another location, update the path in the script accordingly.

Run the application:
sh
python app.py
