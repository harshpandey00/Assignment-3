num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    i = 1
    while i <= num:
        fact *= i
        i += 1
    print("The factorial of", num, "is", fact)
