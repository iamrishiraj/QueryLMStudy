def smooth():
    temp=temp1=0
    counter=0
    position=0
    for i in degdist.values():
        position+=1
        if i==0:
            counter+=1
        elif (counter!=0 and i!=0):
            temp1=i
            break
        else:
            temp=i

    if temp1>temp:
        value=float(temp1-temp)/(counter+1)
        final=temp+value
    else:
        value=float(temp-temp1)/(counter+1)
        final=temp-value
    if temp1!=temp:
        if temp1>temp:
            for index in range(0,counter):
                degdist[position-counter+index]=final
                final+=value
        else:
            for index in range(0,counter):
                degdist[position-counter+index]=final
                final-=value
    else:
        for index in range(0,counter):
            degdist[position-counter+index]=temp1




for index in range(1,2):
    edge={}
    redgelist="real_random_1m_1_lcc.txt"
    edgefile=open(redgelist,"r")
    lines=edgefile.readlines()
    final=lines[2:]
    for i in final:
        finalline=i[:-1]
        nodes=finalline.split("\t\t\t")
        try:
            edge[nodes[0]]+=1
        except KeyError:
            edge[nodes[0]]=1
        try:
            edge[nodes[1]]+=1
        except KeyError:
            edge[nodes[1]]=1
    edgefile.close()

    maxdeg=max(edge.values())
    noofnodes=len(edge)
    degdist={}

    for i in range(1,maxdeg+1):
        degdist[i]=0
        
    for i in range(1,maxdeg+1):
        for j in edge.values():
            if j==i:
                degdist[j]+=1
                
    smooth()
    flag=0
    while(flag!=1):
        count=0
        for j in degdist.values():
            count+=1
            if j==0:
                smooth()
                break
            elif(count==maxdeg) :
                flag=1
    outputfile="degree_dist_2_real_random_1m_1_lcc.txt"
    fileoutput=open(outputfile,"w")
    for i in range(1,maxdeg+1):
        #fractionnodes=degdist[i]/float(noofnodes)
        fileoutput.write(str(i))
        fileoutput.write("\t")
        fileoutput.write(str(degdist[i]))
        #fileoutput.write("\t")
        #fileoutput.write(str(fractionnodes))
        fileoutput.write("\n")

    fileoutput.close()
