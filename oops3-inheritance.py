#!/usr/bin/env python

#=======================

class One:
    """One class"""
    def __init__(self, x, y):
        print('init of one');
    def func1(self):
        print('func1 of class one.');

class Two(One):
    """Two class"""
    def __init__(self, x, y, z):
        print('init of two');
    def func2(self):
        print('func2 of class two');
        #One.__init__(self, x, y); #calling parent constructor
        One.func1(self); # not required as two accessing full properties of one already

class Three(One):
    """Three class"""
    def __init__(self, x, y, z):
        print('init of three');
    def func3(self):
        print('func3 of class three');
        One.func1(self);

one = One(1,2);
one.func1();
print('-----------');

two = Two(20,30,40);
two.func1(); #making calls from parent class
two.func2();
print('-----------');

three = Three(98,99,100);
three.func1(); #making calls from parent class
three.func3();
print('------------');

objects = [two, three];
for obj in objects:
    obj.func1();
    print('*************');
