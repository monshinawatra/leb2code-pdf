with open("./5/myFile.txt", "r") as file:
    text = file.readlines()
    text = list(map(str.strip, text))
print("Total letters", len("".join(text)))
