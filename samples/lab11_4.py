def create_list(iter):
    num_list = [float(input()) for _ in range(iter)]
    print("The enter list is ", num_list)
    return num_list


def find_min_max(num_list):
    return f"The maximum number entered is {max(num_list)} \nThe mininum number entered is {min(num_list)}"


n = int(input("Enter number of elements : "))
numbers = create_list(n)
print(find_min_max(numbers))
