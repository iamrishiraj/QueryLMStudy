from igraph import *
for index in range(1,6):
    inputfile=open("n_by_1000_sample_000_"+index+"_lcc.txt","r")
    lines=inputfile.readlines()
    inputfile.close()
    tempdict={}
    templist=[]
    lines=lines[2:]
    maxvalue=0
    for i in lines:
        i=i[:-1]
        words=i.split("\t\t\t")
        templist.append((int(words[0]),int(words[1])))
        tempdict[words[0]]=1
        tempdict[words[1]]=1
        if int(words[0])>maxvalue:
            maxvalue=int(words[0])
        if int(words[1])>maxvalue:
            maxvalue=int(words[1])

    nodes=len(tempdict)
    edges=len(templist)
    nc3= (nodes*(nodes-1)*(nodes-2))/6
    nc4= (nodes*(nodes-1)*(nodes-2)*(nodes-3))/24
    g=Graph()
    g.add_vertices(maxvalue)
    g.add_edges(templist)

    motifs_3=g.motifs_randesu(3)
    motifs_4=g.motifs_randesu(4)
    sum3=0
    sum4=0
    for i in motifs_3:
        sum3+=i
    for i in motifs_4:
        sum4+=i

    disconct3=nc3-(motifs_3[2]+motifs_3[3])
    disconct4=nc4-(motifs_4[6]+motifs_4[7]+motifs_4[8]+motifs_4[9]+motifs_4[10])
    outputfile=open("n_by_1000_sample_000"+index+"_motif.txt","a")
    outputfile.write(str(index)+"\t"+str(nodes)+"\t")
    outputfile.write(str(motifs_3[0])+"\t"+str(motifs_3[1])+"\t")
    outputfile.write(str(motifs_3[2]))
    outputfile.write("\t")
    outputfile.write(str(motifs_3[3]))
    outputfile.write("\t"+str(disconct3)+"\t"+str(sum3)+"\t"+str(nc3)+"\t")
    for i in motifs_4:
        outputfile.write(str(i)+"\t")
    outputfile.write("\t"+str(disconct4)+"\t"+str(sum4)+"\t"+str(nc4)+"\t")
    outputfile.write("\n")
    outputfile.close()
