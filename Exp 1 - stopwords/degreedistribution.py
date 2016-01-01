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

    from collections import OrderedDict
    # make a new ordered dictionary from the original,
    # sorting its items by values
    d_sorted_by_value = OrderedDict(sorted(edge.items(), key=lambda x: x[1]))

    templist=[]
    maxvalue=0
    for k, v in d_sorted_by_value.items():
        templist.append((k,v))
        maxvalue=int(v)

    counter=0
    outputname="degree_dist_real_random_1m_1_lcc.txt"
    fileoutput=open(outputname,"w")
    numberofnodes=len(templist)
    for i in range(1,maxvalue+1):
        for (u,v) in templist:
            if int(v)<i:
                counter+=1
            else:
                break
        fractionnodes=(numberofnodes-counter)/float(numberofnodes)
        counter=0
        fileoutput.write(str(i))
        fileoutput.write("\t")
        fileoutput.write(str(fractionnodes))
        fileoutput.write("\n")

    fileoutput.close()
