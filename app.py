from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # Allow your frontend to call this API

# Set your OpenAI API key (replace with your real key)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/workout", methods=["GET"])
def generate_workout():
    goal = request.args.get("goal", "general fitness")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a personal fitness coach."},
                {"role": "user", "content": f"Create a 3-day workout plan for someone with goal: {goal}"}
            ],
            temperature=0.7
        )
        workout = response.choices[0].message.content
        return jsonify({"workout": workout})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)