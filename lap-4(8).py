input_string = "hello"
result_string = ""

for char in input_string:
    if char not in result_string:
        result_string += char

print("Original string:", input_string)
print("String with duplicates removed:", result_string)
