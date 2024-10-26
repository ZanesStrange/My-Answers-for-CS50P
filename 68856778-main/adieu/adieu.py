names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    names.append(name)
