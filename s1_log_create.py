import random
templist=[]

nodefile=open("Cumulative.txt","r")
lines=nodefile.readlines()
finallines=lines[2:]
for i in finallines:
    words=i.split("\t\t")
    templist.append(words[0])
nodefile.close()

for index in range(1,2):
    if index<10:
        filename="synthetic1_random_10m_00"+str(index)+".txt"
    elif (index>=10 and index<100):
        filename="synthetic1_random_10m_0"+str(index)+".txt"
    else:
        filename="synthetic1_random_10m_"+str(index)+".txt"
    final=open(filename,"w")
    for i in range(1,10000001):
        rand=random.randint(2,10)
        temp=random.sample(templist,rand)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    final.close()    
