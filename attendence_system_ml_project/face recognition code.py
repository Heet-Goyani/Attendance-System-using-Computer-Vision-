import face_recognition
# import cv2
# import numpy as np
# import os
# import xlwt
# from xlwt import Workbook
# from datetime import date
# import xlrd, xlwt
# from xlutils.copy import copy as xl_copy

# CurrentFolder = os.getcwd() #Read current folder path
# image = CurrentFolder+'\\rahul.png'
# image2 = CurrentFolder+'\\sneha.png'


# # This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# # other example, but it includes some basic performance tweaks to make things run a lot faster:
# #   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
# #   2. Only detect faces in every other frame of video.

# # PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# # OpenCV is not required to use the face_recognition library. It's only required if you want to run this
# # specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# # Get a reference to webcam #0 (the default one)
# video_capture = cv2.VideoCapture(0)

# # Load a sample picture and learn how to recognize it.
# person1_name = "Rahul"
# person1_image = face_recognition.load_image_file(image)
# person1_face_encoding = face_recognition.face_encodings(person1_image)[0]

# # Load a second sample picture and learn how to recognize it.
# person2_name = "sneha"
# person2_image = face_recognition.load_image_file(image2)
# person2_face_encoding = face_recognition.face_encodings(person2_image)[0]

# # Create arrays of known face encodings and their names
# known_face_encodings = [
#     person1_face_encoding,
#     person2_face_encoding
# ]
# known_face_names = [
#     person1_name,
#     person2_name
# ]

# # Initialize some variables
# face_locations = []
# face_encodings = []
# face_names = []
# process_this_frame = True

# rb = xlrd.open_workbook('attendence_excel.xls', formatting_info=True) 
# wb = xl_copy(rb)
# inp = input('Please give current subject lecture name')
# sheet1 = wb.add_sheet(inp)
# sheet1.write(0, 0, 'Name/Date')
# sheet1.write(0, 1, str(date.today()))
# row=1
# col=0
# already_attendence_taken = ""
# while True:
#             # Grab a single frame of video
#             ret, frame = video_capture.read()

#             # Resize frame of video to 1/4 size for faster face recognition processing
#             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

#             # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#             rgb_small_frame = small_frame[:, :, ::-1]

#             # Only process every other frame of video to save time
#             if process_this_frame:
#                 # Find all the faces and face encodings in the current frame of video
#                 face_locations = face_recognition.face_locations(rgb_small_frame)
#                 face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#                 face_names = []
#                 for face_encoding in face_encodings:
#                     # See if the face is a match for the known face(s)
#                     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                     name = "Unknown"

#                     # # If a match was found in known_face_encodings, just use the first one.
#                     # if True in matches:
#                     #     first_match_index = matches.index(True)
#                     #     name = known_face_names[first_match_index]

#                     # Or instead, use the known face with the smallest distance to the new face
#                     face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#                     best_match_index = np.argmin(face_distances)
#                     if matches[best_match_index]:
#                         name = known_face_names[best_match_index]

#                     face_names.append(name)
#                     if((already_attendence_taken != name) and (name != "Unknown")):
#                      sheet1.write(row, col, name )
#                      col =col+1
#                      sheet1.write(row, col, "Present" )
#                      row = row+1
#                      col = 0
#                      print("attendence taken")
#                      wb.save('attendence_excel.xls')
#                      already_attendence_taken = name
#                     else:
#                      print("next student")
                        
#             process_this_frame = not process_this_frame


#             # Display the results
#             for (top, right, bottom, left), name in zip(face_locations, face_names):
#                 # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#                 top *= 4
#                 right *= 4
#                 bottom *= 4
#                 left *= 4

#                 # Draw a box around the face
#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#                 # Draw a label with a name below the face
#                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#                 font = cv2.FONT_HERSHEY_DUPLEX
#                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#             # Display the resulting image
#             cv2.imshow('Video', frame)

#             # Hit 'q' on the keyboard to quit!
#             if cv2.waitKey(1) & 0xff==ord('q'):   
#                 print("data save")
#                 break

# # Release handle to the webcam
# video_capture.release()
# cv2.destroyAllWindows()








# from cv2 import VideoCapture, imshow, imwrite
# import cv2
# import numpy as np
# import os
# from datetime import date
# import xlrd
# from xlutils.copy import copy as xl_copy

# CurrentFolder = os.getcwd() # Read current folder path
# image = os.path.join(CurrentFolder, 'rahul.png')
# image2 = os.path.join(CurrentFolder, 'sneha.png')

# # Get a reference to webcam #0 (the default one)
# video_capture = cv2.VideoCapture(0)

# # Check if the camera is opened successfully
# if not video_capture.isOpened():
#     print("Error: Failed to open webcam.")
#     exit()

# # Load sample pictures and learn how to recognize them
# person1_name = "Rahul"
# person1_image = cv2.imread(image)
# person1_face_encoding = []

# person2_name = "Sneha"
# person2_image = cv2.imread(image2)
# person2_face_encoding = []

# # Create arrays of known face encodings and their names
# known_face_encodings = [
#     person1_face_encoding,
#     person2_face_encoding
# ]
# known_face_names = [
#     person1_name,
#     person2_name
# ]

# # Initialize some variables
# face_locations = []
# face_encodings = []
# face_names = []
# process_this_frame = True

# rb = xlrd.open_workbook('attendence_excel.xls', formatting_info=True) 
# wb = xl_copy(rb)
# inp = input('Please give current subject lecture name: ')
# sheet1 = wb.add_sheet(inp)
# sheet1.write(0, 0, 'Name/Date')
# sheet1.write(0, 1, str(date.today()))
# row = 1
# col = 0
# already_attendence_taken = ""

# while True:
#     # Grab a single frame of video
#     ret, frame = video_capture.read()

#     # Check if the frame is valid
#     if not ret:
#         print("Error: Failed to capture frame from the webcam.")
#         break

#     # Resize frame of video to 1/4 size for faster face recognition processing
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

#     # Convert the image from BGR color to RGB color
#     rgb_small_frame = small_frame[:, :, ::-1]

#     # Only process every other frame of video to save time
#     if process_this_frame:
#         # Find all the faces and face encodings in the current frame of video
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         face_names = []
#         for face_encoding in face_encodings:
#             # See if the face is a match for the known face(s)
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = "Unknown"

#             # If a match was found in known_face_encodings, just use the first one
#             if True in matches:
#                 first_match_index = matches.index(True)
#                 name = known_face_names[first_match_index]

#             face_names.append(name)
#             if (already_attendence_taken != name) and (name != "Unknown"):
#                 sheet1.write(row, col, name)
#                 col += 1
#                 sheet1.write(row, col, "Present")
#                 row += 1
#                 col = 0
#                 print("Attendence taken")
#                 wb.save('attendence_excel.xls')
#                 already_attendence_taken = name
#             else:
#                 print("Next student")

#     process_this_frame = not process_this_frame

#     # Display the results
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

#         # Draw a box around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Draw a label with a name below the face
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     # Display the resulting image
#     cv2.imshow('Video', frame)

#     # Hit 'q' on the keyboard to quit!
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         print("Data saved")
#         break

# # Release handle to the webcam
# video_capture.release()
# cv2.destroyAllWindows()







# import face_recognition
# import cv2
# import numpy as np
# import os
# from datetime import date
# import xlrd
# from xlutils.copy import copy as xl_copy

# # Get current folder path
# CurrentFolder = os.getcwd()

# # Paths to sample images
# image_path_1 = os.path.join(CurrentFolder, 'rahul.png')
# image_path_2 = os.path.join(CurrentFolder, 'sneha.png')
# image_path_3 = os.path.join(CurrentFolder, 'bhavya.png')
# # Load sample images
# image_1 = face_recognition.load_image_file(image_path_1)
# image_2 = face_recognition.load_image_file(image_path_2)
# image_3 = face_recognition.load_image_file(image_path_3)

# # Encode faces
# known_face_encodings = []
# known_face_names = []

# # Encode face 1
# face_encoding_1 = face_recognition.face_encodings(image_1)
# if len(face_encoding_1) > 0:
#     known_face_encodings.append(face_encoding_1[0])
#     known_face_names.append("Rahul")
# else:
#     print("No face detected in image 1")

# # Encode face 2
# face_encoding_2 = face_recognition.face_encodings(image_2)
# if len(face_encoding_2) > 0:
#     known_face_encodings.append(face_encoding_2[0])
#     known_face_names.append("Sneha")
# else:
#     print("No face detected in image 2")

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# # Check if webcam is opened successfully
# if not video_capture.isOpened():
#     print("Error: Failed to open webcam.")
#     exit()

# # Open Excel workbook
# rb = xlrd.open_workbook('attendence_excel.xls', formatting_info=True)
# wb = xl_copy(rb)
# inp = input('Please give current subject lecture name: ')
# sheet1 = wb.add_sheet(inp)
# sheet1.write(0, 0, 'Name/Date')
# sheet1.write(0, 1, str(date.today()))
# row = 1
# col = 0
# already_attendance_taken = ""

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Convert the image from BGR color to RGB color
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Find all the faces in the current frame
#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#     # Recognize faces
#     face_names = []
#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]
#             if already_attendance_taken != name:
#                 sheet1.write(row, col, name)
#                 col += 1
#                 sheet1.write(row, col, "Present")
#                 row += 1
#                 col = 0
#                 print("Attendance taken for", name)
#                 wb.save('attendence_excel.xls')
#                 already_attendance_taken = name

#         face_names.append(name)

#     # Display the results
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         # Scale back up face locations
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

#         # Draw a box around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Draw a label with the name below the face
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     # Display the resulting image
#     cv2.imshow('Video', frame)

#     # Quit by pressing 'q' on the keyboard
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("Data saved")
#         break

# # Release handle to the webcam
# video_capture.release()
# cv2.destroyAllWindows()

# import face_recognition
# import cv2
# import numpy as np
# import os
# import csv
# from datetime import datetime

# def mark_attendance(name):
#     with open('attendance.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

# # Load sample images and encode faces
# known_face_encodings = []
# known_face_names = []

# # Path to sample images
# CurrentFolder = os.getcwd()
# image_path_1 = os.path.join(CurrentFolder, 'rahul.png')
# image_path_2 = os.path.join(CurrentFolder, 'sneha.png')
# image_path_3 = os.path.join(CurrentFolder, 'bhavya.png')

# # Load images
# image_1 = face_recognition.load_image_file(image_path_1)
# image_2 = face_recognition.load_image_file(image_path_2)
# image_3 = face_recognition.load_image_file(image_path_3)


# # Encode faces
# face_encoding_1 = face_recognition.face_encodings(image_1)[0]
# face_encoding_2 = face_recognition.face_encodings(image_2)[0]
# face_encoding_3 = face_recognition.face_encodings(image_3)[0]

# # Add encoded faces to lists
# known_face_encodings = [face_encoding_1, face_encoding_2,face_encoding_3]
# known_face_names = ["Rahul", "Sneha","bhavya"]

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     ret, frame = video_capture.read()
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#     face_names = []
#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"

#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]
#             mark_attendance(name)

#         face_names.append(name)

#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     cv2.imshow('Video', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# video_capture.release()
# cv2.destroyAllWindows()



# import face_recognition
# import cv2
# import numpy as np
# import os
# import csv
# from datetime import datetime

# def mark_attendance(name):
#     with open('attendance.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

# # Load sample images and encode faces
# known_face_encodings = []
# known_face_names = []

# # Path to folder containing images
# image_folder = os.path.join(os.getcwd(), 'images')

# # Load images from the folder
# for filename in os.listdir(image_folder):
#     if filename.endswith('.png') or filename.endswith('.jpg'):
#         image_path = os.path.join(image_folder, filename)
#         image = face_recognition.load_image_file(image_path)
#         face_encoding = face_recognition.face_encodings(image)[0]
#         known_face_encodings.append(face_encoding)
#         known_face_names.append(os.path.splitext(filename)[0])  # Get the filename without extension

# # Initialize webcam

# #print the names of 
# # for i in known_face_names:
# #     print(i)
# video_capture = cv2.VideoCapture(0)

# while True:
#     ret, frame = video_capture.read()
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#     face_names = []
#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"

#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]
#             mark_attendance(name)

#         face_names.append(name)

#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     cv2.imshow('Video', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("Attendence marked")
#         break

# video_capture.release()
# cv2.destroyAllWindows()





import face_recognition
import cv2
import numpy as np
import os
import csv
from datetime import datetime

# Function to mark attendance in CSV file
def mark_attendance(name):
    with open('attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

# Load sample images and encode faces
known_face_encodings = []
known_face_names = []

# Path to folder containing images
image_folder = os.path.join(os.getcwd(), 'images')

# Load images from the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        image_path = os.path.join(image_folder, filename)
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(os.path.splitext(filename)[0])  # Get the filename without extension

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Initialize attendance marking
marked_attendance = set()

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
            # Check if attendance has been marked for this name
            if name not in marked_attendance:
                mark_attendance(name)
                marked_attendance.add(name)  # Add name to marked set to avoid duplicate marking

        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Attendance marked")
        break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()

