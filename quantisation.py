# Convert the Keras model to TensorFlow Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Apply default quantization
tflite_model = converter.convert()

# Save the model
with open('voice_command_model.tflite', 'wb') as f:
    f.write(tflite_model)
