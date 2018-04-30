#custom modules example
import eg; #i have not included this module in folder so it searches for "PYTHONPATH" in environment vars
print('Done by :- ',eg._owner_);

import manualimportout;

x = int(input('enter first no.'));
y = int(input('enter second no.'));

result = manualimportout.addi(x,y);
print('sum of given no. is : ',result);
print(manualimportout._version_);


#inbuilt modules example
#import sys;
#print('the path is : ',sys.path);

#importing only specific object from modules
#from sys import path;
#print('the path is :',path);
#modifying new value to old
#path='xyz'
#print('New value: ',path);

#importing all objects from modules
from sys import *;
print('the path is: ',path);
