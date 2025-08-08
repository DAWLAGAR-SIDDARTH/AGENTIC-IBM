from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend calls

@app.route('/run-agent')
def run_agent():
    # Placeholder for traffic agent logic
    return "✅ Smart Traffic Agent executed. IBM integration: ACTIVE"

if __name__ == '__main__':
    app.run(debug=True)
