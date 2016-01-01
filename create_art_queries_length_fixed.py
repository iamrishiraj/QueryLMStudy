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
        filename="artificial_random_1m_length_fixed_00"+str(index)+".txt"
    elif (index>=10 and index<100):
        filename="artificial_random_1m_length_fixed_0"+str(index)+".txt"
    else:
        filename="artificial_random_1m_length_fixed_"+str(index)+".txt"
    final=open(filename,"w")
    for i in range(1,265201):
        temp=random.sample(templist,2)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,313001):
        temp=random.sample(templist,3)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,205001):
        temp=random.sample(templist,4)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,107001):
        temp=random.sample(templist,5)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,53701):
        temp=random.sample(templist,6)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,27601):
        temp=random.sample(templist,7)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,14801):
        temp=random.sample(templist,8)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,8001):
        temp=random.sample(templist,9)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    for i in range(1,5701):
        temp=random.sample(templist,10)
        for j in temp:
            final.write(str(j))
            final.write(" ")
        final.write("\n")
    final.close()    
