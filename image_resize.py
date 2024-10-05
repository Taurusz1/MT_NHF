import os
from PIL import Image

folder_path = 'Books_Before_Resize'
new_folder = 'books'
output_size = (256, 256)

# Iterate through all files in the folder
for i, filename in enumerate(os.listdir(folder_path), start=1):
    file_path = os.path.join(folder_path, filename)

    try:
        with Image.open(file_path) as img:
            resized_img = img.resize(output_size)
            new_filename = f"book_{i}.png"  # Change the extension based on your needs
            new_file_path = os.path.join(new_folder, new_filename)
            resized_img.save(new_file_path)
    
    except Exception as e:
        print(f"Error processing file {filename}: {e}")
