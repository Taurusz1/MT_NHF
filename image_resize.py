import os
from PIL import Image

def Img_Resize(old_folder_path, new_file_path, image_type):
    output_size = (256, 256)
    if not os.path.exists(new_file_path):
        os.makedirs(new_file_path)
    # Iterate through all files in the folder
    for i, filename in enumerate(os.listdir(old_folder_path), start=1):
        file_path = os.path.join(old_folder_path, filename)

        try:
            with Image.open(file_path) as img:
                resized_img = img.resize(output_size)
                new_filename = f"{image_type}_{i}.jpg"  # Change the extension based on your needs
                new_file_path = os.path.join(new_file_path, new_filename)
                resized_img.save(new_file_path)
    
        except Exception as e:
            print(f"Error processing file {filename}: {e}")
