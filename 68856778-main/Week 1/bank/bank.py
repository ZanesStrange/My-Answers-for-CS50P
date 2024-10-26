def main():
    greet()

def greet():
    Greeting = input("Greeting: ").lower().strip()

    if "hello" in Greeting:
        print("0$")
    elif "h" == Greeting[0]:
        print("20$")
    else:
        print("100$")

main()
