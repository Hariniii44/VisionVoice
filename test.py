
import spacy


def process_query(query):
    nlp = spacy.load("model/trained_ner")

    doc = nlp(query)
    recognized_websites = []

    for ent in doc.ents:
        if ent.label_ == "WEBSITE":
            website_name = ent.text.lower()
            recognized_websites.append(website_name)

    if not recognized_websites:
        print("I'm sorry, you didn't mention a correct website name")
        return None
    else:
        trained_websites = ["oxnotes", "khanacademy", "mathisfun", "cliffsnotes"]
        for website in recognized_websites:
            if website in trained_websites:
                # Determine the appropriate TLD based on the website name

                tld = ".com"  # Default TLD
                if website == "khanacademy":
                    tld = ".org"

                # Return the constructed URL without opening it
                return f"https://{website.replace(' ', '').lower()}"

        # If none of the recognized websites match the trained websites
        print("I'm sorry, none of the recognized websites are in the list of trained websites.")
        return None