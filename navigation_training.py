import spacy
from spacy.training.example import Example

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")

nlp = spacy.blank("en")
# Check if "ner" component exists in the pipeline, otherwise add it
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner") # loading the blank model

# Add new entity label for hyperlinks
ner.add_label("HYPERLINK")

# Training data in the format you provided
train_data = [
    {"text": "Go to home page", "entities": [(6, 10, "HYPERLINK")]},
    {"text": "Home page", "entities": [(0, 4, "HYPERLINK")]},
    {"text": "move to data section", "entities": [(8, 12, "HYPERLINK")]},
    {"text": "click the Games link", "entities": [(10, 15, "HYPERLINK")]},
    {"text": "open the puzzles", "entities": [(9, 16, "HYPERLINK")]},
    {"text": "I want to learn Geometry", "entities": [(16, 24, "HYPERLINK")]},
    {"text": "physics", "entities": [(0, 7, "HYPERLINK")]},
    {"text": "I want to go to basic maths", "entities": [(16, 27, "HYPERLINK")]},
    {"text": "Go to Ratios", "entities": [(6, 12, "HYPERLINK")]},
    {"text": "Go to LCM and HCF", "entities": [(6, 17, "HYPERLINK")]},
    {"text": "Explore LCM and HCF", "entities": [(8, 19, "HYPERLINK")]},
    {"text": "LCM and HCF", "entities": [(0, 11, "HYPERLINK")]},
    {"text": "Open Factorising Quadratics", "entities": [(5, 27, "HYPERLINK")]},
    {"text": "Click Factorising Quadratics", "entities": [(6, 28, "HYPERLINK")]},
    {"text": "Factorising Quadratics", "entities": [(0, 22, "HYPERLINK")]},
    {"text": "Move to Functions", "entities": [(8, 17, "HYPERLINK")]},
    {"text": "Open Gradients, Graphs and Curves", "entities": [(5, 33, "HYPERLINK")]},
    {"text": "Gradients, Graphs and Curves", "entities": [(0, 28, "HYPERLINK")]},
    {"text": "I want to go to Gradients, Graphs and Curves section", "entities": [(16, 44, "HYPERLINK")]},
    {"text": "Move to Gradients, Graphs and Curves", "entities": [(8, 36, "HYPERLINK")]},
    {'text': 'Open Stationary Points', 'entities': [(5, 22, 'HYPERLINK')]},
    {'text': 'Move to Stationary Points', 'entities': [(8, 25, 'HYPERLINK')]},
    {'text': 'Stationary Points', 'entities': [(0, 17, 'HYPERLINK')]},
    {'text': 'Click Stationary Points', 'entities': [(6, 23, 'HYPERLINK')]},
    {'text': 'Open Vectors', 'entities': [(5, 12, 'HYPERLINK')]},
    {'text': 'Go to Vectors', 'entities': [(6, 13, 'HYPERLINK')]},
    {'text': "Open Pythagoras' Theorem", 'entities': [(5, 24,'HYPERLINK')]},
    {'text': "Explore Pythagoras' Theorem", 'entities': [(8, 27, 'HYPERLINK')]},
    {'text': "Pythagoras' Theorem", 'entities': [(0, 19, 'HYPERLINK')]},
    {'text': "Go to Pythagoras' Theorem", 'entities': [(6, 25, 'HYPERLINK')]},
    {'text': 'Open Bounds', 'entities': [(5, 11, 'HYPERLINK')]},
    {'text': 'Click Bounds', 'entities': [(6, 12, 'HYPERLINK')]},
    {'text': 'Bounds', 'entities': [(0, 6, 'HYPERLINK')]},
    {'text': 'Go to Bounds', 'entities': [(6, 12, 'HYPERLINK')]},
    {"text": "Open Introduction to Algebra", "entities": [(5, 28, "HYPERLINK")]},
    {"text": "Go to Introduction to Algebra", "entities": [(6, 29, "HYPERLINK")]},
    {"text": "Introduction to Algebra", "entities": [(0, 23, "HYPERLINK")]},
    {"text": "Move to Introduction to Algebra", "entities": [(8, 31, "HYPERLINK")]},
    {"text": "Explore Introduction to Algebra", "entities": [(8, 31, "HYPERLINK")]},
    {"text": "I want to learn Introduction to Algebra section", "entities": [(16, 39, "HYPERLINK")]},
    {"text": "Balance when Adding and Subtracting", "entities": [(0, 35, "HYPERLINK")]},
    {"text": "Go to Balance when Adding and Subtracting", "entities": [(6, 41, "HYPERLINK")]},
    {"text": "Open Balance when Adding and Subtracting", "entities": [(5, 40, "HYPERLINK")]},
    {"text": "Explore Balance when Adding and Subtracting", "entities": [(8, 43, "HYPERLINK")]},
    {"text": "Go to Introduction to Algebra - Multiplication", "entities": [(6, 46, "HYPERLINK")]},
    {"text": "Introduction to Algebra - Multiplication", "entities": [(0, 40, "HYPERLINK")]},
    {"text": "Open Introduction to Algebra - Multiplication", "entities": [(5, 45, "HYPERLINK")]},
    {"text": "I want to learn Introduction to Algebra - Multiplication", "entities": [(16, 56, "HYPERLINK")]},
    {"text": "I want to study Introduction to Algebra - Multiplication", "entities": [(16, 56, "HYPERLINK")]},
    {"text": "Order of Operations - BODMAS", "entities": [(0, 28, "HYPERLINK")]},
    {"text": "Open Order of Operations - BODMAS", "entities": [(5, 33, "HYPERLINK")]},
    {"text": "Explore Order of Operations - BODMAS", "entities": [(8, 36, "HYPERLINK")]},
    {"text": "Click Order of Operations - BODMAS", "entities": [(6, 34, "HYPERLINK")]},
    {"text": "I want to learn Order of Operations - BODMAS section", "entities": [(16, 44, "HYPERLINK")]},
    {"text": "Open PEMDAS", "entities": [(5, 11, "HYPERLINK")]},
    {"text": "PEMDAS", "entities": [(0, 6, "HYPERLINK")]},
    {"text": "Explore PEMDAS", "entities": [(8, 14, "HYPERLINK")]},
    {"text": "I want to access PEMDAS", "entities": [(17, 23, "HYPERLINK")]},
    {"text": "Open Substitution", "entities": [(5, 17, "HYPERLINK")]},
    {"text": "Substitution", "entities": [(0, 12, "HYPERLINK")]},
    {"text": "Explore Substitution", "entities": [(8, 20, "HYPERLINK")]},
    {"text": "I want to access Substitution", "entities": [(17, 29, "HYPERLINK")]},
    {"text": "Equations and Formulas", "entities": [(0, 22, "HYPERLINK")]},
    {"text": "Open Equations and Formulas", "entities": [(5, 27, "HYPERLINK")]},
    {"text": "Explore Equations and Formulas", "entities": [(8, 30, "HYPERLINK")]},
    {"text": "Click Equations and Formulas", "entities": [(6, 28, "HYPERLINK")]},
    {"text": "Inequalities", "entities": [(0, 12, "HYPERLINK")]},
    {"text": "Open Inequalities", "entities": [(5, 17, "HYPERLINK")]},
    {"text": "Solving Inequalities", "entities": [(0, 20, "HYPERLINK")]},
    {"text": "Click Solving Inequalities", "entities": [(6, 26, "HYPERLINK")]},
    {"text": "Go to the Solving Inequalities section", "entities": [(10, 30, "HYPERLINK")]},
    {"text": "Open Solving Inequalities section", "entities": [(5, 25, "HYPERLINK")]},
    {"text": "Explore Solving Inequalities", "entities": [(8, 28, "HYPERLINK")]},
    {"text": "Exponent", "entities": [(0, 8, "HYPERLINK")]},
    {"text": "I want to learn Negative Exponents", "entities": [(16, 34, "HYPERLINK")]},
    {"text": "Negative Exponents", "entities": [(0, 18, "HYPERLINK")]},
    {"text": "Go to the Negative Exponents section", "entities": [(10, 28, "HYPERLINK")]},
    {"text": "Open Negative Exponents", "entities": [(5, 23, "HYPERLINK")]},
    {"text": "Explore Negative Exponents", "entities": [(8, 26, "HYPERLINK")]},
    {"text": "I want to learn Reciprocal in Algebra", "entities": [(16, 37, "HYPERLINK")]},
    {"text": "Reciprocal in Algebra", "entities": [(0, 21, "HYPERLINK")]},
    {"text": "Go to the Reciprocal in Algebra section", "entities": [(10, 31, "HYPERLINK")]},
    {"text": "Open Reciprocal in Algebra", "entities": [(5, 26, "HYPERLINK")]},
    {"text": "Explore Reciprocal in Algebra", "entities": [(8, 29, "HYPERLINK")]},
    {"text": "Open Square Roots", "entities": [(5, 17, "HYPERLINK")]},
    {"text": "Square Roots", "entities": [(0, 12, "HYPERLINK")]},
    {"text": "Go to the Square Roots section", "entities": [(10, 22, "HYPERLINK")]},
    {"text": "Open Cube Roots", "entities": [(5, 15, "HYPERLINK")]},
    {"text": "Cube Roots", "entities": [(0, 10, "HYPERLINK")]},
    {"text": "Explore Cube Roots", "entities": [(8, 18, "HYPERLINK")]},
    {"text": "I want to learn Cube Roots", "entities": [(16, 26, "HYPERLINK")]},
    {"text": "Go to the nth Roots section", "entities": [(10, 19, "HYPERLINK")]},
    {"text": "Open nth Roots", "entities": [(5, 14, "HYPERLINK")]},
    {"text": "nth Roots", "entities": [(0, 9, "HYPERLINK")]},
    {"text": "Open Surds", "entities": [(5, 10, "HYPERLINK")]},
    {"text": "Go to the Surds", "entities": [(10, 15, "HYPERLINK")]},
    {"text": "Surds", "entities": [(0, 5, "HYPERLINK")]},
    {"text": "Go to Applications of Linear Equations", "entities": [(6, 38, "HYPERLINK")]},
    {"text": "Applications of Linear Equations", "entities": [(0, 32, "HYPERLINK")]},
    {"text": "Go to Applications of Quadratic Equations", "entities": [(6, 41, "HYPERLINK")]},
    {"text": "Applications of Linear Equations", "entities": [(0, 32, "HYPERLINK")]},
    {"text": "Go to Absolute Value Equations", "entities": [(6, 30, "HYPERLINK")]},
    {"text": "Absolute Value Equations", "entities": [(0, 24, "HYPERLINK")]},
    {"text": "Go to Absolute Value Inequalities", "entities": [(6, 33, "HYPERLINK")]},
    {"text": "Absolute Value Inequalities", "entities": [(0, 27, "HYPERLINK")]},
    {"text": "Open Lines, Circles and Piecewise Functions", "entities": [(5, 43, "HYPERLINK")]},
    {"text": "Lines, Circles and Piecewise Functions", "entities": [(0, 38, "HYPERLINK")]},
    {"text": "Open Logarithm Functions", "entities": [(5, 24, "HYPERLINK")]},
    {"text": "Logarithm Functions", "entities": [(0, 19, "HYPERLINK")]},
    {"text": "Visit to Exponential Functions", "entities": [(9, 30, "HYPERLINK")]},
    {"text": "Exponential Functions", "entities": [(0, 21, "HYPERLINK")]},
    {"text": "Visit to Linear Systems with Two Variables", "entities": [(9, 42, "HYPERLINK")]},
    {"text": "Linear Systems with Two Variables", "entities": [(0, 33, "HYPERLINK")]},
    {"text": "Visit to Linear Systems with Three Variables", "entities": [(9, 44, "HYPERLINK")]},
    {"text": "Linear Systems with Three Variables", "entities": [(0, 35, "HYPERLINK")]},
    {"text": "Solving Inequality Word Questions", "entities": [(0, 33, "HYPERLINK")]},
    {"text": "Explore Solving Inequality Word Questions", "entities": [(8, 41, "HYPERLINK")]},
    {"text": "I want to study Completing the Square", "entities": [(16, 37, "HYPERLINK")]},
    {"text": "Completing the Square", "entities": [(0, 21, "HYPERLINK")]},
    {"text": "Equation of a Straight Line", "entities": [(0, 27, "HYPERLINK")]},
    {"text": "Open Equation of a Straight Line", "entities": [(5, 32, "HYPERLINK")]},
    {"text": "Visit to Equation of a Straight Line", "entities": [(9, 36, "HYPERLINK")]},
    {"text": "Equation of a Straight Line", "entities": [(0, 27, "HYPERLINK")]},
    {"text": "Explore Rationalizing The Denominator", "entities": [(8, 37, "HYPERLINK")]},
    {"text": "Rationalizing The Denominator", "entities": [(0, 29, "HYPERLINK")]},
    {"text": "I want to study Polynomial Long Multiplication", "entities": [(16, 46, "HYPERLINK")]},
    {"text": "Polynomial Long Multiplication", "entities": [(0, 30, "HYPERLINK")]},
    {"text": "open Polynomial Long Multiplication", "entities": [(5, 35, "HYPERLINK")]},
    {"text": "I want to study Directly Proportional and Inversely Proportional", "entities": [(16, 64, "HYPERLINK")]},
    {"text": "Directly Proportional and Inversely Proportional", "entities": [(0, 48, "HYPERLINK")]},
    {"text": "Open How to graph functions and linear equations", "entities": [(5, 48, "HYPERLINK")]},
    {"text": "How to graph functions and linear equations", "entities": [(0, 43, "HYPERLINK")]},
    {"text": "Visit How to solve system of linear equations", "entities": [(6, 45, "HYPERLINK")]},
    {"text": "How to solve system of linear equations", "entities": [(0, 39, "HYPERLINK")]},
    {"text": "Open Polynomial functions", "entities": [(5, 25, "HYPERLINK")]},
    {"text": "Polynomial functions", "entities": [(0, 20, "HYPERLINK")]},
    {"text": "Explore Exponential and logarithmic functions", "entities": [(8, 45, "HYPERLINK")]},
    {"text": "Exponential and logarithmic functions", "entities": [(0, 37, "HYPERLINK")]},
    {"text": "Visit to Graph inequalities", "entities": [(9, 27, "HYPERLINK")]},
    {"text": "Graph inequalities", "entities": [(0, 18, "HYPERLINK")]},
    {"text": "Visit to Solving systems of equations in two variables", "entities": [(9, 54, "HYPERLINK")]},
    {"text": "Solving systems of equations in two variables", "entities": [(0, 45, "HYPERLINK")]},
    {"text": "Visit to Solving systems of equations in three variables", "entities": [(9, 56, "HYPERLINK")]},
    {"text": "Solving systems of equations in three variables", "entities": [(0, 47, "HYPERLINK")]},
    {"text": "Go to Matrix properties", "entities": [(6, 23, "HYPERLINK")]},
    {"text": "Matrix properties", "entities": [(0, 17, "HYPERLINK")]},
    {"text": "Go to Matrix operations", "entities": [(6, 23, "HYPERLINK")]},
    {"text": "Matrix operations", "entities": [(0, 17, "HYPERLINK")]},
    {"text": "Go to How to graph quadratic functions", "entities": [(6, 38, "HYPERLINK")]},
    {"text": "How to graph quadratic functions", "entities": [(0, 32, "HYPERLINK")]},
    {"text": "Go to How to solve quadratic equations", "entities": [(6, 38, "HYPERLINK")]},
    {"text": "How to solve quadratic equations", "entities": [(0, 32, "HYPERLINK")]},
    {"text": "Go to Basic knowledge of polynomial functions", "entities": [(6, 45, "HYPERLINK")]},
    {"text": "Basic knowledge of polynomial functions", "entities": [(0, 39, "HYPERLINK")]},
    {"text": "Go to Operate on rational expressions", "entities": [(6, 37, "HYPERLINK")]},
    {"text": "Go to Logarithm and logarithm functions", "entities": [(6, 39, "HYPERLINK")]},
    {"text": "Go to Logarithm property", "entities": [(6, 24, "HYPERLINK")]},
    {"text": "Go to Arithmetic sequences and series", "entities": [(6, 37, "HYPERLINK")]},
    {"text": "Arithmetic sequences and series", "entities": [(0, 31, "HYPERLINK")]},
    {"text": "Go to Geometric sequences and series", "entities": [(6, 36, "HYPERLINK")]},
    {"text": "Geometric sequences and series", "entities": [(0, 30, "HYPERLINK")]},
    {"text": "Lines", "entities": [(0, 5, "HYPERLINK")]}





]

# Convert training data to Example objects
examples = []
for item in train_data:
    text = item["text"]
    entities = item["entities"]
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, {"entities": entities})
    examples.append(example)

# Fine-tune the model
nlp.begin_training()
for _ in range(50):  # Increase iterations for better results
    for example in examples:
        nlp.update([example])

# Save the fine-tuned model
nlp.to_disk("fine_tuned_model")
doc = nlp("I want to go to Stationary Points")
print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
# Load the trained model


