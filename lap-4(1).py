import string

# Input string
sentence = "Hello! How are you? This is a test sentence. Hello, world!"

# Remove punctuation from the sentence
sentence = sentence.translate(str.maketrans('', '', string.punctuation))

# Convert the sentence to lowercase
sentence = sentence.lower()

# Split the sentence into words
words = sentence.split()

# Create a dictionary to store word frequencies
frequency = {}

# Count the frequency of each word
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Print the word frequencies
for word, freq in frequency.items():
    print(f"{word}: {freq}")

