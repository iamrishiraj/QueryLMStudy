import random
import sys

#Word comes 1st and its selection
seglist=[]
filename=open(sys.argv[1],"r")
for i in filename:
    i=i.strip('\n')
    i=i.strip('"')
    seg=i.split('" "')
    for j in seg:
        finalseg='"'+j+'"'
        seglist.append(finalseg)

filename.close()

def calquery(index):
    querylist=[]
    segment=random.sample(seglist,index-1) #selecting the segments
    
    for i in segment:
        querylist.append(i)

    for value in querylist:
        outputfile.write(str(value)+" ")
    outputfile.write("\n")

for index1 in range(1,101):
    if index1<10:
        outputname="segment_synthetic3_random_1m_00"+str(index1)+".txt"
    elif index1<100:
        outputname="segment_synthetic3_random_1m_0"+str(index1)+".txt"
    else:
        outputname="segment_synthetic3_random_1m_"+str(index1)+".txt"
        
    outputfile=open(outputname,"w")
    

    for i in range(1,105365+1):
        calquery(2)

    for i in range(1,450523+1):
        calquery(3)
    for i in range(1,272681+1):
        calquery(4)
    for i in range(1,105527+1):
        calquery(5)
    for i in range(1,40445+1):
        calquery(6)
    for i in range(16105+1):
        calquery(7)
    for i in range(1,6429+1):
        calquery(8)
    for i in range(1,2238+1):
        calquery(9)
    for i in range(1,588+1):
        calquery(10)
    for i in range(1,99+1):
        calquery(11)

    outputfile.close()




