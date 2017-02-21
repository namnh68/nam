# -*- coding: utf-8 -*-
# Author: Nguyen Hoai Nam

def kwargs_example(x, y, **kwargs):
    print x
    print y
    print kwargs # kwargs is dict
    print type(kwargs)
    print '======='
    print "All keys of kwargs:", kwargs.keys()
    print "All values of kwargs:", kwargs.values()


foo = kwargs_example(100, 200, name='nam', school='PTIT')

