#!/usr/bin/env python
class Employee:
    """docstring forOne."""
    __salary = 0;  #private variable can not be accessible from outside of class.

    def show(self):
        print(self.name,self.__salary);


emp1 = Employee();
emp1.name = 'shah';
# print(emp1.salary);
emp1.__salary = 10000; #not accessible from here
emp1.show();
