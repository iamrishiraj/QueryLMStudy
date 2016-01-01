import pickle
import sys


tempdict={}   #a dictionary for temporary storage of segments

#counting the number of occurence of each word in a query and storing it in a dictionary
try:
    segval=sys.argv[1];
    indexedfile=open(segval,"r")
    lines=indexedfile.readlines()
    nwords=0
    for i in lines:
        i=i[:-1];
        segmentsinline = i.split(" ")
        l=len(segmentsinline)
        for j in segmentsinline[0:]:
            if tempdict.has_key(j):
                tempdict[j]+=1
            else:
                tempdict[j]=1
        
        nwords+=l
    indexedfile.close()
except IOError :
    print "The filename doesnt exist.Please check"
    


#Creating a node list with the segments ,their index and the probability of their occurence
#(i.e the number of queries in which it occurs divided by total queries)

nodecreate="nodelist_"+sys.argv[1];
nodelist=open(nodecreate,"w")
nodelist.write("Word\t\tP(N)\n\n")
for i in tempdict:
    nodelist.write(i)
    nodelist.write("\t\t")
    prob=float(tempdict[i])/nwords
    nodelist.write(str(prob))
    nodelist.write("\n")
nodelist.close()
