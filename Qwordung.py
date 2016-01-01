import pickle
import networkx as nx
import os

counter=0
c=1
temp=0
tempedge={}
edgedict={}

try:
    readfile=open("allQueriesvalued.txt","r")
    lines=readfile.readlines() #stored all the lines in a list
    n=len(lines)    #the number of queries
except IOError :
    print "The filename doesnt exist.Please check"
    
readfile.close()
for i in lines:
    os.system("clear")
    temp+=1
    counter+=1
    percentage= (100*counter)/float(n)
    print percentage
    if temp==5000:
        file=open("temp.txt","w")
        nlines=5000*c
	file.write(str(nlines))
	c=c+1
	temp=0
	file.close()
    else:
	pass
    finalline=i[:-2]        #for neglecting the white space character and \n at the end of each line
    words=finalline.split(" ") #words will contain the list of words present in each line
    #sort the list of words
    words.sort()
    for j in words:
        for k in words:
            if j<k:
                tempedge[(j,k)]=1 #a method to form an edge between each words(global)

    #store the edge in dictionary edgedict where value is equal to number of occurence of edge in the graph as a whole to evaluate P(ij)=number of queries in which the edge occurs/total query    
    for (u,v) in tempedge:
        try:
            edgedict[(u,v)]+=1
        except KeyError:
            edgedict[(u,v)]=1
    tempedge={}

#Creating the edge list for unrestricted global graph
f2=open("qwordunglobal.txt","w")
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
    
                
