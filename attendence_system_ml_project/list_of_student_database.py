import os
import face_recognition

known_face_names = []

# Path to folder containing images
image_folder = os.path.join(os.getcwd(), 'images')

# Load images from the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        image_path = os.path.join(image_folder, filename)
        known_face_names.append(os.path.splitext(filename)[0])  # Get the filename without extension
        
        

for i in known_face_names:
    print(i)