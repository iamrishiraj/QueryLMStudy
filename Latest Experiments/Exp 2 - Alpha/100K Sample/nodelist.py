import pickle
import sys

for index in range(1,2):
    nsegmentoccur={} #a dictionary which will contain the number of times a segment occurs in a query
    tempdict={}   #a dictionary for temporary storage of segments

    #counting the number of occurence of each word in a query and storing it in a dictionary
    try:
        segval="Value_synthetic4_random_0.1m_001_stemmed.txt"#+sys.argv[1]
        indexedfile=open(segval,"r")
        lines=indexedfile.readlines()
        noofquery=len(lines)
        for i in lines:
            segmentsinline = i.split(" ")
            for j in segmentsinline[0:]:
                if tempdict.has_key(j):
                    pass
                else:
                    tempdict[j]=1
            for k in tempdict.keys():
                if nsegmentoccur.has_key(k):
                    nsegmentoccur[k]=nsegmentoccur[k] + 1
                else:
                    nsegmentoccur[k]=1
            tempdict={}
        indexedfile.close()
    except IOError :
        print "The filename doesnt exist.Please check"
        
    #loading the segments with their index in a dictionary
    try:
        listname="list_synthetic4_random_0.1m_001_stemmed.txt"#+sys.argv[1]
        loadsegments=open(listname,"r")
        segments=pickle.load(loadsegments)
        loadsegments.close()
    except IOError :
        print "The filename doesnt exist.Please check"

    from collections import OrderedDict
    # make a new ordered dictionary from the original,
    # sorting its items by values
    d_sorted_by_value = OrderedDict(sorted(segments.items(), key=lambda x: x[1]))

    #Creating a node list with the segments ,their index and the probability of their occurence
    #(i.e the number of queries in which it occurs divided by total queries)

    nodecreate="nodelist_synthetic4_random_0.1m_001_stemmed.txt"#+sys.argv[1]
    nodelist=open(nodecreate,"w")
    nodelist.write("N(index)\t\t\tWord\t\t\tP(N)\n\n")
    for k, v in d_sorted_by_value.items():
        nodelist.write(str(v))
        nodelist.write("\t\t\t")
        nodelist.write(str(k))
        nodelist.write("\t\t\t")
        prob=float(nsegmentoccur[str(v)])/noofquery
        nodelist.write(str(prob))
        nodelist.write("\n")
    nodelist.close()
