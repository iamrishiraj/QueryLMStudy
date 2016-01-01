import random

templist=[]

inputfile=open("Bigram_comes_1st_prob.txt","r")
lines=inputfile.readlines()
inputfile.close()
lines=lines[2:]
for i in lines:
    i=i[:-1]
    words=i.split("\t\t")
    templist.append((words[0],words[2]))

samplefile=open("globaltrigram.txt","r")
trigramlines=samplefile.readlines()
samplefile.close()

tempfile=open("Cumulative.txt","r")
wordprob=tempfile.readlines()
tempfile.close()
wordprob=wordprob[2:]

tempfile2=open("globalbigram.txt","r")
bigramprob=tempfile2.readlines()
tempfile2.close()
bigramprob=bigramprob[2:]

outputfile=open("synthetic7.txt","w")
trigramlines=trigramlines[2:]
for i in range(1,265201):
    randlist=[]
    randomdict={}
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    outputfile.write(str(word))
    outputfile.write("\n")

    
for i in range(1,313001):
    randlist=[]
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    
    randlist.append(word)
    for index in range(1,2):
        totalvalue=0
        randomdict={}
        flag=0
        for i in trigramlines:
            words=i.split(" ")
            finalword=words[0]+" "+words[1]
            if word==finalword:
                tempword=words[2].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            rand=random.sample(wordprob,1)
            randlist.append(rand)
            break
            
        for i in randomdict.keys():
            randomdict[i]=randomdict[i]/totalvalue
        previous=0
        for i in randomdict.keys():
            randomdict[i]+=previous
            previous=randomdict[i]
        rand=random.random()
        for i in randomdict.keys():
            if rand<=randomdict[i]:
                randlist.append(i)
                break
            else:
                pass
        length=len(randlist)
        string1=randlist[length-2]+" "+randlist[length-1]
        strword=string1.split(" ")
        word=strword[1]+" "+strword[2]
    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")

    
for i in range(1,205001):
    randlist=[]
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    
    randlist.append(word)
    for index in range(1,3):
        totalvalue=0
        randomdict={}
        flag=0
        for i in trigramlines:
            words=i.split(" ")
            finalword=words[0]+" "+words[1]
            if finalword==word:
                tempword=words[2].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            if i<2:
                rand=random.sample(bigramprob,1)
                randlist.append(rand)
                break
            else:
                rand=random.sample(wordprob,1)
                randlist.append(rand)
                break
        for i in randomdict.keys():
            randomdict[i]=randomdict[i]/totalvalue
        previous=0
        for i in randomdict.keys():
            randomdict[i]+=previous
            previous=randomdict[i]
        rand=random.random()
        for i in randomdict.keys():
            if rand<=randomdict[i]:
                randlist.append(i)
                break
            else:
                pass
        length=len(randlist)
        string1=randlist[length-2]+" "+randlist[length-1]
        strword=string1.split(" ")
        word=strword[1]+" "+strword[2]

    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")
    
for i in range(1,107001):
    randlist=[]
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    
    randlist.append(word)
    for index in range(1,4):
        totalvalue=0
        randomdict={}
        flag=0
        for i in trigramlines:
            words=i.split(" ")
            finalword=words[0]+" "+words[1]
            if finalword==word:
                tempword=words[2].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            if i<3:
                rand=random.sample(bigramprob,1)
                randlist.append(rand)
                break
            else:
                rand=random.sample(wordprob,1)
                randlist.append(rand)
                break
        for i in randomdict.keys():
            randomdict[i]=randomdict[i]/totalvalue
        previous=0
        for i in randomdict.keys():
            randomdict[i]+=previous
            previous=randomdict[i]
        rand=random.random()
        for i in randomdict.keys():
            if rand<=randomdict[i]:
                randlist.append(i)
                break
            else:
                pass
        length=len(randlist)
        string1=randlist[length-2]+" "+randlist[length-1]
        strword=string1.split(" ")
        word=strword[1]+" "+strword[2]

    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")
    
for i in range(1,53701):
    randlist=[]
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    
    randlist.append(word)
    for index in range(1,5):
        totalvalue=0
        randomdict={}
        flag=0
        for i in trigramlines:
            words=i.split(" ")
            finalword=words[0]+" "+words[1]
            if finalword==word:
                tempword=words[2].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            if i<4:
                rand=random.sample(bigramprob,1)
                randlist.append(rand)
                break
            else:
                rand=random.sample(wordprob,1)
                randlist.append(rand)
                break
        for i in randomdict.keys():
            randomdict[i]=randomdict[i]/totalvalue
        previous=0
        for i in randomdict.keys():
            randomdict[i]+=previous
            previous=randomdict[i]
        rand=random.random()
        for i in randomdict.keys():
            if rand<=randomdict[i]:
                randlist.append(i)
                break
            else:
                pass
        length=len(randlist)
        string1=randlist[length-2]+" "+randlist[length-1]
        strword=string1.split(" ")
        word=strword[1]+" "+strword[2]

    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")
    
for i in range(1,27601):
    randlist=[]
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    
    randlist.append(word)
    for index in range(1,6):
        totalvalue=0
        randomdict={}
        flag=0
        for i in trigramlines:
            words=i.split(" ")
            finalword=words[0]+" "+words[1]
            if finalword==word:
                tempword=words[2].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            if i<5:
                rand=random.sample(bigramprob,1)
                randlist.append(rand)
                break
            else:
                rand=random.sample(wordprob,1)
                randlist.append(rand)
                break
        for i in randomdict.keys():
            randomdict[i]=randomdict[i]/totalvalue
        previous=0
        for i in randomdict.keys():
            randomdict[i]+=previous
            previous=randomdict[i]
        rand=random.random()
        for i in randomdict.keys():
            if rand<=randomdict[i]:
                randlist.append(i)
                break
            else:
                pass
        length=len(randlist)
        string1=randlist[length-2]+" "+randlist[length-1]
        strword=string1.split(" ")
        word=strword[1]+" "+strword[2]

    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")
    
for i in range(1,14801):
    randlist=[]
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    
    randlist.append(word)
    for index in range(1,7):
        totalvalue=0
        randomdict={}
        flag=0
        for i in trigramlines:
            words=i.split(" ")
            finalword=words[0]+" "+words[1]
            if finalword==word:
                tempword=words[2].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            if i<6:
                rand=random.sample(bigramprob,1)
                randlist.append(rand)
                break
            else:
                rand=random.sample(wordprob,1)
                randlist.append(rand)
                break
        for i in randomdict.keys():
            randomdict[i]=randomdict[i]/totalvalue
        previous=0
        for i in randomdict.keys():
            randomdict[i]+=previous
            previous=randomdict[i]
        rand=random.random()
        for i in randomdict.keys():
            if rand<=randomdict[i]:
                randlist.append(i)
                break
            else:
                pass
        length=len(randlist)
        string1=randlist[length-2]+" "+randlist[length-1]
        strword=string1.split(" ")
        word=strword[1]+" "+strword[2]

    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")
    
for i in range(1,8001):
    randlist=[]
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    
    randlist.append(word)
    for index in range(1,8):
        totalvalue=0
        randomdict={}
        flag=0
        for i in trigramlines:
            words=i.split(" ")
            finalword=words[0]+" "+words[1]
            if finalword==word:
                tempword=words[2].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            if i<7:
                rand=random.sample(bigramprob,1)
                randlist.append(rand)
                break
            else:
                rand=random.sample(wordprob,1)
                randlist.append(rand)
                break
        for i in randomdict.keys():
            randomdict[i]=randomdict[i]/totalvalue
        previous=0
        for i in randomdict.keys():
            randomdict[i]+=previous
            previous=randomdict[i]
        rand=random.random()
        for i in randomdict.keys():
            if rand<=randomdict[i]:
                randlist.append(i)
                break
            else:
                pass
        length=len(randlist)
        string1=randlist[length-2]+" "+randlist[length-1]
        strword=string1.split(" ")
        word=strword[1]+" "+strword[2]

    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")
    
for i in range(1,5701):
    randlist=[]
    rannum=random.random()
    for (u,v) in templist:
        if rannum<=float(v):
            word=u
            break
        else:
            pass
    
    randlist.append(word)
    for index in range(1,9):
        totalvalue=0
        randomdict={}
        flag=0
        for i in trigramlines:
            words=i.split(" ")
            finalword=words[0]+" "+words[1]
            if finalword==word:
                tempword=words[2].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            if i<8:
                rand=random.sample(bigramprob,1)
                randlist.append(rand)
                break
            else:
                rand=random.sample(wordprob,1)
                randlist.append(rand)
                break
        for i in randomdict.keys():
            randomdict[i]=randomdict[i]/totalvalue
        previous=0
        for i in randomdict.keys():
            randomdict[i]+=previous
            previous=randomdict[i]
        rand=random.random()
        for i in randomdict.keys():
            if rand<=randomdict[i]:
                randlist.append(i)
                break
            else:
                pass
        length=len(randlist)
        string1=randlist[length-2]+" "+randlist[length-1]
        strword=string1.split(" ")
        word=strword[1]+" "+strword[2]

    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")
    
outputfile.close()
