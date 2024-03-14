from navigation import WebNavigator


def read_hyperlinks_function():
    URL = "https://www.mathsisfun.com/algebra/introduction.html"
    write_to_file(URL)
    print("link")


def write_to_file(URL):
    with open("chosen_URL.txt", "w") as file:
        file.write(URL)


def read_content_function():
    print("reading")


def goto_homepage_function():
    print("Going to the home page")


def go_back_function():
    print("Go back")


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
    navigator.navigate(start_url, test_command)
    return start_url  # Return the updated current URL after navigation
