import random

#Word comes 1st and its selection
wordlist=[]
filename=open("AnjanaQueries.txt","r")
lines1=filename.readlines()
filename.close()
for i in lines1:
    words=i.split(" ")
    wordlist.append(words[0])

#Creating a list of bigrams with a common first word
#bigramdict stores bigrams in a dictionary
filename=open("globalbigram.txt","r")
lines=filename.readlines()
filename.close()
lines=lines[2:]
noofbigram=len(lines)
#Alternative word selct if not found
filename=open("Cumulative.txt","r")
line=filename.readlines()
line=line[2:]
filename.close()
backuplist=[]
for i in line:
    words=i.split("\t\t")
    backuplist.append(words[0])


tempdict={}
#bigramdict={}
for i in lines:
    i=i[:-1]
    words=i.split("\t\t")
    #bigramdict[words[0]]=float(words[1])
    finalwords=words[0].split(" ")
    count=int(noofbigram*float(words[1]))
    for j in range(0,count):
        try:
            tempdict[finalwords[0]].append(finalwords[1])
        except KeyError:
            tempdict[finalwords[0]]=[]
            tempdict[finalwords[0]].append(finalwords[1])

def calquery(index):
    querylist=[]
    word=random.sample(wordlist,1) #calculating the 1st word
    querylist.append(word[0])
    for i in range(1,index):
        try:
            tempbigramlist=tempdict[word[0]]
            nextword=random.sample(tempbigramlist,1)
        except KeyError:
            nextword=random.sample(backuplist,1)
        querylist.append(nextword[0])
        word[0]=nextword[0]

    for value in querylist:
        outputfile.write(str(value)+" ")
    outputfile.write("\n")

for index1 in range(1,101):
    if index1<10:
        outputname="synthetic6_random_1m_00"+str(index1)+".txt"
    elif index1<100:
        outputname="synthetic6_random_1m_0"+str(index1)+".txt"
    else:
        outputname="synthetic6_random_1m_"+str(index1)+".txt"
        
    outputfile=open(outputname,"w")
    

    for i in range(1,265201):
        calquery(2)

    for i in range(1,313001):
        calquery(3)
    for i in range(1,205001):
        calquery(4)
    for i in range(1,107001):
        calquery(5)
    for i in range(1,53701):
        calquery(6)
    for i in range(27601):
        calquery(7)
    for i in range(1,14801):
        calquery(8)
    for i in range(1,8001):
        calquery(9)
    for i in range(1,5701):
        calquery(10)


    outputfile.close()




