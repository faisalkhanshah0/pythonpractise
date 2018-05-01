"""f=open('test.txt','r');
str = f.readline();
while(str!=''):
    print(str);
    str=f.readline();"""

"""f=open('test.txt','r');
str = f.readlines();
for i in str:
    print(i);"""

"""f=open('test.txt','r');
str = f.read(20); #read only 20 bytes from file
print(str);
f.close();"""


f1=open('test.txt','r');
str = f1.read();
print(str);
print('=============');
lines=str.splitlines();
print(lines);
f1.close();
