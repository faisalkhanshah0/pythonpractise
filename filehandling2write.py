#!/usr/bin/env python
"""f=open('testwrite.txt','w+');
str='hello infogain \n';
f.write(str);
str='Best of luck!'
f.write(str);
f.close();"""

f=open('testwrite.txt','w+');
lines=['one\n','two\n','three\n'];
f.writelines(lines);
f.close();
