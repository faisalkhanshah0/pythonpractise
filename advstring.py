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
