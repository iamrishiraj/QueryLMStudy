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
        filename="synthetic2_random_10m_00"+str(index)+".txt"
    elif (index>=10 and index<100):
        filename="synthetic2_random_10m_0"+str(index)+".txt"
    else:
        filename="synthetic2_random_10m_"+str(index)+".txt"
    final=open(filename,"w")
    for i in range(1,2651987):
        temp=random.sample(templist,2)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,3129982):
        temp=random.sample(templist,3)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,2049992):
        temp=random.sample(templist,4)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,1070001):
        temp=random.sample(templist,5)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,537006):
        temp=random.sample(templist,6)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,276008):
        temp=random.sample(templist,7)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,148009):
        temp=random.sample(templist,8)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,80010):
        temp=random.sample(templist,9)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,57014):
        temp=random.sample(templist,10)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    final.close()    
