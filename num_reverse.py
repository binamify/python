#Reversing Number In Python

#Method One
 
  
num = int(input("Number: ")) #input from user
reversed_num = 0

while num != 0:  
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10   

print("Reversed Number is: " , reversed_num )

#Reversing Number in Python(Slice Method)

num = int(input("Number: ")) #input from user

string_for_num = str(num) #converting to string for slicing

print("Revered Number is: " + string_for_num[::-1])

