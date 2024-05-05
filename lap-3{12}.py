# Sample text
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Lorem ipsum dolor sit amet"

# Split the text into words
words = text.split()

# Initialize an empty dictionary to store word frequencies
word_freq = {}

# Count the frequency of each word
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Print the word frequencies
for word, freq in word_freq.items():
    print(f"'{word}': {freq}")

