import os
from PIL import Image
import ffmpeg

def compress_image(input_file, output_file, quality=85):
    """
    Compress an image file and save it to the output file.
    
    Args:
        input_file (str): Path to the input image file.
        output_file (str): Path to save the compressed image file.
        quality (int, optional): Compression quality (1-100). Default is 85.
    """
    try:
        with Image.open(input_file) as img:
            img.save(output_file, optimize=True, quality=quality)
            print(f"Compressed image {input_file} and saved to {output_file}")
    except Exception as e:
        print(f"Error compressing image {input_file}: {e}")

def compress_video(input_file, output_file, crf=23):
    """
    Compress a video file and save it to the output file.
    
    Args:
        input_file (str): Path to the input video file.
        output_file (str): Path to save the compressed video file.
        crf (int, optional): Constant Rate Factor (0-51). Lower values result in better quality and larger file size. Default is 23.
    """
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, crf=crf)
            .run(overwrite_output=True)
        )
        print(f"Compressed video {input_file} and saved to {output_file}")
    except Exception as e:
        print(f"Error compressing video {input_file}: {e}")

def compress_media(input_folder, output_folder, image_quality=85, video_crf=23):
    """
    Compress both images and videos from the input folder and save them to the output folder.
    
    Args:
        input_folder (str): Path to the folder containing media files.
        output_folder (str): Path to the folder where compressed media will be saved.
        image_quality (int, optional): Image compression quality (1-100). Default is 85.
        video_crf (int, optional): Video compression CRF value (0-51). Default is 23.
    """
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each file in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # Check file type and perform appropriate compression
        if file_name.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            compress_image(file_path, output_path, quality=image_quality)
        elif file_name.endswith(('.mp4', '.avi', '.mkv', '.mov')):
            compress_video(file_path, output_path, crf=video_crf)
        else:
            print(f"Skipping unsupported file format: {file_name}")

# if __name__ == "__main__":
#     input_folder = "/path/to/your/input_folder"
#     output_folder = "/path/to/your/output_folder"
    
#     # Compress images at quality 85 and videos at CRF 23
#     compress_media(input_folder, output_folder, )


if __name__ == "__main__":
    input_folder = "/home/sammanamgain/Pictures/Yeon Woo (연우) - Happy Birthday"
    output_folder = "/home/sammanamgain/Pictures/Yeon Woo (연우) - Happy BirthdayReduced"
    compress_media(input_folder, output_folder, image_quality=85, video_crf=23)
