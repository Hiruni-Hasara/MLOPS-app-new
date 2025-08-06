from flask import Flask, request, jsonify, send_from_directory
import joblib
import os

app = Flask(__name__, static_folder='frontend')
model = joblib.load("model.pkl")

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()
        features = input_data["features"]
        prediction = model.predict([features])[0]
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
