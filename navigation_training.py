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

# Load the trained model

