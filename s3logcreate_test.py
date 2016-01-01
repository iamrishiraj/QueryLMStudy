import random

filename=open("AnjanaQueries.txt","r")
line=filename.readlines()
filename.close()
backuplist=[]
for i in line:
    i=i[:-1]
    words=i.split(" ")
    for j in words:
        backuplist.append(j)

def calquery(index):
    querylist=random.sample(backuplist,index)    
    for value in querylist:
        outputfile.write(str(value)+" ")
    outputfile.write("\n")

for index1 in range(1,2):
    if index1<10:
        outputname="synthetic3_random_10m_00"+str(index1)+".txt"
    elif index1<100:
        outputname="synthetic3_random_10m_0"+str(index1)+".txt"
    else:
        outputname="synthetic3_random_10m_"+str(index1)+".txt"
        
    outputfile=open(outputname,"w")
    

    for i in range(1,2651987):
        calquery(2)

    for i in range(1,3129982):
        calquery(3)
    for i in range(1,2049992):
        calquery(4)
    for i in range(1,1070001):
        calquery(5)
    for i in range(1,537006):
        calquery(6)
    for i in range(276008):
        calquery(7)
    for i in range(1,148009):
        calquery(8)
    for i in range(1,80010):
        calquery(9)
    for i in range(1,57014):
        calquery(10)
    outputfile.close()




