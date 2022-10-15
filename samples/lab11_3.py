with open("./5/myFile.txt", "r") as file:
    text = file.read().split()
print("Total words are", len(text))
