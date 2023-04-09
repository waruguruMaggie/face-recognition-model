import face_recognition
import cv2
import os

def enroll_user():
    # Prompt user for name and ID
    name = input("Enter name: ")
    id = input("Enter ID: ")
    
    # Take image from file
    image_path = input("Enter image path: ")
    image = face_recognition.load_image_file(image_path)
    
    # Save image with user's name as file name
    image_name = f"{name}.jpg"
    image_dir = "./user_images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    image_path = os.path.join(image_dir, image_name)
    cv2.imwrite(image_path, image)

    print("User enrolled successfully.")

    if __name__ == '__main__':
   
         enroll_user()