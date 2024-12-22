from flask import Flask, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route("/analyze/<string:text>", methods=["GET"])  # Accept text as a URL parameter
def analyze(text):
    try:
        # Perform sentiment analysis
        result = sentiment_pipeline(text)
        return jsonify({
            "sentiment": result[0]["label"],
            "confidence": result[0]["score"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

