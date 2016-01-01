import math
import sys

tempdict={}
bidict={}
filename=open(sys.argv[1],"r")
lines=filename.readlines()
filename.close()
for i in lines:
    i=i[:-1]
    words=i.split(" ")
    numberofwords=len(words) 
    for a in words:
        for b in words:
            if a!=b:
                try:
                    strname=a+" "+b
                    tempdict[strname]+=1
                except KeyError:
                    tempdict[strname]=1
                


for i in tempdict.keys():
    words=i.split(" ")
    try:
        bidict[words[0]]=bidict[words[0]]+"`"+words[1]
    except KeyError:
        bidict[words[0]]=words[1]

for i in bidict.keys():
    tsum=0
    words=bidict[i].split("`")
    for j in words:
        str1=i+" "+j
        tsum+=float(tempdict[str1])
    for j in words:
        str1=i+" "+j
        tempdict[str1]=float(tempdict[str1])/tsum
        
fileoutput=open(sys.argv[2],"w")
for i in bidict.keys():
    tsum=0
    words=bidict[i].split("`")
    for j in words:
        str1=i+" "+j
        tsum+=float(tempdict[str1])*math.log10(float(tempdict[str1]))/math.log10(2)
    negate=0-tsum
    fileoutput.write(str(i))
    fileoutput.write("\t\t")
    fileoutput.write(str(negate))
    fileoutput.write("\n")

fileoutput.close()


