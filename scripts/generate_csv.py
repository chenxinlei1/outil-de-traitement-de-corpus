import pandas as pd
import os

base_folder = './data/raw'
csv_file = './data/dog_breeds_images.csv'
csv_headers = ['id', 'image', 'label']

data = []
image_id = 1

breed_folders = sorted([d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))])

breed_to_id = {breed: i for i, breed in enumerate(breed_folders)}

for breed_folder in breed_folders:
    breed_path = os.path.join(base_folder, breed_folder)
    for image_file in os.listdir(breed_path):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(breed_path, image_file)
            breed_id = breed_to_id[breed_folder]
            data.append([image_id, image_path, breed_id])
            image_id += 1

df = pd.DataFrame(data, columns=csv_headers)

df.to_csv(csv_file, index=False)
