# English-to-Foreign language dictionary
english_to_foreign = {
    "hello": "bonjour",
    "world": "monde",
    "how": "comment",
    "are": "êtes",
    "you": "vous"
}

# Sample English sentence
english_sentence = "hello world! how are you?"

# Split the sentence into words
english_words = english_sentence.split()

# Translate each word using the dictionary
foreign_words = [english_to_foreign.get(word, word) for word in english_words]

# Join the translated words to form the translated sentence
foreign_sentence = ' '.join(foreign_words)

# Print the translated sentence
print("Translated Sentence:", foreign_sentence)

