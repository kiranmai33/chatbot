import spacy
from nltk.tokenize import word_tokenize
import random

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Hi!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "name_query": ["What's your name?", "May I know your name?"],
    "default": ["I'm not sure how to respond to that.", "Can you tell me more?", "That's interesting!"]
}

def get_response(intent):
    return random.choice(responses.get(intent, responses["default"]))

def identify_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greeting"
        if token.lemma_ in ["bye", "goodbye", "see", "later"]:
            return "goodbye"
        if token.lemma_ in ["name"]:
            return "name_query"
    return "default"

def main():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot:", get_response("goodbye"))
            break
        intent = identify_intent(user_input)
        response = get_response(intent)
        print("Chatbot:", response)
        
if __name__ == "__main__":
    main()
