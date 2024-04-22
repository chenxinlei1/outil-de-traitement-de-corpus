import csv
import os

base_folder = './data/raw/'

csv_file = './data/dog_breeds_images.csv' 

csv_headers = ['id', 'image', 'label']

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)  

    image_id = 1

    for breed_folder in os.listdir(base_folder):
        breed_path = os.path.join(base_folder, breed_folder)
        if os.path.isdir(breed_path):
            for image_file in os.listdir(breed_path):
                if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    image_path = os.path.join(breed_path, image_file)
                    writer.writerow([image_id, image_path, breed_folder])
                    image_id += 1
