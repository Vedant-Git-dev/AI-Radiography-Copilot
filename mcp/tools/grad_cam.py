from mcp.tools.classifier import model, preprocess_image
import tensorflow as tf
import cv2
import numpy as np

def get_grad_model():
    return tf.keras.models.Model(
        inputs=model.input,
        outputs=[
            model.get_layer("top_conv").output,
            model.output
        ]
    )

def compute_grad_cam(img):
    grad_model = get_grad_model()
    input_tensor = preprocess_image(img)

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(input_tensor)
        loss = predictions
        grads = tape.gradient(loss, conv_outputs)\
        
    weights = tf.reduce_mean(grads, axis=(0, 1, 2))

    cam = tf.reduce_sum(tf.multiply(weights, conv_outputs[0]), axis=-1)

    cam = tf.maximum(cam, 0)
    cam = cam / tf.reduce_max(cam)

    cam = cv2.resize(cam.numpy(), (224, 224))
    heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)

    original = input_tensor[0].numpy()
    original = (original * 255).astype(np.uint8)

    overlay = cv2.addWeighted(original, 0.6, heatmap, 0.4, 0)

    return overlay