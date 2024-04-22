import requests
from lxml import html
import os

def download_images(image_urls, folder, breed_name):
    breed_folder = os.path.join(folder, breed_name)
    if not os.path.exists(breed_folder):
        os.makedirs(breed_folder)

    for i, image_url in enumerate(image_urls):
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
    ('https://chien.com/photos-chiens/photo-shiba-inu-95-1.php', 'shiba_inu'),
    ('https://www.chien.com/photos-chiens/photo-berger-allemand-14-1.php', 'berger_allemand'),
    ('https://www.chien.com/photos-chiens/photo-golden-retriever-25-1.php', 'golden_retriever'),
    ('https://www.chien.com/photos-chiens/photo-bouledogue-francais-20-1.php', 'bouledogue_francais'),
    ('https://www.chien.com/photos-chiens/photo-retriever-a-poil-plat-91-1.php', 'retriever_a_poil_plat'),
    ('https://www.chien.com/photos-chiens/photo-husky-siberien-36-1.php', 'husky_siberien'),
    ('https://www.chien.com/photos-chiens/photo-bichon-frise-126-1.php', 'bichon_frise'),
    ('https://www.chien.com/photos-chiens/photo-samoyede-56-1.php', 'samoyede'),
    ('https://www.chien.com/photos-chiens/photo-braque-allemand-a-poil-court-231-1.php', 'braque_allemand_a_poil_court'),
    ('https://www.chien.com/photos-chiens/photo-caniche-34-1.php', 'caniche'),
    ('https://www.chien.com/photos-chiens/photo-shih-tzu-355-1.php', 'shih_tzu'),
    ('https://www.chien.com/photos-chiens/photo-dobermann-55-1.php', 'dobermann'),
    ('https://www.chien.com/photos-chiens/photo-boxer-5-1.php', 'boxer'),
    ('https://www.chien.com/photos-chiens/photo-labrador-husky-507-1.php', 'labrador_husky'),
    ('https://www.chien.com/photos-chiens/photo-petit-levrier-italien-415-1.php', 'petit_levrier_italien'),
]


for url, breed_name in urls_and_breeds:
    response = requests.get(url)
    tree = html.fromstring(response.content)
    image_urls = tree.xpath('//img[@class="lozad"]/@data-src')
    download_images(image_urls, base_folder, breed_name)


