# Author: Nam Nguyen Hoai
# This file is to explain how to use classmethod and staticmethod.
# Source: https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner

# We have this class:


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

# Let's assume that we want to create a lot of Date class instances having
# date information coming from outer source encoded as a string of next
# format ('dd-mm-yyyy'). We have to do that in different places of our source
# code in project.

# This time, we have to do like this:
date1 = '03-03-2012'
day, month, year = map(int, date1.split('-'))
date1_after_convert = Date(day, month, year)
print date1_after_convert.day
print date1_after_convert.month
print date1_after_convert.year
print "############"
# However, if we use classmethod then we will to modify the class like this:


class DateClassMethod(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        # cls: represent class DateClassMethod.
        # cls() is equivalent with DateClassMethod()
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)

date2 = '30-07-1993'
date2_after_convert = DateClassMethod.from_string(date2)
print date2_after_convert.day
print date2_after_convert.month
print date2_after_convert.year
print "##############"
# With staticmethod, we will modify like this:


class DateStaticMethod(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def from_string(date_as_string):
       day, month, year = map(int, date_as_string.split('-'))
       return day <= 31 and month <= 12 and year <= 3999

is_date = DateStaticMethod.from_string('11-09-2012')
print is_date

# My conclusion:
# When we use @classmethod for a function then the function is
# the function of class. And we don't need to create a object
# when we want to call the function

