sentence = "This is a sample sentence to demonstrate the program"
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word in the sentence:", longest_word)

