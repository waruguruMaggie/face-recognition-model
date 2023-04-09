import os

def update_user():
    # Load user IDs
    image_dir = "./user_images"
    image_files = os.listdir(image_dir)
    user_ids = [os.path.splitext(image_file)[0] for image_file in image_files]

    # Prompt user for ID of user to update
    id = input("Enter Name of user to update: ")
    if id not in user_ids:
        print("User not found.")
        return
    
    # Prompt user for new name
    new_name = input("Enter new name: ")

    # Rename user's image file
    old_image_name = f"{id}.jpg"
    new_image_name = f"{new_name}.jpg"
    old_image_path = os.path.join(image_dir, old_image_name)
    new_image_path = os.path.join(image_dir, new_image_name)
    os.rename(old_image_path, new_image_path)

    print("User updated successfully.")

if __name__ == '_main_':
    update_user()