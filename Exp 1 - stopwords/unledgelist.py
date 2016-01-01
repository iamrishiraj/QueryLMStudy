import pickle
import networkx as nx
import sys

for index in range(1,2):
    tempedge={}
    edgedict={}

    try:
        segval="Value_synthetic4_random_1m_001_stemmed_updated.txt"#+sys.argv[1]
        readfile=open(segval,"r")
        lines=readfile.readlines() #stored all the lines in a list
        n=len(lines)    #the number of queries
    except IOError :
        print "The filename doesnt exist.Please check"
        
    readfile.close()
    for i in lines:
        finalline=i[:-2]        #for neglecting the white space character and \n at the end of each line
        words=finalline.split(" ") #words will contain the list of words present in each line
        for i in range(0,len(words)-2):
            localwords=[words[i],words[i+1],words[i+2]]
            #sort the list of words
            localwords.sort()
            for j in localwords:
                for k in localwords:
                    if j<k:
                        tempedge[(j,k)]=1 #a method to form an edge between each words(global)

        #store the edge in graph M where weight is equal to number of occurence of edge in the graph as a whole to evaluate P(ij)=number of queries in which the edge occurs/total query    
        for (u,v) in tempedge:
            try:
                edgedict[(u,v)]+=1
            except KeyError:
                edgedict[(u,v)]=1
        tempedge={}


    #Creating the edge list for unrestricted global graph
    edgelist="unl_synthetic4_random_1m_001_stemmed_updated.txt"#+sys.argv[1]
    f2=open(edgelist,"w")
    f2.write("Node 1\t\t\t")
    f2.write("Node 2\t\t\t")
    f2.write("P(12)\n\n")
    for (u,v) in edgedict:
        f2.write(str(u))
        f2.write("\t\t\t")
        f2.write(str(v))
        f2.write("\t\t\t")
        prob=float(edgedict[(u,v)])/n
        f2.write(str(prob))
        f2.write("\n")

    f2.close()
    
                
