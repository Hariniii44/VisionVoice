import spacy
from spacy.training.example import Example
from function import *
from navigation import WebNavigator
from function import goto_section_function


def train_text_categorization_model(train_data, use_case_labels, n_iter=20, dropout=0.5, batch_size=8):
    # Load the large English language model
    nlp = spacy.blank("en")

    # Add text categorization pipeline
    textcat = nlp.add_pipe("textcat")
    for label in use_case_labels:
        textcat.add_label(label)

    # Convert training data to Examples
    examples = []
    for text, annotations in train_data:
        examples.append(Example.from_dict(nlp.make_doc(text), annotations))

    # Train only the text categorizer
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "textcat"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for i in range(n_iter):
            losses = {}
            for batch in spacy.util.minibatch(examples, size=batch_size):
                nlp.update(batch, drop=dropout, losses=losses, sgd=optimizer)

    return nlp


def quit_browser(navigator):
    navigator.driver.quit()


def predict_intent(model, command, use_case_labels):
    doc = model(command)
    predicted_labels = [label for label in use_case_labels if label in doc.cats]

    if not predicted_labels:
        print("Command not recognized.")
        return None

    matched_intent = max(predicted_labels, key=lambda label: doc.cats[label])
    return matched_intent


# Define your training data
train_data = [
    ("Going to the Ratios section", {"cats": {"goto_section": 1}}),
    ("Going to the Ratios section", {"cats": {"goto_section": 1}}),
    ("Open Introduction to Algebra", {"cats": {"goto_section": 1}}),
    ("Go to Factorising Quadratics ", {"cats": {"goto_section": 1}}),
    ("Introduction to Algebra", {"cats": {"goto_section": 1}}),
    ("Move to Introduction to Algebra", {"cats": {"goto_section": 1}}),
    ("Explore Introduction to Geometry", {"cats": {"goto_section": 1}}),
    ("I want to learn Introduction to Algebra section", {"cats": {"goto_section": 1}}),
    ("Balance when Adding and Subtracting", {"cats": {"goto_section": 1}}),
    ("Go to Balance when Adding and Subtracting", {"cats": {"goto_section": 1}}),
    ("Open Balance when Adding and Subtracting", {"cats": {"goto_section": 1}}),
    ("Open Trigonometry", {"cats": {"goto_section": 1}}),
    ("PEMDAS", {"cats": {"goto_section": 1}}),
    ("Explore PEMDAS", {"cats": {"goto_section": 1}}),
    ("I want to access PEMDAS", {"cats": {"goto_section": 1}}),
    ("Open Substitution", {"cats": {"goto_section": 1}}),
    ("Substitution", {"cats": {"goto_section": 1}}),
    ("Explore Substitution", {"cats": {"goto_section": 1}}),
    ("I want to access Substitution", {"cats": {"goto_section": 1}}),
    ("Open Equations and Formulas", {"cats": {"goto_section": 1}}),
    ("Explore Equations and Formulas", {"cats": {"goto_section": 1}}),
    ("Click Equations and Formulas", {"cats": {"goto_section": 1}}),
    ("Inequalities", {"cats": {"goto_section": 1}}),
    ("Pythagoras' Theorem", {"cats": {"goto_section": 1}}),
    ("What is an Exponent?", {"cats": {"goto_section": 1}}),
    ("What Is A Logarithm", {"cats": {"goto_section": 1}}),
    ("What is a Polynomial?", {"cats": {"goto_section": 1}}),
    ("Rationalizing The Denominator", {"cats": {"goto_section": 1}}),
    ("Explore the Straight Line Graph", {"cats": {"goto_section": 1}}),
    ("Solving systems of equations in two variables", {"cats": {"goto_section": 1}}),
    ("Solving systems of equations in three variables", {"cats": {"goto_section": 1}}),
    ("Matrix operations", {"cats": {"goto_section": 1}}),
    ("Simplify expressions", {"cats": {"goto_section": 1}}),
    ("Solving radical equations", {"cats": {"goto_section": 1}}),
    ("Complex numbers", {"cats": {"goto_section": 1}}),
    ("How to graph quadratic functions", {"cats": {"goto_section": 1}}),
    ("The Quadratic formula", {"cats": {"goto_section": 1}}),
    ("Basic knowledge of polynomial functions", {"cats": {"goto_section": 1}}),
    ("Logarithm property", {"cats": {"goto_section": 1}}),
    ("Counting principle", {"cats": {"goto_section": 1}}),
    ("Trigonometric functions", {"cats": {"goto_section": 1}}),
    ("Law of sines", {"cats": {"goto_section": 1}}),
    ("Law of cosines", {"cats": {"goto_section": 1}}),
    ("Trigonometric identities", {"cats": {"goto_section": 1}}),
    ("Rational expressions", {"cats": {"goto_section": 1}}),
    ("Going to the Ratios section", {"cats": {"goto_section": 1}}),
    ("Open Introduction to Algebra", {"cats": {"goto_section": 1}}),

    ("Readout the Hyperlinks", {"cats": {"read_hyperlinks": 1}}),
    ("List the links", {"cats": {"read_hyperlinks": 1}}),
    ("Provide a list of hyperlinks", {"cats": {"read_hyperlinks": 1}}),
    ("Read out the URLs", {"cats": {"read_hyperlinks": 1}}),
    ("Enumerate the hyperlinks", {"cats": {"read_hyperlinks": 1}}),
    ("Announce the links", {"cats": {"read_hyperlinks": 1}}),
    ("Retrieve the hyperlink addresses", {"cats": {"read_hyperlinks": 1}}),
    ("Read aloud the hyperlinks", {"cats": {"read_hyperlinks": 1}}),
    ("Present the list of links", {"cats": {"read_hyperlinks": 1}}),
    ("Display the URLs", {"cats": {"read_hyperlinks": 1}}),
    ("List all the clickable links", {"cats": {"read_hyperlinks": 1}}),

    ("Go to the home page", {"cats": {"goto_homepage": 1}}),
    ("Navigate to the main page", {"cats": {"goto_homepage": 1}}),
    ("Return to the homepage", {"cats": {"goto_homepage": 1}}),
    ("Visit the front page", {"cats": {"goto_homepage": 1}}),
    ("Access the initial page", {"cats": {"goto_homepage": 1}}),
    ("Move to the starting page", {"cats": {"goto_homepage": 1}}),
    ("Return to the landing page", {"cats": {"goto_homepage": 1}}),
    ("Browse to the home screen", {"cats": {"goto_homepage": 1}}),
    ("Go back to the main menu", {"cats": {"goto_homepage": 1}}),
    ("Access the primary page", {"cats": {"goto_homepage": 1}}),
    ("Navigate to the front end", {"cats": {"goto_homepage": 1}}),

    ("Read the content", {"cats": {"read_content": 1}}),
    ("Read out loud this page", {"cats": {"read_content": 1}}),
    ("Retrieve this paragraph", {"cats": {"read_content": 1}}),
    ("Provide the information in the page", {"cats": {"read_content": 1}}),
    ("Narrate the full content", {"cats": {"read_content": 1}}),
    ("Speak the content", {"cats": {"read_content": 1}}),
    ("Vocalize the content", {"cats": {"read_content": 1}}),
    ("Recite the paragraph", {"cats": {"read_content": 1}}),
    ("Verbally present the content", {"cats": {"read_content": 1}}),
    ("Announce the content", {"cats": {"read_content": 1}}),

    ("Go back", {"cats": {"go_back": 1}}),
    ("Return to the previous page", {"cats": {"go_back": 1}}),
    ("Navigate backward", {"cats": {"go_back": 1}}),
    ("Backtrack", {"cats": {"go_back": 1}}),
    ("Revert to the previous screen", {"cats": {"go_back": 1}}),
    ("Return to the prior page", {"cats": {"go_back": 1}}),
    ("Move backward in navigation", {"cats": {"go_back": 1}}),
    ("Step back", {"cats": {"go_back": 1}}),
    ("Go in reverse", {"cats": {"go_back": 1}}),
    ("Retreat to the last page", {"cats": {"go_back": 1}}),
    ("Revisit the previous screen", {"cats": {"go_back": 1}}),

    ("Provide details about the images", {"cats": {"explain_images": 1}}),
    ("Describe the images", {"cats": {"explain_images": 1}}),
    ("Give information about the pictures", {"cats": {"explain_images": 1}}),
    ("Elaborate on the visuals", {"cats": {"explain_images": 1}}),
    ("Offer an explanation of the images", {"cats": {"explain_images": 1}}),
    ("Discuss the content of the pictures", {"cats": {"explain_images": 1}}),
    ("Clarify what the images depict", {"cats": {"explain_images": 1}}),
    ("Offer insights into the visuals", {"cats": {"explain_images": 1}}),
    ("Examine the imagery", {"cats": {"explain_images": 1}}),
    ("Explain about the images", {"cats": {"explain_images": 1}}),

    ("Describe the graph", {"cats": {"explain_graph": 1}}),
    ("Explain the data visualization", {"cats": {"explain_graph": 1}}),
    ("Provide details about the chart", {"cats": {"explain_graph": 1}}),
    ("Analyze the graphical representation", {"cats": {"explain_graph": 1}}),
    ("Discuss the plotted data", {"cats": {"explain_graph": 1}}),
    ("Interpret the graph", {"cats": {"explain_graph": 1}}),
    ("Elaborate on the graph", {"cats": {"explain_graph": 1}}),
    ("Give insights into the visual representation", {"cats": {"explain_graph": 1}}),
    ("Clarify what the graph depicts", {"cats": {"explain_graph": 1}}),
    ("Break down the chart", {"cats": {"explain_graph": 1}}),
    ("Explain the graphical data", {"cats": {"explain_graph": 1}}),

    ("Please translate to Sinhala", {"cats": {"translate_to_sinhala": 1}}),
    ("Translate this into Sinhala please.", {"cats": {"translate_to_sinhala": 1}}),
    ("Can you convert this to Sinhala?", {"cats": {"translate_to_sinhala": 1}}),
    ("I need this text in Sinhala please.", {"cats": {"translate_to_sinhala": 1}}),
    ("Could you provide a translation in Sinhala?", {"cats": {"translate_to_sinhala": 1}}),
    ("Please translate this into Sinhala.", {"cats": {"translate_to_sinhala": 1}}),
    ("I'm looking for a translation into Sinhala, please.", {"cats": {"translate_to_sinhala": 1}}),
    ("Is it possible to get this text translated into Sinhala?", {"cats": {"translate_to_sinhala": 1}}),
    ("Kindly translate this into Sinhala, please.", {"cats": {"translate_to_sinhala": 1}}),
    ("Can you render this in Sinhala?", {"cats": {"translate_to_sinhala": 1}}),
    ("I'd like this text converted into Sinhala, please.", {"cats": {"translate_to_sinhala": 1}}),

    ("Translate this into Tamil please.", {"cats": {"translate_to_tamil": 1}}),
    ("Can you convert this to Tamil?", {"cats": {"translate_to_tamil": 1}}),
    ("I need this text in Tamil please.", {"cats": {"translate_to_tamil": 1}}),
    ("Could you provide a translation in Tamil?", {"cats": {"translate_to_tamil": 1}}),
    ("Please translate this into Tamil.", {"cats": {"translate_to_tamil": 1}}),
    ("I'm looking for a translation into Tamil, please.", {"cats": {"translate_to_tamil": 1}}),
    ("Is it possible to get this text translated into Tamil?", {"cats": {"translate_to_tamil": 1}}),
    ("Kindly translate this into Tamil, please.", {"cats": {"translate_to_tamil": 1}}),
    ("Can you render this in Tamil?", {"cats": {"translate_to_tamil": 1}}),
    ("I'd like this text converted into Tamil, please.", {"cats": {"translate_to_tamil": 1}}),
    ("Please translate to Tamil", {"cats": {"translate_to_tamil": 1}}),

    ("Shut down the browser.", {"cats": {"close_browser": 1}}),
    ("Exit the browser.", {"cats": {"close_browser": 1}}),
    ("Close the browser window.", {"cats": {"close_browser": 1}}),
    ("Terminate the browser.", {"cats": {"close_browser": 1}}),
    ("End the browser session.", {"cats": {"close_browser": 1}}),  # no need this command
    ("Quit the browser.", {"cats": {"close_browser": 1}}),
    ("Stop the browser.", {"cats": {"close_browser": 1}}),
    ("Close the web browser.", {"cats": {"close_browser": 1}}),
    ("Turn off the browser.", {"cats": {"close_browser": 1}}),
    ("Shut the browser down.", {"cats": {"close_browser": 1}}),
    ("Close the browser", {"cats": {"close_browser": 1}})
]

# Define your use case labels
use_case_labels = ["goto_section", "read_hyperlinks", "read_content", "goto_homepage", "go_back",
                   "explain_images", "explain_graph", "translate_to_sinhala", "translate_to_tamil",
                   "close_browser"]

# Train the model
model = train_text_categorization_model(train_data, use_case_labels)


current_url = input("Enter the initial URL: ")
navigator = None  # Initialize navigator variable


def predict_intent_loop(model, use_case_labels, intent_functions):
    global navigator, current_url  # Access the navigator and current_url variables defined outside the function

    if navigator is None:  # If navigator object is not created yet, create it
        navigator = WebNavigator()
        if current_url:
            navigator.driver.get(current_url)  # Open the initial URL in the browser

    while True:
        test_command = input("Enter your command: ")
        predicted_intent = predict_intent(model, test_command, use_case_labels)
        if test_command.lower() == "close browser":
            print("Closing the browser...")
            if navigator is not None:
                quit_browser(navigator)  # Call quit_browser function with the navigator object
            break

        if predicted_intent == "goto_section":  # Check if the predicted intent is 'goto_section'
            current_url = goto_section_function(test_command, navigator,current_url)  # Update current_url after navigation
        elif predicted_intent in intent_functions:
            intent_functions[predicted_intent]()  # Call the corresponding function
        else:
            print("Command not recognized.")


intent_functions = {
    "goto_section": goto_section_function,
    "read_hyperlinks": read_hyperlinks_function,
    "read_content": read_content_function,
    "goto_homepage": goto_homepage_function,
    "go_back": go_back_function,
    "explain_images": explain_images_function,
    "explain_graph": explain_graph_function,
    "translate_to_sinhala": translate_to_sinhala_function,
    "translate_to_tamil": translate_to_tamil_function,
}

# Test the trained model
predict_intent_loop(model, use_case_labels, intent_functions)
