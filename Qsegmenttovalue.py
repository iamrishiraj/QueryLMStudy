import pickle
import string

# Storing the distinct segments in the file in a dictionary
try:
    file_to_dict=open("allQueriesSegmented.txt","r")
    lines = file_to_dict.readlines()
    segdict={}
    counter=1
    seglen=0
    for i in lines:
        segments = i.split("\" ")
        for j in segments[0:]:
            seglen=len(j)
            if j[seglen-1]== "\n":
                store=j[:-1]
            else:
                j=j + "\""
                store=j
            if segdict.has_key(store):
                pass
            else:
                segdict[store]=counter
                counter=counter+1
    file_to_dict.close()
except IOError :
    print "The filename doesnt exist.Please check"

#Storing the segments in the dictionary in the file
dict_to_file=open("segmentlist.txt","w") 
pickle.dump(segdict,dict_to_file)  
dict_to_file.close()

#Creating a file in which the segments present in source file are stored as their
#counter values in another file
try:
    readfile=open("allQueriesSegmented.txt","r")
    seg_to_val=open("allQueriesSegmentedvalued.txt","w")
    rlines=readfile.readlines()
    for i in rlines:
        segments = i.split("\" ")
        for j in segments[0:]:
            seglen=len(j)
            if j[seglen-1]== "\n":
                store=j[:-1]
            else:
                store=j + "\""
            val=str(segdict[store])
            seg_to_val.write(val)
            seg_to_val.write(" ")
        seg_to_val.write("\n")
    readfile.close()
    seg_to_val.close()
except IOError :
    print "The filename doesnt exist.Please check"