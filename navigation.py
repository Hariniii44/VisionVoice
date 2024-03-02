import spacy
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from test import process_query

# Load the fine-tuned NER model for navigating through the website
nlp_navigation = spacy.load("fine_tuned_model")

# Create a WebDriver instance
driver = webdriver.Chrome()

# Ask the user to input the query
query = input("Enter your query: ")

# Process the user query to open websites and navigate through hyperlinks
current_url = process_query(query)

# If no URL is returned, exit the script
if not current_url:
    print("No website URL found. Exiting.")
    driver.quit()
    exit()

# Use Selenium to navigate to the website extracted from the user query
driver.get(current_url)

while True:
    # Extract hyperlinks from the opened website
    response = driver.page_source
    soup = BeautifulSoup(response, 'html.parser')
    hyperlinks = soup.find_all('a')

    # Process the user command with the fine-tuned NER model
    user_input = input("Enter your command: ")  # Change this to receive user input
    doc_navigation = nlp_navigation(user_input)

    # Identify entities related to hyperlink navigation
    hyperlink_entities = [ent.text.lower() for ent in doc_navigation.ents if ent.label_ == "HYPERLINK"]

    # Check if the hyperlink matches the user's command and if it's found on the website
    hyperlink_found = False
    if hyperlink_entities:
        for hyperlink_entity in hyperlink_entities:
            for hyperlink in hyperlinks:
                if hyperlink_entity.lower() in hyperlink.text.lower():
                    # Construct the absolute URL
                    absolute_url = urljoin(current_url, hyperlink.get('href'))
                    print(f"Opening the hyperlink: {absolute_url}")

                    # Open the hyperlink in the same tab
                    try:
                        driver.get(absolute_url)
                        current_url = absolute_url  # Update the current URL
                    except NoSuchElementException:
                        print(f"The specified hyperlink '{hyperlink_entity}' is not available on the website.")
                    else:
                        hyperlink_found = True
                        break

    if not hyperlink_found:
        print("The specified hyperlink is not available on the website.")

# Close the WebDriver after finishing the navigation
driver.quit()