def main():
    Question()
def Question():
    Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    match Answer:
        case "42":
            print("Yes")
        case "Forty Two":
            print("Yes")
        case "forty-two":
            print("Yes")
        case _:
            print("No")
main()
