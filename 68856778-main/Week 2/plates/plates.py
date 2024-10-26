def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(a):
     if two_letters(a) and min_max(a) and middle_num(a) and punctuation(a):
          return True
     else:
          return False


def two_letters(b):
     # A lot of other people were using the split method.
     # Example:
     #         if b[0:2].isalpha and b[1:2].isalpha():
     #              return True
     #         else:
     #              return False
     #
     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
     plate_letters = list(b)
     # By doing this it would prevent the clash between the two_letters() function
     # and the min_max() function.
     if len(b) < 2:
          return False
     # .isalpha() is used to indentify whether the str contains only alphabetical
     # characters.
     if plate_letters[0].isalpha() and plate_letters[1].isalpha():
          return True
     else:
          return False

def min_max(b):
     if 2 <= len(b) <= 6:
          return True
     else:
          return False

def punctuation(b):
     # .isalnum() is for indentifying whether the str only contains alphabetical or
     # numerical characters.
     if b.isalnum():
          return True
     else:
          return False


def middle_num(b):
     # The middle_num() function will need to be preset to False.
     # Otherwise the code will think that has to be at least one digit in the input.
     # So by presetting the function as False by assigning the variable "has_digit"
     # as False and making the program change it to True when it indentifies a digit,
     # it won't make the program think that the input needs a number.
     has_digit = False
     for i in b:
          # The isdigit() method is used to check whether a character is a digit or not (0~9).
          # The difference between isdigit() and isnumeric() is that isdigit() only recognizes
          # regular mathematical numbers, whereas isnumberic() recognizes many other characters that
          # function as numbers such as roman numerals.
          if i.isdigit():
               has_digit = True
               result = b.index(i)
               # The "[result:]" means every character after "i"/"result".
               # That way it checks whether the characters afer "i" are digits
               # or letters.
               if b[result:].isdigit() and int(i) != 0:
                    return True
               else:
                    return False
     # This does mean "return True" and you CAN write it like that, but by writing it
     # this way, it makes the code a lot easier to understand.
     return not has_digit

main()
