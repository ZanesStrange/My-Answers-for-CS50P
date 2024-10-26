import sys
import pyfiglet
# At first I was using "from pyfiglet import Figlet", but in order to access the list
# of fonts available I had to switch to "import pyfiglet".
# "sys.argv" includes the "figlet.py" part so I had to change the "len(sys.argv)"
# from 0 to 1.
if len(sys.argv) == 1:
    text = input("Input: ")
    # You need to set the formatting of the text beforehand.
    f = pyfiglet.Figlet()
    print("Output: " + "\n" + f.renderText(text))
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    # In order to make the code recognize the fonts that are not available I used
    # "pyfiglet.FigletFont.getFonts()" to get the list of fonts available for figlet
    # and use an if statement for the code to check whether the font is in the figlet font list
    # or not.
    if sys.argv[2] in pyfiglet.FigletFont.getFonts():
        text = input("Input: ")
        f = pyfiglet.Figlet(font=sys.argv[2])
        print("Output: " + "\n" + f.renderText(text))
    else:
        sys.exit
        print("Invalid usage")
else:
    sys.exit
    print("Invalid usage")
