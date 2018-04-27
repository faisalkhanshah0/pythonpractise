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
