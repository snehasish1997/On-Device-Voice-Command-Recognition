import tfcoreml

# Path for the TFLite model
tflite_model_path = 'voice_command_model.tflite'
# Output path for the Core ML model
coreml_model_path = 'VoiceCommandModel.mlmodel'

# Convert TFLite to Core ML
coreml_model = tfcoreml.convert(
    tf_model_path=tflite_model_path,
    mlmodel_path=coreml_model_path,
    input_name_shape_dict={'input': [1, 13, 1]},  # Adjust based on the model input shape
    output_feature_names=['output']
)
