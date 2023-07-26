# Import necessary libraries
import cv2
import os

# Define the directory where the face images will be stored
face_data = 'face_dataset'

# Name of the person for whom the face data is being collected
name = 'abhishek'

# Create a path combining the face_data directory and the person's name
path = os.path.join(face_data, name)

# Check if the path exists, if not, create the directory
if not os.path.isdir(path):
    os.mkdir(path)

# Set the dimensions for resizing the captured face images
(width, height) = (130, 100)

# Load the Haar cascade classifier for face detection
algo = 'haarcascade_frontalface_default.xml'
haar_cascade = cv2.CascadeClassifier(algo)

# Initialize the webcam for capturing images
cam = cv2.VideoCapture(0)

# Initialize the counter to keep track of the number of captured images
count = 1

# Capture 30 images of the person's face
while count < 31:
    print(count)
    
    # Read a frame from the webcam
    _, img = cam.read()
    
    # Convert the frame to grayscale for face detection
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    face = haar_cascade.detectMultiScale(gray_img, 1.3, 4)
    
    # Iterate over all detected faces
    for (x, y, w, h) in face:
        # Draw a green rectangle around the detected face on the original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 0)
        
        # Extract the face region from the grayscale image
        faceonly = gray_img[y:y + h, x:x + w]
        
        # Resize the face region to the specified dimensions
        resize_img = cv2.resize(faceonly, (width, height))
        
        # Save the resized face image in the specified path
        cv2.imwrite('%s/%s.jpg' % (path, count), faceonly)
        
        # Increment the counter for the next image
        count += 1

    # Display the original image with detected faces
    cv2.imshow('FaceDetection', img)
    
    # Wait for a key press for a short duration (10 milliseconds)
    key = cv2.waitKey(10)
    
    # If the key '0' is pressed, break out of the loop
    if key == 0:
        break

# After capturing all the images, print a success message
print('Image captured successfully')

# Release the webcam
cam.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

        
