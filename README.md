
# On-Device Voice Command Recognition

This project is an on-device voice command recognition system, designed for real-time performance on mobile devices. It enables smart home devices to respond to basic voice commands without internet dependency, enhancing user privacy and improving response speed.

## Project Structure

- **coreml.py** - Manages Core ML model conversion for iOS deployment.
- **data.py** - Handles data preprocessing, augmentation, and preparation for training.
- **deploy.swift** - Swift file for integrating the model into an iOS application.
- **inference.py** - Contains inference logic to perform real-time voice command recognition.
- **libraries.py** - Loads required libraries and provides environment configurations.
- **model.py** - Defines and trains the voice recognition model.
- **quantisation.py** - Quantizes the model to optimize performance for mobile devices.
- **README.md** - Provides a project overview and setup instructions.
- **requirements.txt** - Lists required Python dependencies.

## Features

- **Offline Voice Command Recognition**: Performs command recognition without an internet connection.
- **Optimized for On-Device Performance**: Lightweight model architecture allows quick command processing.
- **Low Latency**: Processes voice commands in real-time (sub-100ms latency).
- **Privacy-Centric**: Local data processing enhances user privacy.

## Installation

1. Clone this repository to your local machine.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Data Preprocessing

Use `data.py` to prepare and augment your dataset:
```bash
python data.py
```

### Model Training

Train the voice recognition model using `model.py`:
```bash
python model.py
```

### Model Conversion and Quantization

Convert the trained model to Core ML format for iOS deployment and quantize it for efficiency:
```bash
python coreml.py
python quantisation.py
```

### Running Inference

Run `inference.py` to perform real-time voice command recognition:
```bash
python inference.py
```

### iOS Deployment

Use `deploy.swift` to integrate the trained model into an iOS application.

## Requirements

- Python 3.x
- Core ML
- TensorFlow Lite
- Additional libraries (see `requirements.txt`)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
