#!/usr/bin/env python
x=10
def abc():
    global x;
    print(x);
    x=2;
    print(x);
abc();
print(x);
