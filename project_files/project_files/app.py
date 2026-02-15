from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("payments.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/submit", methods=["POST"])
def submit():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]

    prediction = model.predict(final_features)

    if prediction[0] == 1:
        result = "⚠️ Fraud Transaction Detected!"
    else:
        result = "✅ Legitimate Transaction"

    return render_template("submit.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
