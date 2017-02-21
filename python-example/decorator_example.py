# -*- coding: utf-8 -*-

# We have a fucntion to return the total of two number as below content:

def add(x, y):
    return x + y

# Test
print add(100,300)

# Now we have two condition.
# Condition 1:  If x < 100 and y < 100 then raise Exception. 
# Condition 2: We must still use all add function and don't 
# modify conent of the add function.

def wrapper(func): #1
    def inner(x, y): #2
        if x < 100 or y < 100: #3
            raise TypeError #4
        else: #5
            return func(x, y) #6
    return inner #7


