"""x=int(input('enter any no. to know the table of it.'))
print('-----------------table starts from here-----------------')
for i in range(1,11):
    print('{0} X {1} = {2}'.format(x,i,x*i))
else:
    print('-----------------table ended here-----------------')
"""
x=int(input('enter any no.'));

for i in range(1,11):
    print('{0} X {1} = {2}'.format(x,i,x*i));
else:
    print('table over');    