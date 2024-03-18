import webbrowser
import spacy
from spacy.tokens import Doc
from spacy.training.example import Example
import spacy.util
import random


def train_custom_model():
    nlp = spacy.blank("en")  # loading the blank model
    ner = nlp.add_pipe("ner")  # adding NER pipeline
    ner.add_label("WEBSITE")

    labeled_data = [
        {
            "text": "Go to the website oxnotes",
            "tokens": [
                {"start": 0, "end": 2, "id": 0, "orth": "Go", "tag": "VERB", "dep": "ROOT"},
                {"start": 3, "end": 5, "id": 1, "orth": "to", "tag": "ADP", "dep": "prep"},
                {"start": 6, "end": 9, "id": 2, "orth": "the", "tag": "DET", "dep": "det"},
                {"start": 10, "end": 17, "id": 3, "orth": "website", "tag": "NOUN", "dep": "pobj"},
                {"start": 18, "end": 25, "id": 4, "orth": "oxnotes", "tag": "WEBSITE", "dep": "attr"},
            ],
        },
        {
            "text": "Visit KhanAcademy",
            "tokens": [
                {"start": 0, "end": 5, "id": 0, "orth": "Visit", "tag": "VERB", "dep": "ROOT"},
                {"start": 6, "end": 17, "id": 1, "orth": "KhanAcademy", "tag": "WEBSITE", "dep": "attr"},
            ]
        },
        {
            "text": "Open the Mathisfun website",
            "tokens": [
                {"start": 0, "end": 4, "id": 0, "orth": "Open", "tag": "VERB", "dep": "ROOT"},
                {"start": 5, "end": 8, "id": 1, "orth": "the", "tag": "DET", "dep": "det"},
                {"start": 9, "end": 18, "id": 2, "orth": "Mathisfun", "tag": "WEBSITE", "dep": "compound"},
                {"start": 19, "end": 25, "id": 3, "orth": "website", "tag": "NOUN", "dep": "attr"},
            ]
        },
        {
            "text": "Open cliffsnotes.com",
            "tokens": [
                {"start": 0, "end": 4, "id": 0, "orth": "Open", "tag": "VERB", "dep": "ROOT"},
                {"start": 5, "end": 16, "id": 1, "orth": "cliffsnotes", "tag": "WEBSITE", "dep": "attr"},
            ]
        }
    ]

    examples = []
    for example_data in labeled_data:
        tokens = example_data["tokens"]
        words = [token["orth"] for token in tokens]
        spaces = [True] * len(words)
        doc = Doc(nlp.vocab, words=words, spaces=spaces)
        entities = []     #this is to find the website in which is any form
        for token in tokens:
            if "WEBSITE" in token["tag"]:
                entities.append((token["start"], token["end"], "WEBSITE"))
        example = Example.from_dict(doc, {"entities": entities})
        examples.append(example)



    nlp.begin_training()
    for _ in range(20):
        random.shuffle(examples)
        for example in examples:
            nlp.update([example], drop=0.5)

    nlp.to_disk("model/trained_ner")
