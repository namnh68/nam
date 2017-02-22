# -*- coding: utf-8 -*-
# Author: Nguyen Hoai Nam

# A example use try...except
# Function


def division(x, y):
    try:
        return x/y
    except ZeroDivisionError as error:
        print error

# while True:
#     try:
#         x = int(raw_input("Please input a number: "))
#         break
#     except ValueError:
#         print "OMG! That was no valid number. Try again !!!"

print "one"
a = division(5, 4)
print a
##
print "======"
##
print "two"
b = division(100, 0)
print b




