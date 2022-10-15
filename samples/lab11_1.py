try:
    with open("./5/myFiles.txt", "r") as file:
        print(file.read())
    print("Successfully print content in myFile.txt")
except FileNotFoundError:
    print("Unable to open file myFile.txt")
