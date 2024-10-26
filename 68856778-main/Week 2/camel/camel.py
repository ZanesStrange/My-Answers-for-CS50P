camel_case = input("camelCase: ")

output = ""

for letter in camel_case:
    # At this point you still assigned the letter variable to anything so you need add a function that
    # makes the program automatically assign the letter variable.
    if letter.isupper():
        # In this case by using the .isupper() function the program will automatically make each letter
        # of camel_case into a sort of list and assign that list into the letter variable.
        output += '_' + letter.lower()
        # "+=" means to later on add something.

        # For example: x = 3
        #              x += 2
        #              print(x)
        #              >>> 5

        # This will still only print out as "_c" if you write "camelCase."
        # The if statement will only seek for the uppercase letters and make it print
        # the converted section only.
    else:
        output += letter
        # By adding the else statement and making it print out the letters that don't fit the uppercase
        # criteria as they are originally. This will make the program loop the cycle of converting the
        # letter's that match the .isuppercase() function and just outputting the letter's that don't the
        # way they are.
print("snake_case: " + output)
