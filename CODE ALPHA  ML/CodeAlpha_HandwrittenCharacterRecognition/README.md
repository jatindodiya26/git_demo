# CodeAlpha - Handwritten Character Recognition (MNIST)

## Objective
Build a deep learning model to recognize handwritten digits from images using a Convolutional Neural Network (CNN).

This project is completed as part of the **CodeAlpha Machine Learning Internship (Task 3: Handwritten Character Recognition)**.

## Dataset
- **MNIST** handwritten digit dataset (0–9)
- Loaded directly from TensorFlow/Keras:
  - `tf.keras.datasets.mnist.load_data()`

## Approach
1. Load MNIST dataset
2. Preprocess:
   - Normalize pixel values to range [0, 1]
   - Reshape to include channel dimension: `(28, 28, 1)`
3. Model:
   - CNN with Conv2D + MaxPooling layers
   - Dense layer + Dropout for better generalization
   - Output layer: 10 classes with Softmax
4. Train and evaluate on test set
5. Save trained model to disk

## Project Structure
```text
CodeAlpha_HandwrittenCharacterRecognition/
  mnist_cnn.py
  requirements.txt
  README.md

  Model training was executed on Google Colab due to TensorFlow compatibility issues on local Python 3.14; source code is provided as a Python script and can also be run locally with Python 3.11/3.12.