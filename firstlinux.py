#!/usr/bin/env python3


import os;
#import subprocess;
from subprocess import call, Popen, PIPE, check_output, getoutput;
#call(["cat", "oops1.py"]);
#print(dir(subprocess));

#subprocess.call(["mkdir", "testone"]);
#os.system("mkdir test");
#os.system("sudo systemctl restart jenkins")
#a = os.system("ls");
#b= call('ls -lt', shell=True);
#print(123)
#print(b);
#os.mkdir("test1");


#To pipe output from cmd to py var
#output3 = getoutput("ls -lt").split('\n');
#output = check_output("ls", shell=True)
#print(output3[0]);
#c=Popen("ls", shell=True, stdout=PIPE, stderr=PIPE)

#o, e = c.communicate();

#cmd = ["echo", "hi", ">", "a.txt"]
#call(cmd)

#call("echo {0} > a.txt".format(output3), shell=True);
#print(o);

#print('Output:' + o.decode('ascii'));
#print('Error:' + e.decode('ascii'));
#print('Code:' + str(c.returncode));


file_ = open("output.txt", "w");

Popen("sudo ls rootfolder/", shell=True, stdout=file_)
