# Face-detection-using-Haar-Cascade-algorithm-and-openCV
The Face Dataset Collection Project is a Python-based program that allows users to capture and save images of a person's face using a webcam. The collected face images can be used for various applications, such as training machine learning models for face recognition.
# Requirements

    Python 3.x
    OpenCV (cv2) library
    Haar cascade classifier file for face detection (provided as haarcascade_frontalface_default.xml)

# Installation

    Clone or download the repository to your local machine.

    Install the required dependencies using the following command:

    pip install opencv-python

    Ensure you have the Haar cascade classifier file (haarcascade_frontalface_default.xml) available in the project directory.

# Usage

    Open a terminal or command prompt and navigate to the project directory.

    Run the script face_dataset_collection.py using Python:

    python face_dataset_collection.py

    The script will open the webcam and start capturing face images of the person specified by the variable name in the script. The default name is set to 'abhishek', but you can change it to any desired name.

    The script will capture 30 face images by default. You can change this number by modifying the loop condition in the script.

    Detected faces will be surrounded by a green rectangle in the displayed webcam window.

    The captured face images will be saved in a folder named after the specified person's name under the 'face_dataset' directory.

    Press any key to stop capturing images before reaching the specified count.

# Customization

    You can change the dimensions of the captured face images by modifying the width and height variables in the script.
    To capture face images for a different person, simply change the value of the name variable in the script.
