import pickle;
f=open('test.dat','wb');
md={'a':1,'b':2,'c':3};
pickle.dump(md, f);  #write binary in opend file stream
f.close;


ifl=open('test.dat','rb');
md1=pickle.load(ifl); #reading data from binary file
ifl.close();
print(md1);
print(md1.a);#exact object value
