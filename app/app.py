from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import os
import re

# ---------------------------
# Setup Flask
# ---------------------------
app = Flask(__name__)
app.secret_key = "secret123"   # needed for flash messages

# ---------------------------
# Load model & vectorizer
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "../model/model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "../model/vectorizer.pkl"))

# ---------------------------
# Store history (last 5)
# ---------------------------
history = []

# ---------------------------
# Preprocessing
# ---------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

# ---------------------------
# Simple explanation
# ---------------------------
def get_keywords(text):
    words = text.split()
    return " ".join(words[:5])  # first 5 words

# ---------------------------
# Main route
# ---------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("review")

        # ❌ Empty input check
        if not user_input or user_input.strip() == "":
            flash("⚠ Please enter a review before analyzing")

            # 🔥 CLEAR OLD RESULT
            app.config["prediction"] = None
            app.config["explanation"] = None

            return redirect(url_for("home"))

        # ✔ Clean and predict
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        pred = model.predict(vector)[0]

        # Map prediction
        if pred == 0:
            prediction = "Negative 😡"
        elif pred == 1:
            prediction = "Neutral 😐"
        else:
            prediction = "Positive 😊"

        # Explanation
        explanation = get_keywords(cleaned)

        # Store history
        history.insert(0, (user_input, prediction))
        if len(history) > 5:
            history.pop()

        # Save result temporarily
        app.config["prediction"] = prediction
        app.config["explanation"] = explanation

        # Redirect (prevents duplicate on refresh)
        return redirect(url_for("home"))

    # GET request
    return render_template(
        "index.html",
        prediction=app.config.get("prediction"),
        explanation=app.config.get("explanation"),
        history=history
    )

# ---------------------------
# Run app
# ---------------------------
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)