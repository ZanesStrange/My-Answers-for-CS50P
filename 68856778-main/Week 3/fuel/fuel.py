# To prompt the user again until the program gets the input it expects, I used a while loop.
while True:
    fraction = input("Fraction: ")
    fraction = fraction.split("/")
    # The code I wrote before this actually nested the try and except statements in an else statement, which is not wrong but not really
    # a concise of writing code. To make it more concise you can not use the else statement and instead just use continue to make the code
    # go to the next criteria.
    try:
        x = int(fraction[0])
        y = int(fraction[1])
    except ValueError:
        continue

    try:
        result = f"{x/y:.2f}"
    except ZeroDivisionError:
        continue

    percentage = f"{int(float(result)*100)}"
    # Because there is no error that can be described for the "E" and "F" conditions,
    # I decided to use if statements for them.
    if percentage == "0":
        print("E")
        break
    elif percentage == "100":
        print("F")
        break
    # I made the percentage variable automatically become a str by using the f-string function,
    # so in order to use the "is bigger than" condition, I converted the percentage variable into an int.
    elif int(percentage) > 100:
        continue
    else:
        print(percentage + "%")
        break
