#!/usr/bin/env python
class One:
    """docstring for One."""
    def func1(self):
        print('func1 from class One');

class Two:
    """docstring for Two."""
    def func2(self):
        print('func2 from class Two');

class Three:
    """docstring for Three."""
    def func3(self):
        print('func3 from class Three');

class Four:
    """docstring for Four."""
    def func4(self):
        print('func4 from class Four');

class Child(One, Two, Three, Four):
    """docstring for Child."""
    pass;

obj = Child();
obj.func1();
obj.func2();
obj.func3();
obj.func4();
