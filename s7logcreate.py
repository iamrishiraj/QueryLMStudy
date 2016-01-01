import random

#Bigram comes 1st and its selection
wordlist=[]
filename=open("AnjanaQueries.txt","r")
lines1=filename.readlines()
filename.close()
for i in lines1:
    i=i[:-1]
    words=i.split(" ")
    bigram=words[0]+" "+words[1]
    wordlist.append(bigram)

#Creating a list of trigrams with a common first bigram
filename=open("globaltrigram.txt","r")
lines=filename.readlines()
filename.close()
lines=lines[2:]
nooftrigram=len(lines)

#Alternative bigram select if not found
filename=open("globalbigram.txt","r")
bline=filename.readlines()
bline=bline[2:]
filename.close()
bigbackuplist=[]
for i in bline:
    words=i.split("\t\t")
    temp=words[0]+" "+words[1]
    bigbackuplist.append(temp)
    
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
    count=int(nooftrigram*float(words[1]))
    for j in range(0,count):
        try:
            keyval=finalwords[0]+" "+finalwords[1]
            tempdict[keyval].append(finalwords[2])
        except KeyError:
            keyval=finalwords[0]+" "+finalwords[1]
            tempdict[keyval]=[]
            tempdict[keyval].append(finalwords[2])


def cal2word():
    bigram2word=random.sample(wordlist,265200)
    for value in bigram2word:
        outputfile.write(str(value))
        outputfile.write("\n")
def calquery(index):
    querylist=[]
    word=random.sample(wordlist,1) #calculating the 1st word
    final=word[0].split(" ")
    querylist.append(final[0])
    querylist.append(final[1])
    flag=0
    for i in range(1,index-1):
        if flag==1:
            flag=0
            continue
        try:
            tempbigramlist=tempdict[word[0]]
            nextword=random.sample(tempbigramlist,1)
        except KeyError:
            if i==index-2:
                nextword=random.sample(backuplist,1)
            else:
                tempword=random.sample(bigbackuplist,1)
                intermed=tempword[0].split(" ")
                querylist.append(intermed[0])
                querylist.append(intermed[1])
                word[0]=intermed[0]+" "+intermed[1]
                flag=1
                tempfile=open("Intermediate_value.txt","r")
                value=tempfile.readline()
                tempfile.close()
                value=value[:-1]
                counter=int(value)
                counter+=1
                tempfile1=open("Intermediate_value.txt","w")
                tempfile1.write(str(counter))
                tempfile1.close()
                continue
            
        querylist.append(nextword[0])
        word[0]=final[1]+" "+nextword[0]
        final[1]=nextword[0]

    for value in querylist:
        outputfile.write(str(value)+" ")
    outputfile.write("\n")

counterfile=open("Counter_for_bigram_select.txt","a")
for index1 in range(1,2):
    tempfile=open("Intermediate_value.txt","w")
    tempfile.write("0")
    tempfile.close()
    if index1<10:
        outputname="synthetic7_random_1m_00"+str(index1)+".txt"
    elif index1<100:
        outputname="synthetic7_random_1m_0"+str(index1)+".txt"
    else:
        outputname="synthetic7_random_1m_"+str(index1)+".txt"
        
    outputfile=open(outputname,"w")
    


    cal2word()

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

    tempfile=open("Intermediate_value.txt","r")
    value=tempfile.readline()
    tempfile.close()
    value=value[:-1]
    counter1=int(value)   
    counterfile.write(str(counter1)+"\n")


    outputfile.close()

counterfile.close()


