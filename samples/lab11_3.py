def is_prime(number):
    if number <= 1:
        return ""
    for i in range(2, number):
        if number % i == 0:
            return ""
    return "This is prime number"


n = int(input("Enter a number to test:"))
print(is_prime(n))
