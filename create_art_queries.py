import random
templist=[]

nodefile=open("unstemwordnodelist.txt","r")
lines=nodefile.readlines()
finallines=lines[2:]
for i in finallines:
    words=i.split("\t\t\t")
    templist.append(words[1])
nodefile.close()

for index in range(1,101):
    if index<10:
        filename="artificial_random_1m_00"+str(index)+".txt"
    elif (index>=10 and index<100):
        filename="artificial_random_1m_0"+str(index)+".txt"
    else:
        filename="artificial_random_1m_"+str(index)+".txt"
    final=open(filename,"w")
    for i in range(1,1000001):
        rand=random.randint(2,10)
        temp=random.sample(templist,rand)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    final.close()    
