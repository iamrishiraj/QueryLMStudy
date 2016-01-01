import sys
lendict={}
filename=open(sys.argv[1],"r")
counter=0
for line in filename:
    counter+=1
    line=line.strip('"')
    words=line.split('" "')
    dictlen=len(words)
    try:
        lendict[dictlen]+=1
    except KeyError:
        lendict[dictlen]=1

for i in lendict.keys():
    lendict[i]=float(lendict[i]*100)/counter

print counter

print lendict

for i in lendict.keys():
    lendict[i]=int(lendict[i]*1000000)/100

print lendict
