import os
import time
from instagrapi import Client
from random import randint

# Function to login and upload a photo
def upload_photos_from_folder(username, password, folder_path, caption):
    # Login to Instagram
    client = Client()
    client.login(username, password)

    # Get list of image files in the folder
    images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Iterate over each image and upload it
    for idx, image in enumerate(images):
        image_path = os.path.join(folder_path, image)
        print(f"Uploading {image_path}...")

        try:
            # Upload the photo with a caption
            client.photo_upload(image_path, caption)
            print(f"Uploaded {image} successfully!")

            # Add a delay between uploads to avoid getting blocked
            # Random sleep time between 30 to 90 seconds
            sleep_time = 10
            print(f"Sleeping for {sleep_time} seconds before the next upload...")
            time.sleep(sleep_time)
        except Exception as e:
            print(f"Error uploading {image}: {e}")
            continue  # Skip to the next image if there's an error

if __name__ == "__main__":
    username = "lionalmessi609@gmail.com"
    password = "Samman@123"
    folder_path = "/home/sammanamgain/Pictures/compressed"
    caption = "Hot Korean Model girl --Tani \n  #Korean \n #Hotgirl \n #hot \n #koreanmodel \n #girl"

    upload_photos_from_folder(username, password, folder_path, caption)
