import math

for index in range(1,2):
    reallist=[]
    inputname="degree_dist_2_real_random_1m_1_lcc.txt"
    inputfile=open(inputname,"r")
    lines=inputfile.readlines()
    inputfile.close()
    for i in lines:
        i=i[:-1]
        words=i.split("\t")
        reallist.append(words[1])

    artificiallist=[]
    inputname2="degree_dist_2_synthetic4_random_1m_001_stemmed_updated.txt"
    inputfile=open(inputname2,"r")
    lines=inputfile.readlines()
    inputfile.close()
    for i in lines:
        i=i[:-1]
        words=i.split("\t")
        artificiallist.append(words[1])

    realcount=len(reallist)
    syntheticcount=len(artificiallist)
    if realcount>syntheticcount:
        value=float(artificiallist[syntheticcount-1])/(realcount-syntheticcount+1)
        for i in range(0,realcount-syntheticcount):
            artificiallist.append(float(artificiallist[syntheticcount+i-1])+value)
            if float(artificiallist[syntheticcount+i])<1:
                artificiallist[syntheticcount+i]=1

    else:
        value=float(reallist[realcount-1])/(syntheticcount-realcount+1)
        for i in range(0,syntheticcount-realcount):
            reallist.append(float(reallist[realcount+i-1])+value)
            if float(reallist[realcount+i])<1:
                reallist[realcount+i]=1
    count1=count2=0
    for i in range(0,len(reallist)):
        count1+=float(reallist[i])
        count2+=float(artificiallist[i])

    for i in range(0,len(reallist)):
        reallist[i]=float(reallist[i])/count1
        artificiallist[i]=float(artificiallist[i])/count2


    outputfile=open("KL_Distribution_2_synthetic4_random_1m_001_stemmed_updated.txt","a")
    value=0
    for i in range(0,len(artificiallist)):
        interm=float(reallist[i])/float(artificiallist[i])
        interm1=math.log(interm)
        value+=float(reallist[i])*interm1

    outputfile.write("KL Divergence\t")
    outputfile.write(str(value))
    outputfile.write("\n")

    outputfile.close()
