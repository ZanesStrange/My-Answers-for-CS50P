# In this case the code is only asking for the calories of the fruit that's
# being entered, so there's no need to create a list of dictionaries.
# Also, you can't use index in dictionaries, therefore, you can't treat the
# items that are in a category you created by listing dictionaries like list.
# Even if you print out the items in the category, the program is only going to see
# the items in that category as separate things.
fruit_calories = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
    }

item = input("Item: ").lower().strip()
if item in fruit_calories:
    # By putting the item inside the [], this makes the program output the calories that
    # correspond with the item.
    print("Calories: " + fruit_calories[item])
