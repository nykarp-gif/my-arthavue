from flask import Flask, render_template, jsonify
from brain import run_arthavue_brain # This connects to your math file

app = Flask(__name__)

@app.route('/')
def home():
    # This sends your Arthavue HTML file to the browser
    return render_template('index.html')

@app.route('/get-data')
def get_data():
    # This sends the "Brain" result to the website as data
    result = run_arthavue_brain()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
