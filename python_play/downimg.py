import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve
from PIL import Image

def download_images(url, download_folder):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags in the HTML
        img_tags = soup.find_all('img')
        
        # Download and convert each image to JPG
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                
                # Generate a unique filename for each image
                img_filename = os.path.join(download_folder, os.path.basename(urlparse(img_url).path))
                
                # Download the image
                urlretrieve(img_url, img_filename)
                print(f"Downloaded: {img_filename}")
                
                # Convert the image to JPG if not already
                convert_to_jpg(img_filename)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

def convert_to_jpg(img_filename):
    try:
        # Open the image using Pillow
        image = Image.open(img_filename)
        
        # Convert to RGB if it's not in that mode
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        # Generate a new filename with the .jpg extension
        new_filename = os.path.splitext(img_filename)[0] + ".jpg"
        
        # Save the image in JPG format
        image.save(new_filename, format='JPEG')
        
        # Remove the original image file
        os.remove(img_filename)
        
        print(f"Converted and saved as: {new_filename}")
    except Exception as e:
        print(f"Error converting {img_filename} to JPG: {e}")

# Example usage:
website_url = "https://www.bing.com/images/search?q=Nature+Wallpaper+for+PC&form=IARSLK&first=1"
download_directory = "./images"

# Make sure the download directory exists
os.makedirs(download_directory, exist_ok=True)

# Call the function to download and convert images
download_images(website_url, download_directory)