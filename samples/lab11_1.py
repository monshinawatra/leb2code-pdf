def hello_to_my_friend(name: str):
    if name.capitalize() in ["Jeff", "Jack", "Jim"]:
        print(f"Hello, {name.capitalize()}. Good morning my friend!")
    else:
        print("Who are you?", f"Nice to meet you anyway...{name.capitalize()} :).", sep="\n")


name_input = input("What is your name?:")
hello_to_my_friend(name_input)
