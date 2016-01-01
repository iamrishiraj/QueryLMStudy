import sys
import math

filename=sys.argv[1]

file1=open(filename,"r")
lines=file1.readlines()
file1.close()
lines=lines[2:]
"lines=lines.sort()"
tsum=0
for i in lines:
    i=i[:-1]
    words=i.split("\t\t")
    tsum+=float(words[1])*math.log10(float(words[1]))/math.log10(2)
    
tsum=0-tsum
final=math.pow(2,tsum)
print final
        
    
        
            
