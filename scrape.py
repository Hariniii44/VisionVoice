import requests
from bs4 import BeautifulSoup

def scrape_alt_text(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all image tags
        img_tags = soup.find_all('img')

        # Print the alt text for each image
        for img_tag in img_tags:
            alt_text = img_tag.get('alt', '')
            print(alt_text)

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Replace 'your_url_here' with the actual URL you want to scrape
url_to_scrape = 'https://www.britannica.com/'
scrape_alt_text(url_to_scrape)