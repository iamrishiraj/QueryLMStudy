import sys
import random

file1=open(sys.argv[1],"r")
lines=file1.readlines()
file1.close()

list1=random.sample(lines,100000)

file2=open(sys.argv[2],"w")

for i in list1:
    file2.write(str(i))

file2.close()
