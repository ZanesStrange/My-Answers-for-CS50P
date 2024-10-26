# At first I was using a dictionary but after checking out someone else's code,
# I realized it would be hard to count the values in the dictionary. So instead,
# I decided to use 2 lists: 1 for the items inputted and 1 for the number of items.
grocery_list = []
number = []

# The while loop is for adding the inputted items in the list.
# So as long as there is an input, the while loop will constantly stay True.
while True:
    try:
        grocery = input("").upper()
    except EOFError:
        print("\n", end="")
        break
    # This line is what adds the input to the grocery_list. By adding the
    # .append() method, you can add items to a list.
    grocery_list.append(grocery)

# In this line, I'm redefining grocery_list because the list has no particular order.
# In order to make the grocery_list be in alphabetical order, you use the sorted() function.
grocery_list = sorted(grocery_list)

# One of the reasons why I thought dictionaries wouldn't work is because they will automatically
# exclude items that are already in the dictionary. Lists on the other hand, don't have this and
# will include the repeated items. In this line, I used the set() function so that the code will
# be able to identify the repeated items and gather them in a set.
# Also, if you convert a list to a set, the set won't be in alphabetical order anymore, unless you
# use the sorted() function on the set.
groceries = sorted(set(grocery_list))

# In order to count the items, I used a for loop within the groceries set I created earlier.
for i in groceries:
    # However, if I use the .count() method on the groceries set, the output will always be "1", since
    # all the repeated items have been excluded. So, I used the .count() method on the grocery_list
    # so that the code can find the repeated items that i is iterating, and then add the counted numbers
    # in the number list.
    number.append(grocery_list.count(i))
    # Then I just printed both of the values in the format that was given, and tried to convert the values into
    # a str so that it won't cause a syntax error.
    print(str(grocery_list.count(i)) + " " + str(i))

# I think the number list was unnecessary but I'll just keep it there to remind myself of this.
