import cv2
import numpy as np


def preprocess_image(image_path):
    """
    Preprocess an image for CNN prediction.

    Steps:
    1. Read image from disk
    2. Convert BGR to RGB
    3. Resize to 224x224
    4. Normalize pixel values
    5. Expand dimensions for model input

    Returns:
        image_array (numpy.ndarray): Shape (1, 224, 224, 3)
    """

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Invalid image path or unreadable image")

    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize image
    image = cv2.resize(image, (224, 224))

    # Normalize
    image = image / 255.0

    # Convert to numpy array
    image_array = np.array(image, dtype=np.float32)

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    return image_array
