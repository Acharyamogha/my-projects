import os
import requests
from bs4 import BeautifulSoup

# Create a folder to store the comics
folder_path = 'xkcd_comics'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# URL to the XKCD archive page
base_url = 'https://xkcd.com'
archive_url = base_url + '/archive/'

# Get the archive page
response = requests.get(archive_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the comic URLs
comic_links = soup.select('#middleContainer > a')

# Loop through each comic URL
for link in comic_links:
    comic_url = base_url + link.get('href')

    # Get the comic page
    comic_response = requests.get(comic_url)
    comic_soup = BeautifulSoup(comic_response.content, 'html.parser')

    # Find the comic image URL
    comic_image = comic_soup.select('#comic > img')[0]
    image_url = 'https:' + comic_image.get('src')

    # Get the image data
    image_response = requests.get(image_url)

    # Save the image to the folder
    image_name = image_url.split('/')[-1]
    image_path = os.path.join(folder_path, image_name)

    with open(image_path, 'wb') as f:
        f.write(image_response.content)

    print(f"Downloaded: {image_name}")

print("All XKCD comics downloaded.")