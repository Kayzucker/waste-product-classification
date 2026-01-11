import tensorflow as tf

MODEL_PATH = "models/model.h5"
LABELS_PATH = "models/labels.txt"


def load_model_and_labels():
    """
    Loads the trained model and class labels.
    Returns:
        model: Loaded TensorFlow model
        labels: List of class labels
    """
    model = tf.keras.models.load_model(MODEL_PATH)

    with open(LABELS_PATH, "r") as f:
        labels = [line.strip() for line in f.readlines()]

    return model, labels
