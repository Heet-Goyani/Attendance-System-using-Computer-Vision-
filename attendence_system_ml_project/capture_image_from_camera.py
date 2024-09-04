# from cv2 import VideoCapture ,imshow,imwrite,cv2
# cam_port = 1
# cam = VideoCapture(cam_port)
# # reading the input using the camera

# inp = input('Enter person name')
# # If image will detected without any error,
# # show result
# while(1): 
#         result,image = cam.read()
#         imshow(inp, image)
#         if cv2.waitKey(0):
#          imwrite(inp+".png", image)
#          print("image taken")

# # If captured image is corrupted, moving to else part
# else:
# 	print("No image detected. Please! try again")


# from cv2 import VideoCapture, imshow, imwrite
# import cv2

# cam_port = 1
# cam = VideoCapture(cam_port)
# # reading the input using the camera

# inp = input('Enter person name')
# # If image will detected without any error,
# # show result
# while True:
#     result, image = cam.read()
#     imshow(inp, image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     elif cv2.waitKey(1) & 0xFF == ord('s'):
#         imwrite(inp + ".png", image)
#         print("Image saved as {}.png".format(inp))

# cam.release()
# cv2.destroyAllWindows()



# from cv2 import VideoCapture, imshow, imwrite
# import cv2

# cam_port = 0  # Change the camera index if needed
# cam = VideoCapture(cam_port)
# # reading the input using the camera

# inp = input('Enter person name: ')
# # If image will detected without any error,
# # show result
# while True:
#     result, image = cam.read()
#     if result:  # Check if a valid frame is captured
#         imshow(inp, image)
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord('q'):  # Press 'q' to quit
#             break
#         elif key == ord('s'):  # Press 's' to save the image
#             imwrite(inp + ".png", image)
#             print("Image saved as {}.png".format(inp))
#     else:
#         print("Failed to capture a frame from the camera.")

# cam.release()
# cv2.destroyAllWindows()


import cv2
import os

def capture_and_save_image():
    cam_port = 0  # Change the camera index if needed
    cam = cv2.VideoCapture(cam_port)

    inp = input('Enter person name: ')

    # If image will detected without any error,
    # show result
    while True:
        result, image = cam.read()
        if result:  # Check if a valid frame is captured
            cv2.imshow(inp, image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):  # Press 'q' to quit
                break
            elif key == ord('s'):  # Press 's' to save the image
                folder_path = 'images'
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                image_path = os.path.join(folder_path, inp + ".png")
                cv2.imwrite(image_path, image)
                print("Image saved as {}.png".format(inp))
        else:
            print("Failed to capture a frame from the camera.")

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_save_image()

