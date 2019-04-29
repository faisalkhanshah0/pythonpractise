#!/usr/bin/env python

text="Hello world"

for i in text:  #looping string chars
    print(i)
# print(text[0:4])
# print(text[:4])
# print(text[6:])
# print(text[0])
sliceofstr=text[0:4]; #slicing of string
print(sliceofstr);

print('Hell '*2)  #Repetetion of words

#searching char founc or not in string
print('H' in text);
# opp of 'in' is 'not in'

# print r'\n' #not working

#some string functions use case
print(text.upper()) #to change in uppercase
print(len(text))  # length of string

x=[2,1,6,3,6,4,7]
print(min(x)) #mathematical functions of min and max finding
print(max(x))
print(text.count('e'))  #finding position of given char in string

#advance operation on list
lists = ['apple', 'mango', 'banana', 'grapes', 'guava', 'orange'];  #mutablity ex

print(lists[1]);
newlist = lists[1:3];
print(newlist);
newlist.append('kiwi');
print(newlist);
# del newlist[2]
# same as
newlist[2:] = [];
print(newlist)
# print(lists.reverse()) #not working right now
newlist.clear();
print(newlist)

tuples = ('apple', 'mango', 'banana', 'grapes')
print(tuples[2:4]);
# tuples[0] = 'not possible';  # immutablality

# dict
dicts = {1:'shah',2:'faisal',3:'khan'};
print(dicts[2]);
dicts2 = {'fname':'shah','sname':'faisal','lname':'khan'};
print(dicts2['lname']);
dicts2['class'] = 'A' #APPENDING DICTIONARY WITH KEY VALUE PAIR
dicts2['extra'] = 'extra'
del dicts2['extra']  #deleting key value pair
print(dicts2);


#set eg

bri = set(['brazil', 'russia', 'india'])
bri.add('china');
bric = bri.copy();
print('india' in bri);
print(bri)
print(bric)
