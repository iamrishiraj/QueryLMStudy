import pickle
nwordoccur={} #a dictionary which will contain the number of times a word occurs in a query
tempdict={}   #a dictionary for temporary storage of words

#counting the number of occurence of each word in a query and storing it in a dictionary
try:
    indexedfile=open("AnjanaQueries1.txt","r")
    lines=indexedfile.readlines()
    noofquery=len(lines)
    for i in lines:
        wordsinline = i.split(" ")
        lengthofquery=len(wordsinline)
        if tempdict.has_key(lengthofquery):
            tempdict[lengthofquery]+=1  
        else:
            tempdict[lengthofquery]=1
except IOError :
    print "The filename doesnt exist.Please check"
    
#loading the words with their index in a dictionary
for i in tempdict.keys():
    percent=tempdict[i]*100/float(noofquery)
    print i,
    print ":",
    print percent
