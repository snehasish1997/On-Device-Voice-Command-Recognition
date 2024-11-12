import tensorflow as tf

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="voice_command_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensor details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Function to run inference on an audio file
def predict_command(file_path):
    # Preprocess the audio file
    y, sr = librosa.load(file_path, sr=SAMPLE_RATE)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc = np.mean(mfcc.T, axis=0)
    mfcc = mfcc.reshape(1, 13, 1).astype(np.float32)  # Reshape and cast to float32
    
    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], mfcc)
    
    # Run inference
    interpreter.invoke()
    
    # Get output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_index = np.argmax(output_data)
    
    # Return the predicted command
    return TARGET_CLASSES[predicted_index]

# as file is very big , i am not able to paste the file, we need to provide the path location here
print(predict_command("here we have to provide the path for the file test_audio.wav"))
