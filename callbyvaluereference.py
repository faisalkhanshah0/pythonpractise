
#call by value examply
def abc(mylist):
    mylist=[6,7,8,9,10]
list=[1,2,3,4,5]
abc(list)
print(list)

#call by reference
def xyz(mylists):
    mylists.append([6,7,8,9,10])
lists=[1,2,3,4,5]
xyz(lists)
print(lists)
# os.system  #not working
# print subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()
