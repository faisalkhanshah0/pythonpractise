import os

def performoperation(oprtr):
    numone = int(input('enter your first number : '))
    numtwo = int(input('enter your second number : '))
    if(oprtr == '+'):
        print('Sum of {0} + {1} = {2}'.format(numone,numtwo,numone+numtwo))
    elif(oprtr == '-'):
        print('Sum of {0} - {1} = {2}'.format(numone,numtwo,numone-numtwo))
    elif(oprtr == '*'):
        print('Sum of {0} * {1} = {2}'.format(numone,numtwo,numone*numtwo))
    elif(oprtr == '/'):
        print('Sum of {0} / {1} = {2}'.format(numone,numtwo,numone/numtwo))
    else:
        print('forcely ended.')

def mainfunc():
    print('Main Menu')
    print('Enter + for Addition')
    print('Enter - for Subtraction')
    print('Enter * for Multiplication')
    print('Enter / for division')
    oprtr=input('enter your selection : ')
    if (oprtr == '+' or oprtr == '-' or oprtr == '*' or oprtr == '/'):
        performoperation(oprtr)
    else:
        clear = lambda: os.system('clear') #on Linux System
        clear()
        print('wrong input passed')
        mainfunc()
mainfunc()
