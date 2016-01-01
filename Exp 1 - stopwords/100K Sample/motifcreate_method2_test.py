from igraph import *
import math
import sys

avglist=[]
for index in range(1,2):
    inputname="motif_test.txt"
    inputfile=open(inputname,"r")
    lines=inputfile.readlines()
    inputfile.close()
    templist=[]
    tempdict={}
    lines=lines[2:]
    maxvalue=0
    for i in lines:
        i=i[:-1]
        words=i.split("\t\t\t")
        tempdict[words[0]]=1
        tempdict[words[1]]=1
        templist.append((int(words[0]),int(words[1])))
        if int(words[0])>maxvalue:
            maxvalue=int(words[0])
        if int(words[1])>maxvalue:
            maxvalue=int(words[1])

        
    g=Graph()
    g.add_vertices(maxvalue+1)
    g.add_edges(templist)

    motifs_3=g.motifs_randesu(3)
    motifs_4=g.motifs_randesu(4)
    sum1=sum2=0
    for i in motifs_3:
        try:
            sum1+=int(i)
        except ValueError:
            pass
    for i in motifs_4:
        try:
            sum2+=int(i)
        except ValueError:
            pass
    nodes=len(tempdict)
    Nc3=(nodes*(nodes-1)*(nodes-2))/6
    Nc4=(nodes*(nodes-1)*(nodes-2)*(nodes-3))/24

    fraction3=[]
    fraction4=[]
    outputname="motif_test_output.txt"
    outputfile=open(outputname,"w")
    outputfile.write(str(nodes))
    outputfile.write(" ")
    ival=0
    for value in motifs_3:
        ival=float(value/Nc3)
        fraction3.append(ival)
        outputfile.write(str(value)+" ")
    outputfile.write(str(sum1)+" ")
    outputfile.write(str(Nc3)+" ")

    for value in motifs_4:
        ival=float(value/Nc4)
        fraction4.append(ival)
        outputfile.write(str(value)+" ")
    outputfile.write(str(sum2)+" ")
    outputfile.write(str(Nc4)+" ")

    outputfile.write("\n\n")
    
    if index==1:
        for values in motifs_3:
            try:
                avglist.append(values)
            except ValueError:
                pass
        for values in motifs_4:
            try:
                avglist.append(values)
            except ValueError:
                pass
    else:
        for i in range(0,3):
            avglist[i]= ((avglist[i]*(index-1))+ motifs_3[i])/index
        for i in range(4,15):
            avglist[i]= ((avglist[i]*(index-1))+ motifs_4[i-4])/index

    for value in avglist:
        outputfile.write(str(value)+" ")
    outputfile.close()
"""
    outputfile.write("\n\n")
    disconfract1=disconfract2=0
    for i in range(0,2):
        disconfract1+=fraction3[i]
    for i in range(0,6):
        disconfract2+=fraction4[i]
    loglist=[]
    for i in range(2,4):
        try:
            logval=math.log(float(fraction3[i]),10)
            loglist.append(logval)
        except ValueError:
            loglist.append(0)
        outputfile.write(str(fraction3[i])+" ")
    try:
        logval=math.log(float(disconfract1),10)
        loglist.append(logval)
    except ValueError:
            loglist.append(0)
    outputfile.write(str(disconfract1)+" ")
    
    for i in range(6,11):
        try:
            logval=math.log(float(fraction4[i]),10)
            loglist.append(logval)
        except ValueError:
            loglist.append(0)
        outputfile.write(str(fraction4[i])+" ")
    try:
        logval=math.log(float(disconfract2),10)
        loglist.append(logval)
    except ValueError:
            loglist.append(0)
    outputfile.write(str(disconfract2)+" ")

    outputfile.write("\n\n")
    for value in loglist:
        outputfile.write(str(value)+" ")"""
