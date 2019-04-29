#!/usr/bin/env python
class Employee(object):
    """docstring for ."""
    empCount = 0;
    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;
        Employee.empCount +=1;
    def displayCount(self):
        print("Total Employees {0}".format(Employee.empCount));
    def displayEmployee(self):
        print("Name : {0}, Salary : {1}".format(self.name, self.salary));

emp1 = Employee('Mohan',10000);

emp1.email="c-shah.faisal@timesinternet.in" # adding prop at runtime
print(emp1.email);
del emp1.email; #deleting attr of object at runtime
# del keyword also remove the reference of the given attr so that garbase collection esily detect which prop to delete.

if hasattr(emp1,'email'):
    print('Found email : ');
    print(getattr(emp1,'email'));
else:
    print('Email not found & we have created it');
    setattr(emp1,'email','c-shah.faisal@timesinternet.in');
    print(getattr(emp1,'email'));
    del emp1.email; #deleting attr of object at runtime


emp1.displayCount();
emp1.displayEmployee();
emp2 = Employee('Atul',15000);
emp2.displayCount();
emp2.displayEmployee();
emp3 = Employee('Vivek',12000);
emp3.displayCount();
emp3.displayEmployee();

""" shallow copy both objects referencing to same location that
means if you change value of prop of any object leads to change in another."""
emp4 = emp3;
emp4.displayCount();
emp4.displayEmployee();

"""deep copy of object and its inner content like object.create in javascript"""
import copy;
emp5 = copy.copy(emp2);
emp5.displayCount();
emp5.displayEmployee();
