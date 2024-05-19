char = input("Enter a character: ")
char = char.lower()
if char in ('a', 'e', 'i', 'o', 'u'):
    print("The entered character '{}' is a vowel.".format(char))
elif char.isalpha():
    print("The entered character '{}' is a consonant.".format(char))
else:
    print("Invalid input. Please enter a valid alphabetic character.")

