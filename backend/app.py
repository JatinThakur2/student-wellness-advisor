
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import requests

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})

# Load the trained model
model = joblib.load('backend/wellness_model.joblib')

def get_llm_summary(anxiety_score, depression_score, life_satisfaction):
    prompt = f"""
    Based on the following wellness scores:
    - Anxiety Score: {anxiety_score:.2f}
    - Depression Score: {depression_score:.2f}
    - Life Satisfaction: {life_satisfaction:.2f}

    Please provide a brief summary of the user's well-being and suggest 3-5 actionable steps they can take to improve their mental health and life satisfaction.
    The tone should be supportive and encouraging.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "deepseek-r1:1.5b", "prompt": prompt, "stream": False}
        )
        if response.ok:
            return response.json()["response"]
        else:
            return "Could not generate summary."
    except Exception as e:
        return f"Error generating summary: {e}"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json(force=True)

    # Create a pandas DataFrame from the input data
    df = pd.DataFrame(data, index=[0])

    # Make a prediction using the loaded model
    prediction = model.predict(df)

    anxiety_score = prediction[0][0]
    depression_score = prediction[0][1]
    life_satisfaction = prediction[0][2]

    summary = get_llm_summary(anxiety_score, depression_score, life_satisfaction)

    # Prepare the response
    response = {
        'anxiety_score': anxiety_score,
        'depression_score': depression_score,
        'life_satisfaction': life_satisfaction,
        'summary': summary
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
