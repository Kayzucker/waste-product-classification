import os
from flask import Flask, render_template, request
from utils.preprocess import preprocess_image
from utils.model_loader import load_model_and_labels
import numpy as np

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load model and labels ONCE
model, labels = load_model_and_labels()


@app.route("/", methods=["GET", "POST"])
def home():
    uploaded_image = None
    prediction = None
    confidence = None

    if request.method == "POST":
        file = request.files.get("image")

        if file and file.filename != "":
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            uploaded_image = file.filename

            # Preprocess image
            image_array = preprocess_image(file_path)

            # Predict
            preds = model.predict(image_array)
            predicted_index = np.argmax(preds)
            prediction = labels[predicted_index]
            confidence = round(float(preds[0][predicted_index]) * 100, 2)

    return render_template(
        "index.html",
        uploaded_image=uploaded_image,
        prediction=prediction,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)
