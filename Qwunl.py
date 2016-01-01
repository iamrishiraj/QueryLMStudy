import pickle
import networkx as nx
import os

counter=0
tempedge=[]
G=nx.Graph()
M=nx.Graph()

try:
    readfile=open("allQueriesvalued.txt","r")
    lines=readfile.readlines() #stored all the lines in a list
    n=len(lines)    #the number of queries
except IOError :
    print "The filename doesnt exist.Please check"
    
readfile.close()
for i in lines:
    os.system("clear")
    counter+=1
    percentage= (100*counter)/float(n)
    print percentage
    finalline=i[:-2]        #for neglecting the white space character and \n at the end of each line
    words=finalline.split(" ") #words will contain the list of words present in each line
    for i in range(0,len(words)-2):
        localwords=[words[i],words[i+1],words[i+2]]
        #sort the list of words
        localwords.sort()
        for j in localwords:
            for k in localwords:
                if j<k:
                    tempedge.append((j,k)) #a method to form an edge between each words(global)

    G.add_edges_from(tempedge)      #a temporary graph used to remove duplicate edges
    #store the edge in graph M where weight is equal to number of occurence of edge in the graph as a whole to evaluate P(ij)=number of queries in which the edge occurs/total query    
    for u,v in G.edges():
        try:
            M[u][v]['weight']+=1
        except KeyError:
            M.add_weighted_edges_from([(u,v,1)])
    G.remove_edges_from(tempedge)
    tempedge=[]


M.remove_edge(-1,-1)
#Creating the edge list for unrestricted global graph
f2=open("qwunl.txt","w")
f2.write("Node 1\t\t\t")
f2.write("Node 2\t\t\t")
f2.write("P(12)\n\n")
for u,v,edata in M.edges(data=True):
    f2.write(str(u))
    f2.write("\t\t\t")
    f2.write(str(v))
    f2.write("\t\t\t")
    prob=float(M[u][v]['weight'])/n
    f2.write(str(prob))
    f2.write("\n")

f2.close()
    
                
