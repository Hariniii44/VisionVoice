import spacy
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class WebNavigator:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.current_url = None

    def open_hyperlink(self, absolute_url):
        try:
            self.driver.get(absolute_url)
            self.current_url = self.driver.current_url
            return self.current_url
        except WebDriverException as e:
            print(f"An error occurred while opening the hyperlink")
            return None

    def go_back(self):
        try:
            self.driver.back()
            self.current_url = self.driver.current_url
            return self.current_url
        except WebDriverException as e:
            print("An error occurred while navigating back:", e)
            return None

    def navigate(self):
        current_url = input("Enter the URL: ")

        if not current_url:
            print("No website URL found. Exiting.")
            self.driver.quit()
            return

        self.current_url = current_url
        self.driver.get(current_url)

        while True:
            response = self.driver.page_source
            soup = BeautifulSoup(response, 'html.parser')
            hyperlinks = soup.find_all('a')

            user_input = input("Enter your command: ")  # Change this to receive user input
            doc_navigation = nlp_navigation(user_input)

            hyperlink_entities = [ent.text.lower() for ent in doc_navigation.ents if ent.label_ == "HYPERLINK"]

            hyperlink_found = False
            if hyperlink_entities:
                for hyperlink_entity in hyperlink_entities:
                    for hyperlink in hyperlinks:
                        if hyperlink_entity.lower() in hyperlink.text.lower():  # Case-insensitive comparison
                            absolute_url = urljoin(self.current_url, hyperlink.get('href'))
                            print(f"Opening the hyperlink: {absolute_url}")
                            self.current_url = self.open_hyperlink(absolute_url)
                            if self.current_url:
                                hyperlink_found = True
                                break

            if not hyperlink_found:
                if user_input.lower() == "go back":
                    self.current_url = self.go_back()
                else:
                    print("The specified hyperlink is not available on the website.")

            if not self.current_url:
                break


# Load the fine-tuned NER model for navigating through the website
nlp_navigation = spacy.load("fine_tuned_model")

# Create an instance of WebNavigator and navigate
navigator = WebNavigator()
navigator.navigate()
