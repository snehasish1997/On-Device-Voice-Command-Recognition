# Import necessary libraries
import os
import numpy as np
import librosa
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout

# Set up paths and constants
DATASET_PATH = 'path to the dataset'  # Path where audio files are stored
TARGET_CLASSES = ['yes', 'no', 'up', 'down', 'left', 'right', 'on', 'off', 'stop', 'go']  # all command classes are defined here
SAMPLE_RATE = 16000  # 16kHz sample rate
