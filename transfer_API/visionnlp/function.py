from navigation import WebNavigator
from urllib.parse import urlparse

homepage_urls = {
    "oxnotes.com": "https://www.oxnotes.com/igcse-mathematics.html",
    "mathisfun.com": "https://www.mathsisfun.com/algebra/index.html",
    "tutorial.math.lamar.edu": "https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx",
    "mathplanet.com": "https://www.mathplanet.com/education/algebra-2"  # Add more websites as needed
}


def extract_base_url(url):
    # Parse the URL to extract the domain name
    parsed_url = urlparse(url)
    base_url = parsed_url.netloc
    return base_url


def goto_homepage_function(current_url, navigator):
    print("Going to the home page")
    # Extract the base URL from the current URL
    base_url = extract_base_url(current_url)
    print("Base URL:", base_url)

    # Look up the home page URL from the mapping based on partial match
    homepage_url = None
    for key in homepage_urls:
        if key in base_url:
            homepage_url = homepage_urls[key]
            break

    if base_url == "www.mathsisfun.com":
        homepage_url = "https://www.mathsisfun.com/algebra/index.html"

    if homepage_url:
        print("Going to the home page:", homepage_url)
        # Navigate to the home page URL using the navigator object
        navigator.navigate(homepage_url, "goto_homepage")
    else:
        print("Home page URL not found for the current website.")


def read_hyperlinks_function():
    URL = "https://www.mathsisfun.com/algebra/introduction.html"
    write_to_file(URL)
    print("link")


def write_to_file(URL):
    with open("chosen_URL.txt", "w") as file:
        file.write(URL)


def read_content_function():
    print("reading")


def go_back_function(navigator, current_url):
    print("Go back")
    # Check if the current URL is a homepage URL
    for homepage_url in homepage_urls.values():
        if navigator.current_url == homepage_url:
            print("You are already on the homepage.")
            return current_url

    # If not on the homepage, navigate back
    navigator.go_back()
    # Update current_url after navigation
    current_url = navigator.current_url
    return current_url



def explain_images_function():
    print("explain images")


def explain_graph_function():
    print("explain graph")


def translate_to_sinhala_function():
    print("tarn sin")


def translate_to_tamil_function():
    print("tarn tamil")


def goto_section_function(test_command, navigator, current_url):
    print("Go to section")
    print(current_url)
    start_url = current_url if current_url else input(
        "Enter your url: ")  # Use current URL if available, otherwise ask the user for input
    print(start_url)
    navigator.navigate(start_url, test_command)
    return start_url  # Return the updated current URL after navigation
