def sidemethod():
    try:
        if(len(tempbigramdict)!=0):
            maxval1=max1=0
            max1=max(tempbigramdict.values())
            for u,v in tempbigramdict.items():
                    if v==max1:
                        w=u.split(" ")
                        querylist.append(w[0])
                        ##querylist.append(w[1])
                        newword=w[1]
                        break

            dict2={}
            for i in tempbigramdict.keys():
                wd=i.split(" ")
                if (wd[0]==w[0] or wd[1]==w[0]):
                    dict2[i]=tempbigramdict[i]
                    
            for i in dict2.keys():
                del tempbigramdict[i]

            while(len(tempbigramdict.keys())!=0):
                dict1={}
                for i in tempbigramdict.keys():
                    wd=i.split(" ")
                    if wd[0]==newword:
                        dict1[i]=tempbigramdict[i]
                        
                                    
                maxval1=max(dict1.values())
                for u,v in dict1.items():
                    if v==maxval1:
                        w=u.split(" ")
                        querylist.append(w[0]) #####
                        newword=w[1]
                        break
                
                dict2={}
                for i in tempbigramdict.keys():
                    wd=i.split(" ")
                    if (wd[0]==w[0] or wd[1]==w[0]):
                        dict2[i]=tempbigramdict[i]
                        
                for i in dict2.keys():
                    del tempbigramdict[i]
            querylist.append(w[1]) #####
    except ValueError:
        sidemethod()



inputfile=open("Bigram_comes_1st_prob.txt","r")
bigram_1st={}
lines=inputfile.readlines()
lines=lines[2:]
inputfile.close()
for i in lines:
    i=i[:-1]
    temp=i.split("\t\t")
    bigram_1st[temp[0]]=float(temp[1])

inputfile=open("Consecutive_Bigram_Probability.txt","r")
bigram={}
lines=inputfile.readlines()
lines=lines[2:]
inputfile.close()
for i in lines:
    i=i[:-1]
    temp=i.split("\t\t")
    bigram[temp[0]]=float(temp[1])


file1=open("s6_1m_sample_1.txt","r")
file2=open("s8_1m_sample_1.txt","w")
lines=file1.readlines()
file1.close()

for i1 in lines:
    try:
        tempdict={}
        querylist=[]
        tempbigramdict={}
        i1=i1[:-1]
        words=i1.split(" ")
        for j in words:
            tempdict[j]=1
        for a in tempdict.keys():
            for b in tempdict.keys():
                if a!=b:
                    str1=a+" "+b
                    str2=b+" "+a
                    try:
                        tempbigramdict[str1]=bigram[str1]
                    except KeyError:
                        pass
                    try:
                        tempbigramdict[str2]=bigram[str2]
                    except KeyError:
                        pass
        intermid={}
        for i in tempbigramdict.keys():
            try:
                intermid[i]=bigram_1st[i]
            except KeyError:
                pass
        if len(intermid)==0:
            file2.write(str(i1)+"\n")
            continue
        
        maxval=max(intermid.values())
        for u,v in intermid.items():
            if v==maxval:
                w=u.split(" ")
                querylist.append(w[0])
                # querylist.append(w[1])
                newword=w[1]
                break
        dict1={}
        for i in tempbigramdict.keys():
            wd=i.split(" ")
            if (wd[0]==w[0] or wd[1]==w[0]):
                dict1[i]=tempbigramdict[i]
                
        for i in dict1.keys():
            del tempbigramdict[i]
       
        length=len(tempdict)-2
        while(length!=0):
            list1=[]
            dict1={}
            for i in tempbigramdict.keys():
                wd=i.split(" ")
                if wd[0]==newword:
                    dict1[i]=tempbigramdict[i]
                    list1.append(wd[1])
                    
                                
            maxval1=max(dict1.values())
            for u,v in dict1.items():
                if v==maxval1:
                    w=u.split(" ")
                    querylist.append(w[0]) ###
                    newword=w[1]
                    break
            
            length-=1
            dict2={}
            for i in tempbigramdict.keys():
                wd=i.split(" ")
                if (wd[0]==w[0] or wd[1]==w[0]):
                    dict2[i]=tempbigramdict[i]
                    
            for i in dict2.keys():
                del tempbigramdict[i]
        querylist.append(w[1]) ####
                
    except ValueError:
        querylist.append(w[1])
        sidemethod()
 
    flag=0
    templist=querylist
    for i in tempdict.keys():
        for j in templist:
            if i==j:
                flag=1
                break
        if flag==0:
            querylist.append(str(i))
        flag=0
        
    for i in querylist:
        file2.write(str(i)+" ")
    file2.write("\n")
              
file2.close()


