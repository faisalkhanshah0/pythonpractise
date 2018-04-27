#this is first comment type
""" asdf asdfasdf
asdfasdf
asdfasdf
"""

"""print('hello comment')
global x;
def abc():
    print('inside function abc')
    x=4
    print(x)
def xyz():
    global x;
    x=5
    print('inside function xyz')
    print(x)
xyz()
print(x)
abc()"""

#Next Example for global & local vars
x=50
def func():
    global x;
    print('x is ',x);
    x=2;
    print('changed global x is ',x)

func()
print('value of x is ',x)
