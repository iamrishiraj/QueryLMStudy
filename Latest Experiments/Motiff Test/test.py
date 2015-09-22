from igraph import *


templist=[]
templist.append((0,1))
templist.append((1,2))
templist.append((2,3))
templist.append((3,0))
templist.append((3,1))
templist.append((2,0))

g=Graph()
g.add_vertices(4)
g.add_edges(templist)
motifs_3=g.motifs_randesu(4)


outputfile=open("test_output.txt","w")
for i in motifs_3:
    try:
        outputfile.write(str(int(i)))
    except ValueError:
        pass
outputfile.close()
#For 3 vertices motif
# [1,2,3,4] is the output. 3 corresponds to 3 chain and 4 corresponds to 3 clique
# For 4 vertices motif
# [1,2,3,4,5,6,7,8,9,10,11] is the output.
#4 Chain corresponds to 7
#4 star corresponds to 5
#4 loop out correcponds to 8
#4 box - 9
#4 semi clique - 10
#4 clique - 11
