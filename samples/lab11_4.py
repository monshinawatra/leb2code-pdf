def cel2far(cur: int, stop: int, temp_list: list = []):
    if cur <= stop:
        text = f"{cur} Celcius = {(9/5)*cur + 32:.2f} Farenheit"
        print(text)
        temp_list.append(text)
        cel2far(cur + 1, stop, temp_list)
        return
    with open("./5/multiply.txt", "w") as file:
        for temp in temp_list:
            file.write(temp + "\n")


start = int(input("Enter a beginning of Celcius value: "))
stop = int(input("Enter an ending of Celcius value: "))
cel2far(start, stop)
