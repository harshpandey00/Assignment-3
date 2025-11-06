import math


num = float(input("Enter a number: "))

if num <= 0:
    print("For logarithm and square root, please enter a positive number.")
else:
    # Calculations using math module
    square_root = math.sqrt(num)
    natural_log = math.log(num)
    sine_value = math.sin(num)

    # Display results
    print("Square root of", num, "is:", square_root)
    print(" logarithm of", num, "is:", natural_log)
    print("Sine is:", sine_value)
