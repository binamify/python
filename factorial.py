# Python Program to calculate factorial

num = int(input("Enter a Number: "))
factorial = 1

if num < 0:
    print("Factorial doesn't exists for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial *= i
    print("The factorial of ", num , "is", factorial)