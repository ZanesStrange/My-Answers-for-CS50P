vowels = ["a", "i", "e", "o", "u"]
text = input("Input: ")
output = ""

for letter in text:
    if letter in vowels:
        output += ''
    else:
        output += '' + letter

print("Output: " + output)
