import sys

file1=open(sys.argv[1],"r")
file2=open(sys.argv[2],"w")
for i1 in file1:
    counter=1
    i1=i1.strip(" ")
    i1=i1.strip("\n")
    i1=" ".join(i1.split())
    words=i1.split(" ")
        
    tempdict={}
    for i in words:
        if i in tempdict.keys():
            pass
        else:
            tempdict[i]=counter
            counter+=1

    from collections import OrderedDict
    # make a new ordered dictionary from the original,
    # sorting its items by values
    d_sorted_by_value = OrderedDict(sorted(tempdict.items(), key=lambda x: x[1]))

    for k, v in d_sorted_by_value.items():
        file2.write(str(k)+" ")
    file2.write("\n")

file1.close()
file2.close()
