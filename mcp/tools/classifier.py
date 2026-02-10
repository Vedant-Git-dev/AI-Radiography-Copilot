from tensorflow.keras.models import load_model
import tensorflow as tf
import os

def preprocess_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3, expand_animations=False)
    img = tf.image.resize(img, (224, 224))
    img = tf.cast(img, tf.float32) / 255.0
    img = tf.expand_dims(img, axis = 0)

    return img

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",        
    "..",        
    "models",
    "efficient_net_classifier.keras"
)

MODEL_PATH = os.path.abspath(MODEL_PATH)

print(MODEL_PATH)
print(os.path.exists(MODEL_PATH))

model = load_model(MODEL_PATH)

def run_classifier(img):
    img = preprocess_image(img)
    prob = model.predict(img)[0][0]

    return prob