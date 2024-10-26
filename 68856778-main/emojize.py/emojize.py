import emoji

# Yeahhh I should've read into the emoji documentation more...
# The code will automatically know what word is an emoji code and what word isn't.
# I also had trouble trying to make the code print ":smile_cat:" and after googling I
# found out that you need to add "language='alias'" within the emojize() function.

response = input("Input: ")

print("Output: " + emoji.emojize(response, language="alias"))
