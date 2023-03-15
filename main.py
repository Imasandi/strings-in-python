# numbers
# common data types in python
# basics of using numbers
# different types of numbers
# functions that can be using in python

#import math function
from math import *

print(2.0345)
print(2)
print(-3.5435)

# basic arithmetics
print(3.45 + 3)
print(3*5)
print(2-3)
print(6/3)

# parenthesis
print(3*5+4)
print(3*(5+4))

# moules
print(10 % 3)  # gives the remainder of the division

# store the numbers inside of variables
my_num = -5
print(my_num)

#convert number into a string
print(str(my_num))
print(str(my_num ) + " is my favourite number")  # need to have "str" infront in order to type the number and string together


# print(my_num + "is my favourite number") ---- this function gives an error

#abs -- absolute value of a number
print(abs(my_num))

# pow -- power of the number --4 to the power 3
print(pow(4,3))


# max function -- return the larger  number
print(max(3,8)) # shows which number is higher

# min -- opposite-- return small value
print(min(2, 9))

# round  --- round a number

# converting a number function to a string
# using string inside a number function by converting it into a string
# using a variable inside a number function


round_num = 3.6
print(round(round_num))

print(str(round(round_num))+" is the rounded value ", round_num)

# ceil function --- round the number in the largest decimal
print(ceil(3.1))  # round the number to the largest decimal no matter what decimal is there


# floor method --- grab the lowest number
print(floor(3.7)) # cut off the decimal number

# squire root function
print(sqrt(36))



