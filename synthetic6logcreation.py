import random

templist=[]

inputfile=open("Word_comes_1st_prob.txt","r")
lines=inputfile.readlines()
inputfile.close()
lines=lines[2:]
for i in lines:
    i=i[:-1]
    words=i.split("\t\t")
    templist.append((words[0],words[2]))

samplefile=open("globalbigram.txt","r")
bigramlines=samplefile.readlines()
samplefile.close()

tempfile=open("Cumulative.txt","r")
templine=tempfile.readlines()
tempfile.close()
templine=templine[2:]

outputfile=open("synthetic6.txt","w")
bigramlines=bigramlines[2:]
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
    totalvalue=0
    randlist.append(word)
    for i in bigramlines:
        words=i.split(" ")
        if words[0]==word:
            tempword=words[1].split("\t\t")
            randomdict[tempword[0]]=float(tempword[1])
            totalvalue+=float(tempword[1])
        else:
            pass
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
    outputfile.write(str(randlist[0]))
    outputfile.write(" ")
    outputfile.write(str(randlist[1]))
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
    for index in range(1,3):
        totalvalue=0
        flag=0
        randomdict={}
        for i in bigramlines:
            words=i.split(" ")
            if words[0]==word:
                tempword=words[1].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
                flag=1
            else:
                pass
        if flag!=1:
            rand=random.sample(templine,1)
            word=rand.split("\t\t")
            randomdict[word[0]]=float(word[1])
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
        
        word=i
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
    for index in range(1,4):
        totalvalue=0
        randomdict={}
        flag=0
        for i in bigramlines:
            words=i.split(" ")
            if words[0]==word:
                tempword=words[1].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
            else:
                pass
        if flag!=1:
            rand=random.sample(templine,1)
            word=rand.split("\t\t")
            randomdict[word[0]]=float(word[1])
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
         
        word=i
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
    for index in range(1,5):
        totalvalue=0
        randomdict={}
        flag=0
        for i in bigramlines:
            words=i.split(" ")
            if words[0]==word:
                tempword=words[1].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
            else:
                pass
        if flag!=1:
            rand=random.sample(templine,1)
            word=rand.split("\t\t")
            randomdict[word[0]]=float(word[1])
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
         
        word=i
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
    for index in range(1,6):
        totalvalue=0
        randomdict={}
        flag=0
        for i in bigramlines:
            words=i.split(" ")
            if words[0]==word:
                tempword=words[1].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
            else:
                pass
        if flag!=1:
            rand=random.sample(templine,1)
            word=rand.split("\t\t")
            randomdict[word[0]]=float(word[1])
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
         
        word=i
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
    for index in range(1,7):
        totalvalue=0
        randomdict={}
        flag=0
        for i in bigramlines:
            words=i.split(" ")
            if words[0]==word:
                tempword=words[1].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
            else:
                pass
        if flag!=1:
            rand=random.sample(templine,1)
            word=rand.split("\t\t")
            randomdict[word[0]]=float(word[1])
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
         
        word=i
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
    for index in range(1,8):
        totalvalue=0
        randomdict={}
        flag=0
        for i in bigramlines:
            words=i.split(" ")
            if words[0]==word:
                tempword=words[1].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
            else:
                pass
        if flag!=1:
            rand=random.sample(templine,1)
            word=rand.split("\t\t")
            randomdict[word[0]]=float(word[1])
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
         
        word=i
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
    for index in range(1,9):
        totalvalue=0
        randomdict={}
        flag=0
        for i in bigramlines:
            words=i.split(" ")
            if words[0]==word:
                tempword=words[1].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
            else:
                pass
        if flag!=1:
            rand=random.sample(templine,1)
            word=rand.split("\t\t")
            randomdict[word[0]]=float(word[1])
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
         
        word=i
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
    for index in range(1,10):
        totalvalue=0
        randomdict={}
        flag=0
        for i in bigramlines:
            words=i.split(" ")
            if words[0]==word:
                tempword=words[1].split("\t\t")
                randomdict[tempword[0]]=float(tempword[1])
                totalvalue+=float(tempword[1])
            else:
                pass
        if flag!=1:
            rand=random.sample(templine,1)
            word=rand.split("\t\t")
            randomdict[word[0]]=float(word[1])
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
         
        word=i
    for items in randlist:
        outputfile.write(str(items))
        outputfile.write(" ")
    outputfile.write("\n")

outputfile.close()
