# Python Program to find Factors of a Number
 
number =6

value = 1
print("Factors of a Given Number {0} are:".format(number))

while (value <= number):
    if(number % value == 0):
        print("{0}".format(value))
    value = value + 1
