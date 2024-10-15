# Malaria Detection using Transfer Learning with ResNet-50v2

## Project Overview

This project implements an advanced approach for malaria cell-image classification using the ResNet-50v2 architecture and transfer learning techniques. The system is designed to accurately classify blood cell images as either "Parasitized" or "Uninfected", aiding in the early detection and diagnosis of malaria.

## Features

- Utilizes ResNet-50v2 architecture pre-trained on ImageNet dataset
- Implements transfer learning for efficient model training
- Achieves high accuracy in classifying malaria cell images
- Provides a web-based interface for easy interaction with the model

## Technical Specifications

- **Programming Language**: Python 3.9.16
- **Deep Learning Libraries**: TensorFlow 2.12, Keras
- **Machine Learning Libraries**: Scikit-Learn, NumPy, Pandas
- **Image Processing**: OpenCV
- **Data Visualization**: Matplotlib
- **Web Framework**: Flask
- **Front-end**: HTML, CSS, JavaScript

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/arjunvs903/malaria-detection.git
   cd malaria-detection
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   it is located on **Malaria Detector** folder
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`.

3. Upload a blood cell image through the web interface to get the classification result.

## Model Training

To retrain the model or experiment with different configurations:

1. Ensure you have the dataset in the correct directory structure:
   ```
   dataset/
   ├── train/
   │   ├── parasitized/
   │   └── uninfected/
   ├── val/
   │   ├── parasitized/
   │   └── uninfected/
   └── test/
       ├── parasitized/
       └── uninfected/
   ```

2. Run the training script:
   ```
   open train_model.ipynb on jupyter notebook or vs code 
   then run each cell one by one
   ```

## Performance

The model achieves the following performance metrics:

- Training Accuracy: 94.85%
- Training Loss: 13.30%
- Test Accuracy: 94.07%
- Test Loss: 16.24%


## Acknowledgments

- National Library of Medicine for providing the dataset
- Malaria Cell Atlas for additional data resources
