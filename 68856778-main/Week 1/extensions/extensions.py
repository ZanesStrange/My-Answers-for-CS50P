def main():
    extension()

def extension():
    filename = input("File name: ").strip()
    filename = filename.split('.')[-1]

    match filename:
        case "gif":
            print("image/" + filename)
        case "jpg":
            print("image/" + filename)
        case "jpeg":
            print("image/" + filename)
        case "png":
            print("image/" + filename)
        case "pdf":
            print("image/" + filename)
        case "txt":
            print("image/" + filename)
        case "zip":
            print("image/" + filename)
        case _:
            print("application/octet-stream")

main()
