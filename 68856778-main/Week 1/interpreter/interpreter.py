expression = input("Expression: ").strip()

x, y, z = expression.split(" ")

x = int(x)

z = int(z)

match y:
    case "+":
        #One guy used "F-strings" to make it more concise

        #print(f"{x+z:.1f}")

        add = float(x + z)
        print(add)
    case "-":

        #print(f"{x-z:.1f}")

        sub = float(x - z)
        print(sub)
    case "*":

        #print(f"{x*z:.1f}")

        mult = float(x * z)
        print(mult)
    case "/":

        #print(f"{x/z:.1f}")

        divi = float(x / z)
        print(divi)
    case _:
        print("")
