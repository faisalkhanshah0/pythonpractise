#!/usr/bin/env python
class Employee:
    pass

class Manager(Employee):
    'This is documentation'
    def personalDetails():
        pass;

print("name :",Manager.__name__); # Class name
print("Bases :",Manager.__bases__); # A possily empty tuple containing the base classes, in the order of their occurence in the base class list.
print("Doc :",Manager.__doc__); # Class documentation string, or None if undefined.
print("Module :",Manager.__module__); # Module name in which the class is defined. This attr is "__main__" in interactive mode
print("Dict :",Manager.__dict__);  # Contains the class's namespace
