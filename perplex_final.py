import math
import sys
unidict={}
filename=open(sys.argv[1],"r")
lines=filename.readlines()
filename.close()
lines=lines[2:]
for i in lines:
    i=i[:-1]
    words=i.split("\t\t") 
    unidict[words[0]]=float(words[1])

filename1=open(sys.argv[2],"r")
lines=filename1.readlines()
filename1.close()
lines=lines[2:]

for i in lines:
    i=i[:-1]
    words=i.split("\t\t")
    unidict[words[0]]=unidict[words[0]]*float(words[1])

ent=0
for i in unidict.keys():
    ent+=unidict[i]
perp=math.pow(2,ent)
print perp


