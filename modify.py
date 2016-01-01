import sys
import re

file1=open(sys.argv[1],"r")
lines=file1.readlines()
file1.close()

file2=open(sys.argv[2],"w")

for i in lines:
    words=i.split("\t")
    words[1]=words[1].lower()
    pattern = re.compile('[^ a-zA-Z0-9_]')
    words[1] = re.sub(pattern, '', words[1])
    file2.write(words[1]+"\n")

file2.close()
