def load_audio_files(dataset_path, target_classes):
    data = []
    labels = []
    
    for label, class_name in enumerate(target_classes):
        class_path = os.path.join(dataset_path, class_name)
        
        for file_name in os.listdir(class_path):
            if file_name.endswith('.wav'):
                file_path = os.path.join(class_path, file_name)
                
                # Load audio file and preprocess
                y, sr = librosa.load(file_path, sr=SAMPLE_RATE)
                
                # Extract MFCC features
                mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
                mfcc = np.mean(mfcc.T, axis=0)  # Average over time axis
                
                data.append(mfcc)
                labels.append(label)
    
    return np.array(data), np.array(labels)

# Load dataset
data, labels = load_audio_files(DATASET_PATH, TARGET_CLASSES)

# Convert labels to categorical format
labels = to_categorical(labels, num_classes=len(TARGET_CLASSES))

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
