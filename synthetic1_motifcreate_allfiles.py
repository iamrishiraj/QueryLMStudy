from igraph import *

for index in range(15,101):
    filename="artificial_random_1m_"+str(index)+"_lcc.txt"
    inputfile=open(filename,"r")
    lines=inputfile.readlines()
    inputfile.close()
    templist=[]
    lines=lines[2:]
    maxvalue=0
    for i in lines:
        i=i[:-1]
        words=i.split("\t\t\t")
        templist.append((int(words[0]),int(words[1])))
        if int(words[0])>maxvalue:
            maxvalue=int(words[0])
        if int(words[1])>maxvalue:
            maxvalue=int(words[1])
        
    g=Graph()
    g.add_vertices(maxvalue+1)
    g.add_edges(templist)

    outputname="synthetic1_"+str(index)+"_motif.txt"
    outputfile = open(outputname, "a")

    motifs_3=g.motifs_randesu(3)
    motifs_4=g.motifs_randesu(4)

    outputfile.write("\t")
    outputfile.write(str(motifs_3[2]))
    outputfile.write("\t")
    outputfile.write(str(motifs_3[3]))

    outputfile.write("\t")
    outputfile.write(str(motifs_4[6]))
    outputfile.write("\t")
    outputfile.write(str(motifs_4[7]))    
    outputfile.write("\t")
    outputfile.write(str(motifs_4[8]))
    outputfile.write("\t")
    outputfile.write(str(motifs_4[9]))
    outputfile.write("\t")
    outputfile.write(str(motifs_4[10]))
    outputfile.write("\n")
    outputfile.close()
