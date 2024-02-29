import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the target website URL
website_url = "https://www.mathplanet.com/education/algebra-1/formulating-linear-equations/writing-linear-equations-using-the-slope-intercept-form"  # Replace with the actual website URL

# Create a folder to store the downloaded images
output_folder = "images"
os.makedirs(output_folder, exist_ok=True)

# Send a request to the website
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(website_url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all image tags (img) and extract their source URLs
image_tags = soup.find_all("img")
for img in image_tags:
    img_url = img.get("src")
    if img_url:
        # Construct the absolute URL for the image
        full_img_url = urljoin(website_url, img_url)

        # Download the image
        try:
            img_response = requests.get(full_img_url)
            img_filename = os.path.join(output_folder, os.path.basename(full_img_url))
            with open(img_filename, "wb") as img_file:
                img_file.write(img_response.content)
            print(f"Downloaded: {img_filename}")
        except Exception as e:
            print(f"Error downloading {full_img_url}: {e}")

print("Image scraping completed. Images saved in the 'images' folder.")
