menu = {
  "Baja Taco": 4.25,
  "Burrito": 7.50,
  "Bowl": 8.50,
  "Nachos": 11.00,
  "Quesadilla": 8.50,
  "Super Burrito": 8.50,
  "Super Quesadilla": 9.50,
  "Taco": 3.00,
  "Tortilla Salad": 8.00
}
# I originally had the total_price variable inside the while loop which made the
# program constantly reset the total_price variable to 0 since the loop constantly ran
# "total_price = 0" which made the output $0.00 constantly.
total_price = 0

while True:
    try:
        # In order to make the code recognize the item in the dictionary even if the input
        # isn't titlecased, I used the "title()" method so that even if it's all lowercase,
        # the code will automatically change the input into titlecase so that it could recognize the
        # item from the dictionary.
        item = input("Item: ").title()
    # An EOFError (End-Of-File-Error) happens when the input function reachs the end of a file.
    # In this case, control-d signifies that there is nothing else to input anymore or that the file
    # has ended, thus you can use this for the try and except statement.
    except EOFError:
        # By inputting control-d, the program will automatically know that it is an
        # EOFError but you need to press enter for the program to properly end.
        # That's why you can't end it with just break and will also need to add a print function
        # that automatically creates a new line. This is still not over since by adding that,
        # there will be literally a new line after "Item: ". To solve that in order to make it
        # more aesthetically pleasing, you need to use the end function and set it to nothing, and thus
        # the program will end cleanly.
        print("\n", end="")
        break
    if item in menu:
        total_price = total_price + menu[item]
        # I used an f-string to convert the total_price into a str whilst keeping the 2 decimals
        # even if the numbers after the decimal point are 0, and adding the "Total: $" prompt as well.
        print(f"Total: ${total_price:.2f}")
