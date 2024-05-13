import requests
from lxml import html
import os

def download_images(image_urls, folder, breed_name):
    breed_folder = os.path.join(folder, breed_name)
    if not os.path.exists(breed_folder):
        os.makedirs(breed_folder)

    # 获取已经存在的图片数量，以便继续命名
    existing_images = len([name for name in os.listdir(breed_folder) if os.path.isfile(os.path.join(breed_folder, name))])

    for i, image_url in enumerate(image_urls, start=existing_images):
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                image_path = os.path.join(breed_folder, f'{breed_name}_{i}.jpg')
                with open(image_path, 'wb') as f:
                    f.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {image_url}: {e}")

base_folder = './data/raw/'

urls_and_breeds = [
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-1.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-2.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-3.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-4.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-5.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-6.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-47.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-48.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-samoyede-56-1.php', 'samoyede'),
    ('https://www.chien.com/photos-chiens/photo-samoyede-56-2.php', 'samoyede'),
    ('https://www.chien.com/photos-chiens/photo-samoyede-56-3.php', 'samoyede'),
    ('https://www.chien.com/photos-chiens/photo-samoyede-56-4.php', 'samoyede'),
    ('https://www.chien.com/photos-chiens/photo-samoyede-56-5.php', 'samoyede'),
    ('https://www.chien.com/photos-chiens/photo-samoyede-56-6.php', 'samoyede'),
    ('https://www.chien.com/photos-chiens/photo-carlin-145-1.php', 'carlin'),
    ('https://www.chien.com/photos-chiens/photo-carlin-145-2.php', 'carlin'),
    ('https://www.chien.com/photos-chiens/photo-carlin-145-3.php', 'carlin'),
    ('https://www.chien.com/photos-chiens/photo-carlin-145-4.php', 'carlin'),
    ('https://www.chien.com/photos-chiens/photo-carlin-145-5.php', 'carlin'),
    ('https://www.chien.com/photos-chiens/photo-carlin-145-6.php', 'carlin'),
    ('https://www.chien.com/photos-chiens/photo-carlin-145-7.php', 'carlin'),
    ('https://www.chien.com/photos-chiens/photo-carlin-145-8.php', 'carlin'),
]

for url, breed_name in urls_and_breeds:
    response = requests.get(url)
    tree = html.fromstring(response.content)
    image_urls = tree.xpath('//img[@class="lozad"]/@data-src')
    download_images(image_urls, base_folder, breed_name)
