#!/usr/bin/env python
import sys
def abc(message,times = 1):
    print(message * times)
abc('Hello')
abc('world\n',5)
"""print('\a') #beep not working

sys.stdout.write('\a')   #beep not working
sys.stdout.flush() #beep not working"""

def func(*numbers): #factorial in some new way through python
    fact=1
    for n in numbers:
        print('Number at index {0} is {1}'.format(numbers.index(n),n))
        fact=fact*n;
        # print(numbers.index(n))
    print('fact is ',fact);
func(1,2,3,4,5)

def test(farg, **kwargs): #important multi param in keyvalue pair
    print('formal arg : ',farg)
    for key in kwargs:
        print('another keyword arg: %s: %s' %(key, kwargs[key]))

test(farg=1,myarg1='two', myarg2='three')
