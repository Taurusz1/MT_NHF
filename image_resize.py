import os
from PIL import Image

def Img_Resize(old_folder_path, new_folder, image_type):
    output_size = (256, 256)
    
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        
    for i, filename in enumerate(os.listdir(old_folder_path), start=1):
        file_path = os.path.join(old_folder_path, filename)

        try:
            with Image.open(file_path) as img:
                resized_img = img.resize(output_size)
                new_filename = f"{image_type}_{i}.jpg"
                new_file = os.path.join(new_folder, new_filename)
                resized_img.save(new_file)
        except Exception as e:
            print(f"Error processing file {filename}: {e}")
