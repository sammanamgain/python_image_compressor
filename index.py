import os
import tweepy
import time

# Authenticate to Twitter (X)
consumer_key='yYnyEIzZLpTfGnNsE41igtdeZ'
consumer_secret='qiBxJanObrWlWiTs1p03lXMuxsvYS1FGULrMVgCZu3gDaZGJTr'
api_key = "bscvOXxg3TNMk1ZjTXVPdQ2h5"
api_secret_key = "Dw4VGxtYnMDyEsDEPh5QIovMK9f1IQxsenmMLjLdwlvNV6qhBS"
access_token = "1537436761261228032-i1UFN6CbqpKiX1RjSOqETPFIUZvDmN"
access_token_secret = "STluI1eZaX5PXzLodor0hNabkhBLWOfnXtCigouzQ3baW"

auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Directory where your images are stored
image_folder = "/home/sammanamgain/Pictures/compressed/Paranhosu-Tani-Heart-Flutter-MissKON.com-036.jpg"




# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)
auth = tweepy.OAuth1UserHandler(
consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)





image_folder = "/home/sammanamgain/Pictures/compressed"

# Time to wait between uploads (in seconds)
wait_time = 300  # 300 seconds = 5 minutes

# Loop through the folder and upload images
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file types if needed
        image_path = os.path.join(image_folder, filename)

        # Create tweet
        message = "Tani -Hot korean Model \n #Hotgirl #Korean"

        # Upload image
        media = api.media_upload(image_path)

        # Post tweet with image
        client.create_tweet(text=message, media_ids=[media.media_id])
        print("upload succesfully")
        time.sleep(50)
# print("Tweeted!")
# # Time to wait between uploads (in seconds)
# wait_time = 10  # 300 seconds = 5 minutes

# # Loop through the folder and upload images
# for filename in os.listdir(image_folder):
#     if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file types if needed
#         image_path = os.path.join(image_folder, filename)
        
#         try:
#             # Step 1: Upload media
#             media = api.media_upload(image_path)
            
#             # Step 2: Post tweet with the uploaded media
#             api.update_status(status="Hot tani Korean Model", media_ids=[media.media_id])
#             print(f"Uploaded: {filename}")
            
#             # Wait for the specified time before uploading the next image
#             time.sleep(wait_time)
        
#         except Exception as e:
#             print(f"Error uploading {filename}: {e}")
