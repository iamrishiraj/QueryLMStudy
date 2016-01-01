import pickle
nwordoccur={} #a dictionary which will contain the number of times a word occurs in a query
tempdict={}   #a dictionary for temporary storage of words

#counting the number of occurence of each word in a query and storing it in a dictionary
try:
    indexedfile=open("AnjanaQueriesvalued.txt","r")
    lines=indexedfile.readlines()
    noofquery=len(lines)
    for i in lines:
        wordsinline = i.split(" ")
        for j in wordsinline[0:]:
            if tempdict.has_key(j):
                pass
            else:
                tempdict[j]=1
        for k in tempdict.keys():
            if nwordoccur.has_key(k):
                nwordoccur[k]=nwordoccur[k] + 1
            else:
                nwordoccur[k]=1
        tempdict={}
    indexedfile.close()
except IOError :
    print "The filename doesnt exist.Please check"
    
#loading the words with their index in a dictionary
try:
    loadwords=open("unstemwordlist.txt","r")
    words=pickle.load(loadwords)
    loadwords.close()
except IOError :
    print "The filename doesnt exist.Please check"

from collections import OrderedDict
# make a new ordered dictionary from the original,
# sorting its items by values
d_sorted_by_value = OrderedDict(sorted(words.items(), key=lambda x: x[1]))

#Creating a node list with the words ,their index and the probability of their occurence
#(i.e the number of queries in which it occurs divided by total queries)

nodelist=open("unstemwordnodelist.txt","w")
nodelist.write("N(index)\t\t\tWord\t\t\tP(N)\n\n")
for k, v in d_sorted_by_value.items():
    nodelist.write(str(v))
    nodelist.write("\t\t\t")
    nodelist.write(str(k))
    nodelist.write("\t\t\t")
    prob=float(nwordoccur[str(v)])/noofquery
    nodelist.write(str(prob))
    nodelist.write("\n")
nodelist.close()
