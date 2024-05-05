# Dictionary of valid words
valid_words = {"apple", "banana", "orange", "grape", "pear", "kiwi", "melon", "strawberry"}

# Example document
document = "I like apples and bannanas, but I don't like strawbery."

# Split the document into words
words = document.split()

# List to store misspelled words
misspelled_words = []

# Check spelling of each word
for word in words:
    # Convert word to lowercase for case-insensitive comparison
    word = word.lower()
    if word not in valid_words:
        misspelled_words.append(word)

# Print misspelled words
if misspelled_words:
    print("Misspelled Words:")
    for word in misspelled_words:
        print(word)
else:
    print("No misspelled words found.")


